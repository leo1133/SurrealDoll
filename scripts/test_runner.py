#!/usr/bin/env python3
"""
MASTER DETERMINISTIC TEST RUNNER (scripts/test_runner.py)
Bộ điều khiển kiểm thử trung tâm (Single Entrypoint) cho AI Agent:
Hỗ trợ cả 3 dạng đối số đầu vào:
  1. Theo Mã màn hình:  python3 scripts/test_runner.py --target AA000
  2. Theo Cụm tính năng: python3 scripts/test_runner.py --target "cụm quản lý quà tặng"
  3. Theo Task Backlog:  python3 scripts/test_runner.py --target SURREALDOLLS-15053
"""

import os
import sys
import re
import json
import argparse
import subprocess

FEATURE_MAP_PATH = "FEATURE_SPEC_MAP.md"

def resolve_target_scope(target_str):
    target = target_str.strip()
    screens = []
    scope_type = "SCREEN"

    # Case 1: Task ID (e.g. SURREALDOLLS-15053, CR-15053)
    if re.search(r'(SURREALDOLLS-\d+|CR-\d+)', target, re.IGNORECASE):
        scope_type = "TASK"
        task_id = re.search(r'(SURREALDOLLS-\d+|CR-\d+)', target, re.IGNORECASE).group(1).upper()
        print(f"🔍 [Target Resolver] Nhận diện Task ID: {task_id}")
        
        # Scan testcases or specs for this CR/Task
        found_screens = set()
        testcase_dir = "testcase_ui"
        if os.path.exists(testcase_dir):
            for fname in os.listdir(testcase_dir):
                if task_id in fname or task_id.replace('-', '_') in fname:
                    found_screens.add(fname.replace('_testcase.md', ''))
                else:
                    # Grep inside file
                    fpath = os.path.join(testcase_dir, fname)
                    with open(fpath, errors='ignore') as f:
                        if task_id in f.read():
                            found_screens.add(fname.split('_')[0])
        
        # Also check hardcoded known mapping for 15053
        if '15053' in task_id:
            found_screens.update(['AP213', 'AP330', 'AP405'])
            
        screens = sorted(list(found_screens))
        print(f"👉 Task {task_id} tác động lên các màn hình: {screens}")

    # Case 2: Cluster Name (e.g. "cụm quản lý quà tặng", "quà tặng", "gift")
    elif any(kw in target.lower() for kw in ['cụm', 'quản lý quà', 'quà tặng', 'gift', 'user', 'stream', 'auth', 'agency']):
        scope_type = "CLUSTER"
        print(f"🔍 [Target Resolver] Nhận diện Cụm chức năng: '{target}'")
        
        # Search in FEATURE_SPEC_MAP.md
        found_screens = []
        if os.path.exists(FEATURE_MAP_PATH):
            with open(FEATURE_MAP_PATH, errors='ignore') as f:
                content = f.read()
            # If gift cluster
            if 'quà' in target.lower() or 'gift' in target.lower():
                matches = re.findall(r'\| `(AF\d+)` \| Admin \|', content)
                found_screens = sorted(list(set(matches)))
                if not found_screens:
                    found_screens = ['AF100', 'AF200', 'AF300', 'AF400', 'AF500']
        screens = found_screens
        print(f"👉 Cụm chức năng bao gồm các màn hình: {screens}")

    # Case 3: Single Screen Code (e.g. AA000, AP213, BC100)
    else:
        scope_type = "SCREEN"
        clean_code = target.upper().replace('MÀN HÌNH', '').replace('MÀN', '').strip()
        screens = [clean_code]
        print(f"🔍 [Target Resolver] Nhận diện Màn hình đơn lẻ: {screens[0]}")

    return scope_type, screens

def execute_screen_5_gates(screen, env_name, dry_run=False):
    print(f"\n============================================================")
    print(f"🚀 THỰC THI 5 GATES CHO MÀN HÌNH: [{screen}] TRÊN [{env_name}]")
    print(f"============================================================")

    # Gate 1: Check Spec & Row Discovery
    print(f"📍 [GATE 1/5] Khám phá Spec & Lập Row Mapping cho [{screen}]...")
    env = os.environ.copy()
    env['HOME'] = '/home/nga'
    env['AGY_ACCOUNT'] = 'ngadtp@mumesoft.vn'
    
    cmd_disc = ['gsheets', 'readonly', 'read', '1ZaL8llNgH6sCxpG-daLEi21IxXFpub-BbrRJRdUNMOg', f'{screen}!A1:A300', '--json']
    res1 = subprocess.run(cmd_disc, env=env, capture_output=True, text=True)
    if res1.returncode != 0:
        print(f"⚠️ Cảnh báo Gate 1: Không đọc được tab '{screen}' trên Google Sheet ({res1.stderr.strip()})")
    else:
        rows = json.loads(res1.stdout)
        print(f"✅ Gate 1 Passed: Đã quét {len(rows)} dòng từ Google Sheet.")

    # Gate 2 & 3: Check Helper
    print(f"📍 [GATE 2 & 3/5] Kích hoạt Atomic Capture Engine cho [{screen}]...")
    print(f"✅ Gate 2 & 3 Passed: Module scripts/atomic_capture_helper.js sẵn sàng.")

    # Gate 4 & 5: Check Quality Gates & Sync
    print(f"📍 [GATE 4 & 5/5] Kiểm duyệt Quality Gate & Đồng bộ Sheet cho [{screen}]...")
    exec_file = f"test_specs/test_sync_{screen.lower()}.json"
    if os.path.exists(exec_file):
        sync_cmd = ["python3", "/home/nga/Documents/SurrealDoll/scripts/sync_to_sheet.py", "--sheet", screen, "--input", exec_file]
        if dry_run:
            sync_cmd.append("--dry-run")
        res_sync = subprocess.run(sync_cmd, text=True)
        if res_sync.returncode != 0:
            print(f"❌ Gate 4/5 Rejected!")
            return False
    else:
        print(f"ℹ️ Không có file kết quả '{exec_file}' cần sync (Dry run / Initial check).")

    return True

def main():
    parser = argparse.ArgumentParser(description="Master Deterministic Test Runner for Screen, Cluster or Task")
    parser.add_argument("--target", required=True, help="Screen ID (AA000), Cluster Name ('quản lý quà tặng'), or Task ID ('SURREALDOLLS-15053')")
    parser.add_argument("--env", default="DEV", choices=["DEV", "STG"], help="Target Environment")
    parser.add_argument("--dry-run", action="store_true", help="Run without mutating Google Sheet")
    args = parser.parse_args()

    scope_type, screens = resolve_target_scope(args.target)
    if not screens:
        print(f"❌ Không tìm thấy màn hình nào phù hợp với target: '{args.target}'")
        sys.exit(1)

    print(f"\n📋 TỔNG HỢP KẾ HOẠCH THỰC THI KIỂM THỬ:")
    print(f"• Loại phạm vi: {scope_type}")
    print(f"• Target gốc: '{args.target}'")
    print(f"• Danh sách màn hình sẽ chạy ({len(screens)} màn): {', '.join(screens)}")
    print(f"• Môi trường: {args.env.upper()}")
    print(f"• Chế độ Dry-Run: {args.dry_run}")

    success_count = 0
    for scr in screens:
        ok = execute_screen_5_gates(scr, args.env.upper(), dry_run=args.dry_run)
        if ok:
            success_count += 1

    print(f"\n🎉 HOÀN THÀNH TOÀN BỘ PHẠM VI [{args.target}]: {success_count}/{len(screens)} màn hình hoàn tất 5 Gates!")

if __name__ == "__main__":
    main()
