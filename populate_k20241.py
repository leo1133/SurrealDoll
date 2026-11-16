# -*- coding: utf-8 -*-
import json
import os
import re
import subprocess

SPREADSHEET_ID = "1j1CtnETyAwex7lqzvuA9yzJhpDDNB2pHQ5sVRlztLNM"
SHEET_ID = 354670491
SHEET_NAME = "K20241(Mobile)"
GSHEETS_CMD = "/home/nga/.gemini/config/plugins/gsheets/skills/gsheets/scripts/gsheets"

env = os.environ.copy()
env['PATH'] = env.get('PATH', '') + ':/home/nga/.gemini/config/plugins/gsheets/skills/gsheets/scripts'
env['AGY_ACCOUNT'] = 'ngadtp@mumesoft.vn'

# 1. Parse testcases from markdown file
md_path = "testcase_ui/K20241_testcase.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_lines = f.readlines()

testcases = []
for l in md_lines:
    if l.startswith("| `[K20241-"):
        parts = [p.strip() for p in l.split("|")[1:-1]]
        testcases.append({
            "id": parts[0].replace("`", ""),
            "title": parts[1],
            "big_item": parts[2],
            "steps": parts[3].replace("<br>", "\n"),
            "pre": parts[4],
            "expected": parts[5].replace("<br>", "\n"),
            "priority": parts[6].replace("*", "")
        })

print(f"Loaded {len(testcases)} testcases from {md_path}")

total = len(testcases)
end_row = 7 + total

# 2. Build header data
header_data = [
    ['Module Code', 'K20241', 'Env', 'Mobile', '', '', '', 'Round 1 - IOS', '', '', '', '', 'Round 2 - Android', '', '', '', ''],
    ['Total of Test cases Created', f'=COUNTA(A8:A{end_row})', '% Executed', f'=IF(L3 > 0,L3/B2,0)', '', '', '', 'Pass', 'Fail', 'Impact', 'Not Run', 'Total', 'Pass', 'Fail', 'Impact', 'Not Run', 'Total'],
    ['Total of Test cases plan to Executed', '=B2', 'Creator', 'NgaDTP', 'Spec: 1-Surreal SPEC', '', '', f'=COUNTIF(H8:H{end_row}, "Pass")', f'=COUNTIF(H8:H{end_row}, "Fail")', f'=COUNTIF(H8:H{end_row}, "Impact")', f'=COUNTIFS(A8:A{end_row}, "<>", H8:H{end_row}, "")', '=SUM(H3:K3)', f'=COUNTIF(M8:M{end_row}, "Pass")', f'=COUNTIF(M8:M{end_row}, "Fail")', f'=COUNTIF(M8:M{end_row}, "Impact")', f'=COUNTIFS(A8:A{end_row}, "<>", M8:M{end_row}, "Not run")', '=SUM(M3:P3)'],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['ID', 'Title', 'Big item', 'Steps', 'Pre-condition', 'Expected', 'Priority', 'Round 1 - IOS', '', '', '', '', 'Round 2 - Android', '', '', '', ''],
    ['', '', '', '', '', '', '', 'Result', 'Bug ID', 'Tester', 'Test Date', 'Note', 'Result', 'Bug ID', 'Tester', 'Test Date', 'Note'],
    ['UI & Functional', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
]

rows_data = []
for idx, tc in enumerate(testcases, start=8):
    formula = f'=IF(OR(D{idx}<>"",F{idx}<>""),"["&TEXT($B$1,"##")&"-"&TEXT(ROW()-7-COUNTBLANK($F$8:F{idx}),"##")&"]","")'
    row = [
        formula,
        tc['title'],
        tc['big_item'],
        tc['steps'],
        tc['pre'],
        tc['expected'],
        tc['priority'],
        '', '', '', '', '', '', '', '', '', ''
    ]
    rows_data.append(row)

all_data = header_data + rows_data

batch_requests = [
    {"op": "clear", "range": f"'{SHEET_NAME}'!A1:Q{end_row + 20}"},
    {"op": "write", "range": f"'{SHEET_NAME}'!A1:Q{len(all_data)}", "data": all_data}
]

with open("batch_write_k20241.json", "w", encoding="utf-8") as f:
    json.dump(batch_requests, f, ensure_ascii=False, indent=2)

print(f"Executing batch write {len(all_data)} rows to {SHEET_NAME}...")
res = subprocess.run([GSHEETS_CMD, "mutate", "batch", SPREADSHEET_ID, "-f", "batch_write_k20241.json"], capture_output=True, text=True, env=env)
print("Write Return code:", res.returncode)
print("Write Stdout:", res.stdout)
if res.stderr:
    print("Write Stderr:", res.stderr)

# 3. Calculate Merges
raw_requests = []

# Header merges
# H1:L1 (cols 7 to 12)
raw_requests.append({
    "mergeCells": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 7, "endColumnIndex": 12},
        "mergeType": "MERGE_ALL"
    }
})
# M1:Q1 (cols 12 to 17)
raw_requests.append({
    "mergeCells": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 12, "endColumnIndex": 17},
        "mergeType": "MERGE_ALL"
    }
})
# H5:L5 (cols 7 to 12)
raw_requests.append({
    "mergeCells": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 5, "startColumnIndex": 7, "endColumnIndex": 12},
        "mergeType": "MERGE_ALL"
    }
})
# M5:Q5 (cols 12 to 17)
raw_requests.append({
    "mergeCells": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 5, "startColumnIndex": 12, "endColumnIndex": 17},
        "mergeType": "MERGE_ALL"
    }
})
# Vertical merges for A5:A6 to G5:G6 (cols 0 to 7)
for c in range(7):
    raw_requests.append({
        "mergeCells": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 6, "startColumnIndex": c, "endColumnIndex": c + 1},
            "mergeType": "MERGE_ALL"
        }
    })

# Merge row 7 (UI & Functional): A7:Q7
raw_requests.append({
    "mergeCells": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 6, "endRowIndex": 7, "startColumnIndex": 0, "endColumnIndex": 17},
        "mergeType": "MERGE_ALL"
    }
})

# Body merges: Title (col 1 to 2)
start_row = 8
current_title = None
title_start = None
for idx, tc in enumerate(testcases):
    row_idx = (start_row + idx) - 1
    title = tc['title']
    if title != current_title:
        if current_title is not None and (row_idx - title_start) > 1:
            raw_requests.append({
                "mergeCells": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": title_start, "endRowIndex": row_idx, "startColumnIndex": 1, "endColumnIndex": 2},
                    "mergeType": "MERGE_ALL"
                }
            })
        current_title = title
        title_start = row_idx
if current_title is not None and (end_row - title_start) > 1:
    raw_requests.append({
        "mergeCells": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": title_start, "endRowIndex": end_row, "startColumnIndex": 1, "endColumnIndex": 2},
            "mergeType": "MERGE_ALL"
        }
    })

# Body merges: Big item (col 2 to 3)
current_key = None
item_start = None
for idx, tc in enumerate(testcases):
    row_idx = (start_row + idx) - 1
    key = (tc['title'], tc['big_item'])
    if key != current_key:
        if current_key is not None and (row_idx - item_start) > 1:
            raw_requests.append({
                "mergeCells": {
                    "range": {"sheetId": SHEET_ID, "startRowIndex": item_start, "endRowIndex": row_idx, "startColumnIndex": 2, "endColumnIndex": 3},
                    "mergeType": "MERGE_ALL"
                }
            })
        current_key = key
        item_start = row_idx
if current_key is not None and (end_row - item_start) > 1:
    raw_requests.append({
        "mergeCells": {
            "range": {"sheetId": SHEET_ID, "startRowIndex": item_start, "endRowIndex": end_row, "startColumnIndex": 2, "endColumnIndex": 3},
            "mergeType": "MERGE_ALL"
        }
    })

# 4. Add formatting requests (Styles & Borders)
# Common borders
solid_border = {
    "style": "SOLID",
    "width": 1,
    "color": {"red": 0.8, "green": 0.8, "blue": 0.8}
}

# Base font & alignment for whole data range A1:Q77
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": end_row, "startColumnIndex": 0, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "textFormat": {"fontFamily": "Times New Roman", "fontSize": 11},
                "borders": {"top": solid_border, "bottom": solid_border, "left": solid_border, "right": solid_border}
            }
        },
        "fields": "userEnteredFormat.textFormat,userEnteredFormat.borders"
    }
})

# Body test cases wrap and vertical alignment
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 7, "endRowIndex": end_row, "startColumnIndex": 0, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "wrapStrategy": "WRAP",
                "verticalAlignment": "TOP"
            }
        },
        "fields": "userEnteredFormat.wrapStrategy,userEnteredFormat.verticalAlignment"
    }
})

# Alignment for Col A (ID) and Col G (Priority)
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 7, "endRowIndex": end_row, "startColumnIndex": 0, "endColumnIndex": 1},
        "cell": {
            "userEnteredFormat": {
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 7, "endRowIndex": end_row, "startColumnIndex": 6, "endColumnIndex": 7},
        "cell": {
            "userEnteredFormat": {
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})

# Title (Col B) and Big item (Col C) vertical alignment middle
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 7, "endRowIndex": end_row, "startColumnIndex": 1, "endColumnIndex": 3},
        "cell": {
            "userEnteredFormat": {
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.verticalAlignment"
    }
})

# Color styles:
# Header Orange/Tan: {'red': 0.42745098, 'green': 0.61960787, 'blue': 0.92156863} -> wait, red, green, blue in inspect-cell:
# red=0.427, green=0.620, blue=0.922 is #6D9EEB (light blue) or tan? Let's use exact rgb from inspect-cell
color_tan = {"red": 0.42745098, "green": 0.61960787, "blue": 0.92156863}
color_green = {"red": 0.35686275, "green": 0.7882353, "blue": 0.36862746}
color_blue = {"red": 0.96862745, "green": 0.7921569, "blue": 0.6745098}
color_grey = {"red": 0.78431374, "green": 0.78431374, "blue": 0.78431374}
color_peach = {"red": 0.7882353, "green": 0.85490197, "blue": 0.972549}

# Row 1 headers (A1:D1 tan, H1:L1 green, M1:Q1 blue)
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 0, "endColumnIndex": 4},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_tan,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 7, "endColumnIndex": 12},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_green,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 0, "endRowIndex": 1, "startColumnIndex": 12, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_blue,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})

# Row 2 & 3 stats headers (H2:Q2 grey)
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 7, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_grey,
                "textFormat": {"fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 2, "endRowIndex": 3, "startColumnIndex": 7, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})

# Rows 5-6 Table Headers (A5:G6 tan, H5:L6 green, M5:Q6 blue)
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 6, "startColumnIndex": 0, "endColumnIndex": 7},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_tan,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 6, "startColumnIndex": 7, "endColumnIndex": 12},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_green,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 4, "endRowIndex": 6, "startColumnIndex": 12, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_blue,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "horizontalAlignment": "CENTER",
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment,userEnteredFormat.verticalAlignment"
    }
})

# Row 7 UI & Functional (peach)
raw_requests.append({
    "repeatCell": {
        "range": {"sheetId": SHEET_ID, "startRowIndex": 6, "endRowIndex": 7, "startColumnIndex": 0, "endColumnIndex": 17},
        "cell": {
            "userEnteredFormat": {
                "backgroundColor": color_peach,
                "textFormat": {"bold": True, "fontFamily": "Times New Roman", "fontSize": 11},
                "verticalAlignment": "MIDDLE"
            }
        },
        "fields": "userEnteredFormat.backgroundColor,userEnteredFormat.textFormat,userEnteredFormat.verticalAlignment"
    }
})

with open("raw_batch_merges_k20241.json", "w", encoding="utf-8") as f:
    json.dump({"requests": raw_requests}, f, ensure_ascii=False, indent=2)

print(f"Executing {len(raw_requests)} raw-batch formatting and merge requests...")
res_m = subprocess.run([GSHEETS_CMD, "mutate", "raw-batch", SPREADSHEET_ID, "-f", "raw_batch_merges_k20241.json"], capture_output=True, text=True, env=env)
print("Merges Return code:", res_m.returncode)
print("Merges Stdout:", res_m.stdout)
if res_m.stderr:
    print("Merges Stderr:", res_m.stderr)

# 5. Freeze rows 1-6
subprocess.run([GSHEETS_CMD, "mutate", "freeze", SPREADSHEET_ID, "--sheet-id", str(SHEET_ID), "--rows", "6"], env=env)

# 6. Set column widths
col_widths = {
    0: 100,  # ID
    1: 220,  # Title
    2: 240,  # Big item
    3: 380,  # Steps
    4: 200,  # Pre-condition
    5: 380,  # Expected
    6: 90,   # Priority
    7: 100,  # R1 Result
    8: 100,  # R1 Bug ID
    9: 100,  # R1 Tester
    10: 100, # R1 Test Date
    11: 150, # R1 Note
    12: 100, # R2 Result
    13: 100, # R2 Bug ID
    14: 100, # R2 Tester
    15: 100, # R2 Test Date
    16: 150, # R2 Note
}

for col_idx, width in col_widths.items():
    subprocess.run([
        GSHEETS_CMD, "mutate", "set-col-width", SPREADSHEET_ID,
        "--sheet-id", str(SHEET_ID),
        "--start-col", str(col_idx),
        "--end-col", str(col_idx + 1),
        "--pixels", str(width)
    ], env=env)

print("K20241(Mobile) Google Sheets population finished successfully!")
