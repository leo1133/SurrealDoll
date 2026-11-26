#!/usr/bin/env python3
"""
Sync FEATURE_SPEC_MAP.md from Google Sheet 'Overview' data (JSON) and local project artifacts.
Usage:
  python3 scripts/sync_feature_map.py [--input path/to/overview.json]
"""

import argparse
import json
import os
import re
from collections import defaultdict

PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_OVERVIEW_PATHS = [
    os.path.join(PROJ_ROOT, 'test_specs', 'overview_latest.json'),
    '/Users/ngaphuong/.gemini/antigravity/brain/3f1b4fa9-6802-4055-9ca0-2ef2e6f8bc87/scratch/overview.json',
]
CATEGORIZED_FALLBACK = '/Users/ngaphuong/.gemini/antigravity/brain/3f1b4fa9-6802-4055-9ca0-2ef2e6f8bc87/scratch/categorized.json'
OUT_PATH = os.path.join(PROJ_ROOT, 'FEATURE_SPEC_MAP.md')


def scan_local_artifacts():
    artifacts = defaultdict(set)
    dirs = {
        'Q&A': 'Q&A',
        'testcase_ui': 'TC-UI',
        'testcase_api': 'TC-API',
        'bugs': 'Bug',
        'test_specs': 'SpecJSON',
        'automation': 'Auto',
    }
    for d, label in dirs.items():
        p = os.path.join(PROJ_ROOT, d)
        if not os.path.exists(p):
            continue
        for entry in os.listdir(p):
            matches = re.findall(r'\b([A-Z]{1,2}\d{3,4}[A-Z]?)\b', entry)
            for m in matches:
                artifacts[m].add(label)
    return artifacts


def classify_screen(sid, name_en, orig_grp):
    """Fallback classifier for newly added screens not in categorized.json."""
    u_id = sid.upper().strip()
    u_grp = orig_grp.upper().strip()

    if u_grp == 'ADMIN' or u_id.startswith(('AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AP', 'AQ', 'AS', 'AX', 'AY')):
        grp = 'Admin'
        if u_id.startswith(('AA', 'AB', 'AC')):
            mod = '1. Tài khoản Quản trị & Phân quyền (Auth & Permissions)'
        elif u_id.startswith('AD'):
            mod = '2. Quản lý Agency / Đại lý (Agency Management)'
        elif u_id.startswith('AE') or u_id == 'K2022':
            mod = '3. Quản lý Người dùng (User Management)'
        elif u_id.startswith('AF'):
            mod = '4. Quản lý Quà tặng (Gift Management)'
        elif u_id.startswith('AG'):
            mod = '5. Giám sát & Quản lý Phòng Livestream (Stream Management)'
        elif u_id.startswith('AH'):
            mod = '6. Quản lý Thông báo & Tin nhắn Admin (Announcements & Messages)'
        elif u_id.startswith('AI'):
            mod = '7. Quản lý Báo cáo vi phạm (Report Management)'
        elif u_id.startswith('AJ'):
            mod = '8. Quản lý BGM & Nhạc nền (BGM Management)'
        elif u_id.startswith('AK'):
            mod = '9. Quản lý Hình nền & Mini Garden (Background & Garden Management)'
        elif u_id.startswith('AL'):
            mod = '10. Quản lý Karaoke & Báo cáo Bản quyền (Karaoke & Copyright Reports)'
        elif u_id.startswith('AM'):
            mod = '11. Quản lý Bài đăng (Post Management)'
        elif u_id.startswith('AP'):
            mod = '12. Quản lý 3D Model & Avatar (3D Model & Avatar Management)'
        elif u_id.startswith('AQ'):
            mod = '13. Quản lý Gacha (Gacha Management)'
        elif u_id.startswith('AS'):
            mod = '14. Báo cáo Doanh thu & Rút tiền (Sales & Financial Analytics)'
        elif u_id.startswith('AX'):
            mod = '15. Quản lý & Giám sát Tin nhắn (User Messages Monitoring)'
        elif u_id.startswith('AY'):
            mod = '16. Giám sát Bình luận & Cấm Chat Livestream (Livestream Chat Monitoring)'
        else:
            mod = '3. Quản lý Người dùng (User Management)'
        return grp, mod

    if u_grp == 'AGENCY' or u_id.startswith(('BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'BX', 'BY')):
        grp = 'Agency'
        if u_id.startswith('BA'):
            mod = '1. Xác thực & Mật khẩu Agency (Auth & Password)'
        elif u_id.startswith('BB'):
            mod = '2. Quản lý Thông tin Agency & Quản trị viên (Agency Info & Staff Admin)'
        elif u_id.startswith(('BC', 'BD')):
            mod = '3. Quản lý Streamer / Liver & Tài chính (Streamer Management & Analytics)'
        elif u_id.startswith('BE'):
            mod = '4. Quản lý Bài đăng của Streamer (Streamer Posts)'
        elif u_id.startswith('BF'):
            mod = '5. Giám sát Livestream của Streamer (Streamer Livestream Management)'
        elif u_id.startswith('BG'):
            mod = '6. Quản lý Báo cáo vi phạm liên quan (Report Management)'
        else:
            mod = '7. Giám sát Tin nhắn & Bình luận Chat (Message & Chat Monitoring)'
        return grp, mod

    grp = 'App'
    if u_id.startswith(('A0', 'A1', 'A3')) or 'login' in name_en.lower():
        mod = '1. Đăng nhập & Khởi tạo tài khoản (Login & Authentication)'
    elif u_id.startswith('A2'):
        mod = '2. Hướng dẫn, Điều khoản & Trợ giúp Webview (Help, Policies & Legal)'
    elif u_id.startswith('B'):
        mod = '3. Trang chủ, Gợi ý & Nhiệm vụ (Home, Recommend & Missions)'
    elif u_id.startswith('C') and not u_id.startswith('CMR'):
        mod = '4. Tìm kiếm (Search)'
    elif u_id.startswith('D'):
        mod = '5. Trang cá nhân người khác & Video lưu trữ (Other User Profile & Archive)'
    elif u_id.startswith('E') or u_id == 'I8042':
        mod = '6. Thông báo & Hoạt động (Announcements & Notifications)'
    elif u_id.startswith('F'):
        mod = '7. Tin nhắn 1-1 / Hòm thư (Direct Messages)'
    elif u_id.startswith('G'):
        mod = '8. Cửa hàng, Nạp Coin, Gacha & Gói tháng (Shop, Currency, Gacha & Subscription)'
    elif u_id.startswith('I'):
        mod = '9. Livestream - Khán giả (Viewer Livestream Experience)'
    elif u_id.startswith('M') or u_id == 'OBS' or u_id.startswith('CMR') or 'stream' in name_en.lower():
        mod = '10. Livestream - Streamer & OBS (Streamer Broadcasting & Tools)'
    elif u_id.startswith('K'):
        mod = '11. Trang cá nhân của tôi & Cài đặt hệ thống (My Page, Account & Settings)'
    elif u_id.startswith('L'):
        mod = '12. Cộng đồng Familia, Bài đăng & Backnumber (Familia Fanclub & Content)'
    else:
        mod = '11. Trang cá nhân của tôi & Cài đặt hệ thống (My Page, Account & Settings)'
    return grp, mod


def main():
    parser = argparse.ArgumentParser(description='Sync FEATURE_SPEC_MAP.md from Overview JSON')
    parser.add_argument('--input', help='Path to overview JSON file')
    args = parser.parse_args()

    ov_path = args.input
    if not ov_path:
        for p in DEFAULT_OVERVIEW_PATHS:
            if os.path.exists(p):
                ov_path = p
                break
    if not ov_path or not os.path.exists(ov_path):
        raise FileNotFoundError('Could not find overview JSON. Pass --input <path>.')

    with open(ov_path, 'r', encoding='utf-8') as f:
        ov = json.load(f)

    # Load existing categorized mapping as baseline if available
    known_map = {}
    if os.path.exists(CATEGORIZED_FALLBACK):
        with open(CATEGORIZED_FALLBACK, 'r', encoding='utf-8') as f:
            old_cat = json.load(f)
        for g, mods in old_cat.items():
            for m_title, items in mods.items():
                for it in items:
                    known_map[(str(it.get('stt', '')).strip(), str(it.get('id', '')).strip(), str(it.get('name_en', '')).strip())] = (g, m_title)

    # Build fresh categorized structure from overview.json
    cat = {'Admin': defaultdict(list), 'Agency': defaultdict(list), 'App': defaultdict(list)}
    new_screens = []
    ov_map = {}

    for row in ov[2:]:
        if len(row) < 4:
            continue
        stt = str(row[0]).strip()
        orig_grp = str(row[1]).strip() if len(row) > 1 else ''
        sid = str(row[2]).strip() if len(row) > 2 else ''
        name_en = str(row[3]).strip() if len(row) > 3 else ''
        name_jp = str(row[4]).strip() if len(row) > 4 else ''
        if not sid and not name_en:
            continue

        spec_stt = str(row[5]).strip() if len(row) > 5 else ''
        be_stt = str(row[6]).strip() if len(row) > 6 else ''
        fe_stt = str(row[8]).strip() if len(row) > 8 else ''
        tc_stt = str(row[12]).strip() if len(row) > 12 else ''
        test_stt = str(row[14]).strip() if len(row) > 14 else ''
        is_close = str(row[22]).strip() if len(row) > 22 else ''
        note = str(row[23]).strip() if len(row) > 23 else ''

        key = (stt, sid, name_en)
        ov_map[key] = {
            'spec': spec_stt, 'be': be_stt, 'fe': fe_stt,
            'tc': tc_stt, 'test': test_stt, 'close': is_close, 'note': note,
        }

        if key in known_map:
            grp, mod = known_map[key]
        else:
            grp, mod = classify_screen(sid, name_en, orig_grp)
            new_screens.append((grp, mod, sid, name_en))

        cat[grp][mod].append({
            'stt': stt,
            'id': sid,
            'name_en': name_en,
            'name_jp': name_jp,
            'orig_grp': orig_grp,
            'note': note,
        })

    # Import subcluster generator from local scripts/subcluster_rules.py
    import sys
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    from subcluster_rules import get_subclusters

    local_artifacts = scan_local_artifacts()
    section_num = {'Admin': 'II', 'Agency': 'III', 'App': 'IV'}
    all_subclusters = {}
    total_sub = 0
    total_all_screens = 0

    for grp in ['Admin', 'Agency', 'App']:
        mods = cat[grp]
        sorted_mod_keys = sorted(mods.keys(), key=lambda k: int(k.split('.', 1)[0]) if k.split('.', 1)[0].isdigit() else 999)
        grp_subs = []
        for mod_title in sorted_mod_keys:
            subs = get_subclusters(grp, mod_title, mods[mod_title])
            grp_subs.append((mod_title, subs))
            total_sub += len(subs)
            total_all_screens += len(mods[mod_title])
        all_subclusters[grp] = grp_subs

    md = []
    md.append('# BẢN ĐỒ PHÂN RÃ TÍNH NĂNG & ĐẶC TẢ HỆ THỐNG SURREALDOLL (FEATURE & SPEC MAP)\n')
    md.append(f'> **Mục đích:** Tài liệu tra cứu nhanh cấu trúc tính năng chi tiết ({total_all_screens} màn hình, 35 cụm gốc -> **{total_sub} cụm tính năng chi tiết**) dùng trực tiếp khi **Test / Verify Bug / Phân tích Spec** cho dự án SurrealDoll.')
    md.append('> **Cách sử dụng nhanh:** Khi kiểm thử hoặc verify bug, chỉ cần nêu **Mã màn hình** (VD: `BD500`, `AQ100`, `I303`, `K203`) hoặc **Tên tính năng** (VD: *2-shot*, *Payout*, *ACRCloud*, *Gacha*), AI sẽ tra cứu ngay cụm tính năng, spec cốt lõi, điểm cần verify và các màn hình liên quan chéo (Admin ↔ Agency ↔ App).')
    md.append('> **Nguồn dữ liệu gốc:** Google Spreadsheet `1pxox5GcjOXwKadMnzOa765ptG2huPJSxCiWsrH0_h7Y` (Sheet `Overview`) + Kho tài liệu local (`Q&A/`, `testcase_ui/`, `testcase_api/`, `bugs/`, `test_specs/`).\n')

    md.append('---\n')
    md.append('## I. TỔNG QUAN HỆ THỐNG & MA TRẬN LIÊN KẾT CHÉO (CROSS-ROLE MATRIX)\n')
    md.append('| Nhóm (Group) | Vai trò | Số cụm gốc | Số cụm chi tiết | Số màn hình |')
    md.append('| :--- | :--- | :---: | :---: | :---: |')
    for grp, desc, base_cnt in [
        ('Admin', 'CMS Quản trị trung tâm toàn nền tảng', 16),
        ('Agency', 'Cổng Portal cho Công ty quản lý / Đại lý Streamer', 7),
        ('App', 'Ứng dụng Mobile (iOS/Android) & Webview tích hợp', 12),
    ]:
        sc_cnt = sum(len(s) for _, s in all_subclusters[grp])
        scr_cnt = sum(len(it) for _, subs in all_subclusters[grp] for _, _, _, _, it in subs)
        md.append(f'| **{grp}** | {desc} | {base_cnt} | {sc_cnt} | {scr_cnt} |')
    md.append(f'| **TỔNG** | **Toàn bộ hệ thống SurrealDoll** | **35** | **{total_sub}** | **{total_all_screens}** |\n')

    md.append('### Ma trận Nghiệp vụ Liên thông 3 Cổng (Admin ↔ Agency ↔ App)\n')
    md.append('> Dùng để kiểm tra ảnh hưởng dây chuyền (Regression / Side-effect) khi verify bug.\n')
    md.append('| Luồng Nghiệp vụ | Admin CMS | Agency Portal | Mobile App / Webview |')
    md.append('| :--- | :--- | :--- | :--- |')
    md.append('| **Quản lý Agency & Liên kết Liver** | `AD100`, `AD200`, `AD301`, `AD302` | `BA100`, `BB100-BB300`, `BC100`, `BC200` | `K203` (Join/Exit Agency) |')
    md.append('| **Hồ sơ User, eKYC & Xóa tài khoản** | `AE100`, `AE200`, `AE700`, `K2022` | `BC100`, `BC200` | `K000`, `K800`, `K205` (eKYC), `K2022` |')
    md.append('| **Tài sản, Billing & Doanh thu / Rút tiền** | `AE300-AE800`, `AS100`, `AS200`, `AS300`, `AS500` | `BD100-BD500` | `G501-G702`, `K601-K6013`, `K906-K9066` |')
    md.append('| **Giám sát Livestream, Ban & Archive** | `AG100-AG500`, `AY100-AY300` | `BF100-BF500`, `BY100`, `BY300` | `I099-I805`, `M100-M500`, `D701-D705`, `K9051-K9054`, `OBS` |')
    md.append('| **Quà tặng, 3D Model, BG & Gacha** | `AF100-AF500`, `AP000-AP400`, `AK201-AK303`, `AQ100-AQ500` | - | `A209`, `G200-G302`, `I600-I701`, `M0011-M00131`, `M20501-M20504` |')
    md.append('| **Karaoke, BGM & Bản quyền (JASRAC/ACRCloud)** | `AJ100-AJ400`, `AL100-AL400`, `AL600`, `AL700` | - | `I501-I509`, `M401-M409`, `M20514`, `K010-K0142`, `K209-New` |')
    md.append('| **Bài đăng Familia & Kiểm duyệt** | `AM100`, `AM101`, `AM200` | `BE100`, `BE200` | `L100-L600` |')
    md.append('| **Tin nhắn, Thông báo & Báo cáo Vi phạm** | `AH100-AH400`, `AI100-AI200`, `AX100-AX300` | `BG100-BG200`, `BX100` | `E201-E203`, `F100-F500`, `D2021-D2023`, `I804` |\n')

    quick_index = []
    for grp in ['Admin', 'Agency', 'App']:
        grp_subs = all_subclusters[grp]
        total_screens = sum(len(it_list) for _, subs in grp_subs for _, _, _, _, it_list in subs)
        s_idx = section_num[grp]
        md.append(f'\n---\n## {s_idx}. NHÓM: {grp.upper()} ({total_screens} MÀN HÌNH)\n')

        for mod_title, subs in grp_subs:
            mod_count = sum(len(s[4]) for s in subs)
            md.append(f'### {mod_title} ({mod_count} màn hình)\n')

            for sub_title, spec, verify, cross, sub_items in subs:
                md.append(f'#### {sub_title} ({len(sub_items)} màn hình)\n')
                md.append(f'- **Tính năng chính & Spec:** {spec}')
                md.append(f'- **Trọng tâm Test / Verify Bug:** {verify}')
                md.append(f'- **Liên kết chéo:** {cross}\n')
                md.append('| Mã ID | Tên màn hình (EN) | Tên màn hình (JP) | Loại | Trạng thái (Spec / BE / FE / Test) | Tài liệu / Link |')
                md.append('| :--- | :--- | :--- | :---: | :--- | :--- |')

                for it in sub_items:
                    stt = str(it.get('stt', '')).strip()
                    sid = str(it.get('id', '')).strip() or '-'
                    name_en = str(it.get('name_en', '')).strip().replace('\n', ' ').replace('|', '/')
                    raw_jp = str(it.get('name_jp', '')).strip().replace('\n', ' ').replace('|', '/')
                    orig_grp = str(it.get('orig_grp', '')).strip() or grp
                    note = str(it.get('note', '')).strip().replace('\n', ' ').replace('|', '/')

                    link_parts = []
                    if raw_jp.startswith('http'):
                        link_parts.append(f'[Link]({raw_jp})')
                        name_jp = '-'
                    else:
                        name_jp = raw_jp or '-'

                    if note and note != '-':
                        if note.startswith('http'):
                            link_parts.append(f'[Spec]({note})')
                        else:
                            link_parts.append(note)

                    ov_info = ov_map.get((stt, sid, str(it.get('name_en', '')).strip()), {})
                    status_str = '-'
                    if ov_info:
                        s_spec = ov_info.get('spec') or '-'
                        s_be = ov_info.get('be') or '-'
                        s_fe = ov_info.get('fe') or '-'
                        s_test = ov_info.get('test') or '-'
                        status_str = f'{s_spec} / {s_be} / {s_fe} / {s_test}'
                        if ov_info.get('close'):
                            status_str += f" ({ov_info['close']})"

                    art_tags = sorted(local_artifacts.get(sid.upper(), set()))
                    if art_tags:
                        link_parts.append('Local: `' + ', '.join(art_tags) + '`')

                    doc_col = ' · '.join(link_parts) if link_parts else '-'
                    md.append(f'| `{sid}` | {name_en} | {name_jp} | {orig_grp} | {status_str} | {doc_col} |')
                    quick_index.append((sid, grp, sub_title, name_en))
                md.append('\n')

    md.append('\n---\n## V. CHỈ MỤC TRA CỨU NHANH THEO MÃ MÀN HÌNH (QUICK ID INDEX)\n')
    md.append('> Dùng `Ctrl+F` hoặc AI grep theo mã màn hình để định vị ngay cụm tính năng chi tiết.\n')
    md.append('| Mã ID | Nhóm | Cụm tính năng chi tiết | Tên màn hình (EN) |')
    md.append('| :--- | :---: | :--- | :--- |')
    for sid, grp, sub_title, name_en in sorted(quick_index, key=lambda x: (x[0], x[1], x[3])):
        md.append(f'| `{sid}` | {grp} | {sub_title} | {name_en} |')

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f'Synced {OUT_PATH}: {total_all_screens} screens, {total_sub} sub-clusters.')
    if new_screens:
        print(f'New screens detected ({len(new_screens)}):')
        for g, m, s, n in new_screens:
            print(f'  + [{g}] {m} -> {s}: {n}')
    else:
        print('No new unclassified screens compared to baseline.')


if __name__ == '__main__':
    main()
