#!/usr/bin/env python3
"""
SYNC TO SHEET WITH AUTOMATED QUALITY GATES (scripts/sync_to_sheet.py)
Cổng kiểm duyệt tự động ngăn chặn hoàn toàn việc:
1. Gán trùng ảnh giữa các testcase (Zero Duplication Gate).
2. Ảnh không tồn tại hoặc rỗng (File Integrity Gate).
3. Ghi đè vào các ca Mobile App bị loại trừ (Blacklist Gate).
4. Tính toán sai offset dòng (Auto-Discovery Row Mapping Gate).
"""

import os
import sys
import json
import hashlib
import subprocess
import argparse
from datetime import datetime

# Nạp động cấu hình từ TEST_CONFIG.md
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from config_loader import load_global_config

GLOBAL_CFG = load_global_config()
SPREADSHEET_ID = GLOBAL_CFG["admin_spreadsheet_id"]

def calculate_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def run_quality_gate(sheet_name, execution_data, skip_patterns=None):
    print(f"\n==========================================")
    print(f"🔒 RUNNING QUALITY GATE FOR: {sheet_name}")
    print(f"==========================================")
    
    if skip_patterns is None:
        skip_patterns = ['App', 'Mobile', 'Camera', 'Livestream']

    used_evidence_paths = {}
    used_hashes = {}
    errors = []

    for item in execution_data:
        tc_id = item.get('tc_id', '').strip()
        result = item.get('result', '').strip()
        evidence_path = item.get('evidence_path', '').strip()

        # Check skip blacklist
        is_skip = any(pattern.lower() in tc_id.lower() or pattern.lower() in item.get('title', '').lower() for pattern in skip_patterns)
        if is_skip:
            if result or evidence_path:
                errors.append(f"Gate Blacklist Violation: TC {tc_id} belongs to Mobile/App and MUST remain blank!")
            continue

        if not result:
            continue

        # 1. Check path collision (Zero Duplication)
        if evidence_path in used_evidence_paths:
            errors.append(f"Gate 1 Failed (Duplicate Path): TC {tc_id} reuses evidence of {used_evidence_paths[evidence_path]} -> {evidence_path}")
        else:
            used_evidence_paths[evidence_path] = tc_id

        # 2. Check file existence
        if not os.path.exists(evidence_path):
            errors.append(f"Gate 2 Failed (File Missing): TC {tc_id} file not found: {evidence_path}")
            continue

        # 3. Check file size
        size = os.path.getsize(evidence_path)
        if size < 10240: # < 10KB
            errors.append(f"Gate 2 Failed (File Too Small/Empty): TC {tc_id} file size is only {size} bytes: {evidence_path}")

        # 4. Check file hash collision (Anti-Shortcut Zero Identical Images)
        f_hash = calculate_file_hash(evidence_path)
        if f_hash in used_hashes:
            errors.append(f"Gate 4 Failed (Duplicate Image Content): TC {tc_id} has identical SHA256 image as {used_hashes[f_hash]}")
        else:
            used_hashes[f_hash] = tc_id

    if errors:
        print("\n❌ QUALITY GATE REJECTED! Found violations:")
        for err in errors:
            print(f"  • {err}")
        print("\n🚫 ABORTING SYNC TO GOOGLE SHEET. Fix all violations before retrying.\n")
        sys.exit(1)

    print(f"✅ 100% Quality Gates Passed! ({len(used_evidence_paths)} unique atomic evidence files verified)")

def sync_to_sheet(sheet_name, execution_data, dry_run=False):
    env = os.environ.copy()
    env['HOME'] = GLOBAL_CFG["home_dir"]
    env['AGY_ACCOUNT'] = GLOBAL_CFG["agy_account"]

    print(f"\n📡 Querying Google Sheet '{sheet_name}' for exact row mapping...")
    cmd = ['gsheets', 'readonly', 'read', SPREADSHEET_ID, f'{sheet_name}!A1:A300', '--json']
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error reading Google Sheet:", res.stderr)
        sys.exit(1)

    sheet_rows = json.loads(res.stdout)
    mapping = {}
    for idx, row in enumerate(sheet_rows, start=1):
        if not row or len(row) == 0:
            continue
        first_col = str(row[0]).strip()
        # Nhận diện mọi dòng bắt đầu bằng mã testcase [MÃ-X]
        if first_col.startswith('[') and ('-' in first_col or ']' in first_col):
            clean_id = first_col.replace('[', '').replace(']', '').strip()
            mapping[clean_id] = idx
            mapping[first_col] = idx

    print(f"Found {len(mapping)} testcase row mappings on Sheet '{sheet_name}'.")

    # Build row writes
    updates_by_row = {}
    current_date = datetime.now().strftime("%d.%m.%Y")
    for item in execution_data:
        tc_id = item.get('tc_id', '').strip()
        clean_id = tc_id.replace('[', '').replace(']', '').strip()
        row_num = mapping.get(clean_id) or mapping.get(tc_id)
        if not row_num:
            print(f"⚠️ Warning: Could not find row for {tc_id} on Sheet '{sheet_name}'")
            continue

        result = item.get('result', '')
        tester = GLOBAL_CFG["creator"] if result else ''
        date_str = current_date if result else ''
        ev_path = item.get('evidence_path', '') if result else ''
        updates_by_row[row_num] = [result, '', tester, date_str, ev_path]

    if dry_run:
        print(f"DRY RUN: Prepared {len(updates_by_row)} updates. No changes written.")
        return

    # Write individually or in sequential blocks
    sorted_rows = sorted(updates_by_row.keys())
    print(f"Writing {len(sorted_rows)} rows to '{sheet_name}'...")
    for row_num in sorted_rows:
        row_data = updates_by_row[row_num]
        range_str = f"{sheet_name}!H{row_num}:L{row_num}"
        val_str = ','.join(row_data)
        cmd_w = ['gsheets', 'mutate', 'write', SPREADSHEET_ID, range_str, val_str]
        res_w = subprocess.run(cmd_w, env=env, capture_output=True, text=True)
        if res_w.returncode != 0:
            print(f"Error writing {range_str}: {res_w.stderr}")

    print(f"🎉 Successfully synchronized 100% test results to '{sheet_name}'!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Sync Test Results to Google Sheet with Quality Gates")
    parser.add_argument('--sheet', required=True, help="Sheet name (e.g. AP213, AP330, AP405)")
    parser.add_argument('--input', required=True, help="Path to JSON file containing execution results")
    parser.add_argument('--dry-run', action='store_true', help="Check gates without writing to sheet")
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        data = json.load(f)

    run_quality_gate(args.sheet, data)
    sync_to_sheet(args.sheet, data, dry_run=args.dry_run)
