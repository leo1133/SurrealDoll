#!/usr/bin/env python3
"""
Automated Quality Gate (3-Gate Audit) for SurrealDoll UI & API Testcase Markdown files.
Detects bundled/compressed testcases (violating Atomic Test Case rule), header count mismatches,
missing required columns, and automation ratio violations.
Usage:
    python3 scripts/audit_testcases.py <file1.md> [file2.md ...]
"""

import re
import sys
from pathlib import Path

TC_ROW_RE = re.compile(r"^\|\s*`?\[([A-Za-z0-9_\s-]+)\]`?\s*\|")
RANGE_BUNDLING_RE = re.compile(
    r"(?:[A-Z]+-\d{2,3}\.\.(?:[A-Z]+-)?\d{2,3}|Viewpoint\s+\d+-\d+)", re.IGNORECASE
)
MULTI_BOUNDARY_RE = re.compile(
    r"(?:0,\s*-1|-\d+,\s*\d+\.\d+,\s*['\"]?abc|999999.*abc|\?page=-1.*99999.*abc|0B,\s*5MB,\s*>\s*5MB)",
    re.IGNORECASE,
)
MULTI_ERROR_RE = re.compile(r"(\bCMMSG8\b.*\bCMMSG1\b|\bCMMSG1\b.*\bCMMSG10\b|\bCMMSG43\b.*\bCMMSG45\b)")
VALID_AUTO_TAGS = ("Auto-UI", "Auto-API", "Auto-Data", "Manual-Only")


def parse_cells(line: str) -> list[str]:
    # Tách cột theo | nhưng không tách dấu \| được escape
    raw_cells = re.split(r"(?<!\\)\|", line.strip().strip("|"))
    parts = [c.replace(r"\|", "|").strip() for c in raw_cells]
    return parts


def audit_file(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"File not found: {path}"]

    lines = path.read_text(encoding="utf-8").splitlines()
    is_ui = path.name.endswith("_testcase.md")
    is_api = path.name.endswith("_api.md")

    tc_rows: list[tuple[int, str, list[str]]] = []
    for idx, line in enumerate(lines, start=1):
        m = TC_ROW_RE.match(line)
        if m:
            tc_rows.append((idx, m.group(1), parse_cells(line)))

    if not tc_rows:
        errors.append("No testcase rows found matching `| [ID] | ...`")
        return errors

    # 1. Check Dashboard Total Testcases for UI
    if is_ui:
        for line in lines[:25]:
            m = re.search(r"\*\*Total Testcases\*\*\s*\|\s*\*\*(\d+)\*\*", line)
            if m:
                declared = int(m.group(1))
                if declared != len(tc_rows):
                    errors.append(
                        f"Dashboard Total Testcases ({declared}) != actual rows ({len(tc_rows)})"
                    )
                break

    # 2. Check each row for bundling & required columns
    auto_count = 0
    manual_count = 0

    for line_no, tc_id, cells in tc_rows:
        row_text = " | ".join(cells)

        if RANGE_BUNDLING_RE.search(row_text):
            errors.append(f"Line {line_no} [{tc_id}]: Range bundling detected ({RANGE_BUNDLING_RE.search(row_text).group(0)})")

        if MULTI_BOUNDARY_RE.search(row_text):
            errors.append(f"Line {line_no} [{tc_id}]: Multiple boundary values bundled in 1 row")

        if MULTI_ERROR_RE.search(row_text):
            errors.append(f"Line {line_no} [{tc_id}]: Multiple CMMSG error codes bundled in 1 row")

        if is_ui:
            if len(cells) < 8:
                errors.append(f"Line {line_no} [{tc_id}]: Expected 8 columns, got {len(cells)}")
                continue
            title, big_item, feasibility = cells[1], cells[2], cells[7]
            if not title or not big_item:
                errors.append(f"Line {line_no} [{tc_id}]: Blank Title or Big item")
            if not any(feasibility.startswith(tag) for tag in VALID_AUTO_TAGS):
                errors.append(f"Line {line_no} [{tc_id}]: Invalid Automation Feasibility '{feasibility}'")
            elif feasibility.startswith("Manual-Only"):
                manual_count += 1
                if "(" not in feasibility:
                    errors.append(f"Line {line_no} [{tc_id}]: Manual-Only missing reason in parentheses")
            else:
                auto_count += 1

        elif is_api:
            if len(cells) < 14:
                errors.append(f"Line {line_no} [{tc_id}]: Expected >= 14 columns (with VP ID & Test Type), got {len(cells)}")
                continue
            vp_id, test_type, r1, r2 = cells[1], cells[10], cells[12], cells[13]
            if not vp_id:
                errors.append(f"Line {line_no} [{tc_id}]: Missing VP ID")
            if test_type not in ("Positive", "Negative", "Boundary", "Security", "Performance"):
                errors.append(f"Line {line_no} [{tc_id}]: Invalid Test Type '{test_type}'")
            if r1 or r2:
                errors.append(f"Line {line_no} [{tc_id}]: R1/R2 must be empty on design handover")

    # 3. Check Automation Feasibility golden ratio (70-85% Auto / 15-30% Manual) & Minimum Depth
    if is_ui and tc_rows:
        if len(tc_rows) < 15:
            errors.append(
                f"[Anti-Scaffolding Violation]: Số lượng ca kiểm thử ({len(tc_rows)} TCs) quá ít, vi phạm Ranh giới đỏ số 7 (tối thiểu >= 15 TCs cho 1 màn hình/tính năng)."
            )
        auto_pct = (auto_count / len(tc_rows)) * 100
        if auto_pct < 65 or auto_pct > 90:
            errors.append(
                f"Automation ratio out of range: {auto_pct:.1f}% Auto ({auto_count}/{len(tc_rows)}). Target ~70-85%."
            )

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/audit_testcases.py <file1.md> [file2.md ...]")
        return 2

    all_passed = True
    for arg in sys.argv[1:]:
        p = Path(arg)
        errs = audit_file(p)
        if errs:
            all_passed = False
            print(f"[FAIL] {p} ({len(errs)} issues):")
            for e in errs:
                print(f"  - {e}")
        else:
            lines = p.read_text(encoding="utf-8").splitlines()
            cnt = sum(1 for l in lines if TC_ROW_RE.match(l))
            print(f"[PASS] {p} ({cnt} atomic testcases, 0 violations)")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
