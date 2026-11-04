# Bộ Viewpoint Kiểm Thử API (API Testing Viewpoint Catalog v1)

> Tài liệu này được chuyển đổi đầy đủ từ file **`API_Viewpoint_v1.xlsx`**, bao gồm toàn bộ **4 sheet**: Hướng dẫn sử dụng (`How to use`), Chú giải & Giả định (`Legend & Assumptions`), Thống kê tổng hợp (`Summary`), và Danh mục chi tiết **419 Viewpoints** (`Viewpoint`) chia theo 33 nhóm.

## Mục lục
- [1. Hướng dẫn sử dụng bộ Viewpoint API (How to use)](#1-hướng-dẫn-sử-dụng-bộ-viewpoint-api-how-to-use)
- [2. Placeholders, Điều kiện & Giả định (Legend & Assumptions)](#2-placeholders-điều-kiện--giả-định-legend--assumptions)
- [3. Bảng tổng hợp số liệu (Summary)](#3-bảng-tổng-hợp-số-liệu-summary)
- [4. Danh mục chi tiết 419 Viewpoints (Viewpoint)](#4-danh-mục-chi-tiết-419-viewpoints-viewpoint)

---

## 1. Hướng dẫn sử dụng bộ Viewpoint API (How to use)

### 1.1. Cách áp dụng cho một API mới

| Bước | Nội dung thực hiện |
| :--- | :--- |
| **Bước 1** | Liệt kê từng field / param của API: vị trí (Query, Path, JSON body, Form-data, Header), kiểu dữ liệu, bắt buộc hay không, có unique, min/max, danh sách giá trị (enum). |
| **Bước 2** | Mở sheet 'Viewpoint', bật bộ lọc: Group (hoặc 'Target / field type') + cột vị trí có dấu ✓ + cột 'Applies when'. |
| **Bước 3** | Mỗi viewpoint sau khi lọc = 1 test case. Test Item = cột 'Viewpoint'; Request = cột 'Test data'; Expected = cột 'Expected result'. |
| **Bước 4** | Thay placeholder {field}, {valid}, {max}… bằng giá trị thật của API (xem sheet 'Legend & Assumptions'). |
| **Bước 5** | Cột 'Alternative / note' ghi các hành vi có thể khác nhau giữa hệ thống: đối chiếu với spec rồi chốt một đáp án cho test case. |
| **Bước 6** | Cột 'Assumption' (A1–A14) trỏ tới giả định mặc định. Nếu API của bạn khác, sửa Expected của các viewpoint có cùng mã A đó. |

### 1.2. Field thuộc kiểu nào thì lọc nhóm nào

| Loại field / thành phần | Group cần lọc | Ghi chú |
| :--- | :--- | :--- |
| Mọi query param / form key | **Key / parameter name; Required / optional / empty** | Áp dụng cho từng key |
| Text, tên, mô tả, ô tìm kiếm | **String / text** | Search field có thêm nhóm viewpoint riêng |
| Số nguyên, số lượng, id | **Integer (+ Path parameter nếu nằm trên URL)** | Cần min / max từ spec |
| Tiền, số thập phân | **Decimal / money (+ Integer)** |  |
| Checkbox, flag | **Boolean** |  |
| Ngày, giờ | **Date / datetime; Date range (cặp from_date / to_date)** |  |
| Email | **Email (+ String)** |  |
| Dropdown, trạng thái | **Enum / droplist** |  |
| Danh sách, tag | **Array / list** |  |
| Phân trang, sắp xếp | **Pagination - limit / offset / combination; Sorting** | Chỉ cho API dạng list |
| File upload | **File upload; Body - form-data** |  |
| Header | **Header - general / Accept / Content-Type / Authorization / X-CSRFToken** | Áp dụng cho mọi API |
| Body JSON | **Body - JSON structure + nhóm theo từng kiểu field** |  |
| Login | **Login / authentication** | Chỉ cho API đăng nhập |
| Create / Update / Delete | **CRUD - Create / Update / Delete** | Theo method của API |
| Mọi API | **HTTP method & status; Authorization & permission; Response validation; Security; Non-functional** | Chọn theo mức độ rủi ro |

### 1.3. Đối chiếu với bộ 512 test case cũ

| Module trong file test case | Group viewpoint tương ứng | Cột 'Source' |
| :--- | :--- | :--- |
| 01–02 Status, HTTP Method | HTTP method & status | `01, 02` |
| 03–06 Header | Header – general / Accept / Content-Type / Authorization / X-CSRFToken | `03–06` |
| 07 Permission | Authorization & permission | `07` |
| 08–14 Query | Key; String; Enum; Integer; Pagination; Date range; Sorting | `08–14` |
| 15 Path param | Path parameter | `15` |
| 16–18 Form-data, File | Form-data; File upload; String; Boolean | `16–18` |
| 19–26 JSON | Body - JSON structure; String; Integer; Boolean; Date; Email; Enum; Array | `19–26` |
| 27 Login | Login / authentication | `27` |
| 28–30 CRUD | CRUD - Create / Update / Delete | `28–30` |
| 31 Response | Response validation | `31` |
| 32 Security | Security | `32` |
| 33 Non-functional | Non-functional | `33` |

---

## 2. Placeholders, Điều kiện & Giả định (Legend & Assumptions)

### 2.1. Placeholders (Biến giữ chỗ)

| Placeholder | Ý nghĩa / Thay thế bằng (Replace with) |
| :--- | :--- |
| `{field}` | Name of the field / parameter being tested ({FIELD} = upper-case) |
| `{valid} / {valid2}` | A valid value / another valid value |
| `{min} / {max}` | Min / max length (string) or min / max value (integer) from the spec |
| `{max_items}` | Maximum number of array items |
| `{max_limit}` | Maximum allowed 'limit' |
| `{max_file_size}` | Maximum upload size |
| `{valid_id}` | Id of an existing record |
| `{today}` | Current date (YYYY-MM-DD) |
| `total` | Total number of records matching the current filter |

### 2.2. Conditions (Điều kiện áp dụng trong cột `Applies when`)

| Condition | Ý nghĩa – chỉ sử dụng viewpoint nếu field/API thỏa mãn |
| :--- | :--- |
| **Any field** | Always applicable to a field of this type |
| **Required field / Optional field** | Field is mandatory / not mandatory in the spec |
| **Unique field** | Value must be unique (business rule) |
| **Has max length / min length / min-max / scale / max items** | Spec defines such a limit |
| **Search field** | Param is a free-text search (q, keyword…) |
| **JSON** | Only when the field is sent in a JSON body |
| **Endpoint with body** | POST / PUT / PATCH endpoints |
| **Cookie-session auth** | Authentication uses cookies, so CSRF applies (N/A for pure Bearer/JWT) |
| **API supports sorting / Multi-select / Multi-file / Soft delete / Id is UUID** | Feature exists in the API |
| **Endpoint does not support method** | Method is not allowed on that endpoint (read-only endpoint) |

### 2.3. Default Assumptions (Giả định mặc định `A1` – `A14`)

| ID | Giả định mặc định dùng trong 'Expected result' | Nếu hệ thống hành xử khác (If the system behaves differently) |
| :---: | :--- | :--- |
| **`A1`** | Unknown / misspelled query param is IGNORED (200, default result) | Strict API → 400 |
| **`A2`** | Query keys and enum values are case-sensitive | Case-insensitive → 200 |
| **`A3`** | Duplicate key → LAST value used | First value, or 400 (be consistent) |
| **`A4`** | limit &gt; max → 400 | API caps to max → 200 |
| **`A5`** | Date format YYYY-MM-DD, inclusive range, one-sided range allowed, from &gt; to → 400 | Change per spec |
| **`A6`** | Invalid id format → 400; valid format but not found → 404 | Router returns 404 for all |
| **`A7`** | Wrong / missing Content-Type on body endpoints → 415 | 400 |
| **`A8`** | Invalid file extension → 415; file too large → 413 | Both 400 |
| **`A9`** | GET ignores Content-Type / X-CSRFToken; missing Accept → JSON; CSRF enforced (403) on unsafe methods only with cookie-session auth | Pure JWT API → CSRF viewpoints N/A |
| **`A10`** | Unknown fields in body are ignored | Strict API → 400 |
| **`A11`** | PATCH with empty body → 400 | 200 no change |
| **`A13`** | Error body format: {code, message, errors:[{field, message}]} | Use the project's real format |
| **`A14`** | Rate limit → 429 + Retry-After | No rate limit → N/A |

---

## 3. Bảng tổng hợp số liệu (Summary)

### 3.1. Thống kê theo Nhóm (Group) và Mức độ ưu tiên (Priority)

| STT | Group | Total | High | Medium | Low |
| :---: | :--- | :---: | :---: | :---: | :---: |
| 1 | **Key / parameter name** | **7** | 2 | 4 | 1 |
| 2 | **Required / optional / empty** | **11** | 7 | 4 | 0 |
| 3 | **String / text** | **25** | 12 | 10 | 3 |
| 4 | **Integer** | **19** | 11 | 5 | 3 |
| 5 | **Decimal / money** | **3** | 2 | 1 | 0 |
| 6 | **Boolean** | **10** | 4 | 5 | 1 |
| 7 | **Date / datetime** | **17** | 6 | 7 | 4 |
| 8 | **Date range** | **17** | 12 | 5 | 0 |
| 9 | **Email** | **15** | 6 | 6 | 3 |
| 10 | **Enum / droplist** | **12** | 5 | 6 | 1 |
| 11 | **Array / list** | **12** | 5 | 6 | 1 |
| 12 | **Pagination - limit** | **16** | 10 | 5 | 1 |
| 13 | **Pagination - offset** | **13** | 9 | 4 | 0 |
| 14 | **Pagination - combination** | **10** | 6 | 3 | 1 |
| 15 | **Sorting** | **10** | 1 | 6 | 3 |
| 16 | **Path parameter** | **15** | 7 | 5 | 3 |
| 17 | **Header - general** | **2** | 1 | 0 | 1 |
| 18 | **Header - Accept** | **7** | 2 | 4 | 1 |
| 19 | **Header - Content-Type** | **9** | 6 | 2 | 1 |
| 20 | **Header - Authorization** | **16** | 12 | 3 | 1 |
| 21 | **Header - X-CSRFToken** | **7** | 5 | 1 | 1 |
| 22 | **HTTP method & status** | **12** | 6 | 3 | 3 |
| 23 | **Authorization & permission** | **8** | 8 | 0 | 0 |
| 24 | **Body - JSON structure** | **15** | 6 | 4 | 5 |
| 25 | **Body - form-data** | **5** | 4 | 0 | 1 |
| 26 | **File upload** | **24** | 12 | 10 | 2 |
| 27 | **Login / authentication** | **26** | 15 | 8 | 3 |
| 28 | **CRUD - Create** | **8** | 5 | 3 | 0 |
| 29 | **CRUD - Update** | **14** | 6 | 6 | 2 |
| 30 | **CRUD - Delete** | **8** | 5 | 3 | 0 |
| 31 | **Response validation** | **19** | 11 | 5 | 3 |
| 32 | **Security** | **18** | 11 | 4 | 3 |
| 33 | **Non-functional** | **9** | 0 | 5 | 4 |
| | **TOTAL** | **419** | **220** | **143** | **56** |

### 3.2. Thống kê theo Vị trí áp dụng (By Location)
*(Một viewpoint có thể áp dụng cho nhiều vị trí)*

| Location | Số lượng Viewpoints |
| :--- | :---: |
| **Query** | 188 |
| **Path** | 42 |
| **JSON body** | 222 |
| **Form-data** | 166 |
| **Header** | 59 |

### 3.3. Thống kê theo Loại kiểm thử (By Test Type)

| Test Type | Số lượng Viewpoints |
| :--- | :---: |
| **Positive** | 84 |
| **Negative** | 167 |
| **Boundary** | 108 |
| **Security** | 51 |
| **Performance** | 9 |

---

## 4. Danh mục chi tiết 419 Viewpoints (Viewpoint)

### 4.1. Key / parameter name (7 viewpoints)
* **Target / field type:** `Any query or form-data key`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **KEY-001** | ✓ |  |  | ✓ |  | Any field | Key has empty name | ?={valid}   \|   form part with empty name | 400 Bad Request + error body (A13) (or 422) |  | High | Negative |  | 08-11,16-18 |
| **KEY-002** | ✓ |  |  | ✓ |  | Optional field | Misspelled / unknown key | ?{field}x={valid} | 200 OK. Unknown param ignored, default result (A1) | Required field: 400 (field missing) | Medium | Negative | A1 | 08-11,16-18 |
| **KEY-003** | ✓ |  |  | ✓ |  | Required field | Misspelled key on a REQUIRED field | ?{field}x={valid}  (required field not sent) | 400 Bad Request + error body (A13). Error points to the missing field |  | High | Negative |  | 08-11,16-18 |
| **KEY-004** | ✓ |  |  | ✓ |  | Optional field | Key contains spaces | ?{field}%20x={valid} | 200 OK. Unknown param ignored, default result (A1) | Required field: 400 | Medium | Negative | A1 | 08-11,16-18 |
| **KEY-005** | ✓ |  |  | ✓ |  | Optional field | Key contains special characters | ?{field}@%23={valid} | 200 OK. Unknown param ignored, default result (A1) | Required field: 400 | Medium | Negative | A1 | 08-11,16-18 |
| **KEY-006** | ✓ |  |  | ✓ |  | Optional field | Key in wrong letter case | ?{FIELD}={valid}  (upper-case) | 200 OK. Unknown param ignored, default result (A1). Keys are case-sensitive |  | Low | Negative | A1, A2 | 08-11,16-18 |
| **KEY-007** | ✓ |  |  | ✓ |  | Any field | Duplicate key | ?{field}={valid}&{field}={valid2} | 200/201. Last value is used. Never 500 |  | Medium | Negative | A3 | 08-11,16-18 |

### 4.2. Required / optional / empty (11 viewpoints)
* **Target / field type:** `Any field`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **REQ-001** | ✓ |  | ✓ | ✓ |  | Required field | Required field is missing | Do not send {field} | 400 Bad Request + error body (A13). Error points to field {field} |  | High | Negative |  | 19-26,17-18 |
| **REQ-002** | ✓ |  | ✓ | ✓ |  | Optional field | Optional field is missing | Do not send {field} | Success; default value applied |  | High | Positive |  | 19-26,17-18 |
| **REQ-003** | ✓ |  | ✓ | ✓ |  | Required field | Value = null | JSON: {field}: null   \|   Query/form: {field}=null (text) | 400 Bad Request + error body (A13) | Query/form: 'null' is treated as plain text. Optional JSON field: default applied or 400 per spec | High | Negative |  | 19-26,17-18 |
| **REQ-004** | ✓ |  | ✓ | ✓ |  | Optional field | Value = null (optional) | JSON: {field}: null | Default applied, or 400 (decide per spec and keep consistent) |  | Medium | Negative |  | 19-26,17-18 |
| **REQ-005** | ✓ |  | ✓ | ✓ |  | Required field | Value is empty | {field}="" | 400 Bad Request + error body (A13) | Optional: default list / default value (200/201) | High | Negative |  | 19-26,17-18 |
| **REQ-006** | ✓ |  | ✓ | ✓ |  | Optional field | Value is empty (optional) | {field}="" | Default value applied (200/201) |  | Medium | Boundary |  | 19-26,17-18 |
| **REQ-007** | ✓ |  | ✓ | ✓ |  | Any field | Value is whitespace only | {field}="   " | 400 Bad Request + error body (A13) (treated as empty) |  | Medium | Boundary |  | 19-26,17-18 |
| **REQ-008** | ✓ |  | ✓ | ✓ |  | Body with 2+ required fields | Every required field missing one by one | One request per required field | 400 Bad Request + error body (A13) for each; error names the missing field |  | High | Negative |  | 19-26,17-18 |
| **REQ-009** | ✓ |  | ✓ | ✓ |  | Body with required fields | All fields missing | Body {} / no part / no query | 400 Bad Request + error body (A13). Lists every missing required field |  | High | Negative |  | 19-26,17-18 |
| **REQ-010** | ✓ |  | ✓ | ✓ |  | Body with required fields | All fields = null | Every field set to null | 400 Bad Request + error body (A13) |  | High | Negative |  | 19-26,17-18 |
| **REQ-011** | ✓ |  | ✓ | ✓ |  | Body JSON / form-data | Unknown extra field | Add a field that is not in the spec | Success. Unknown field ignored | Strict API: 400 | Medium | Boundary | A10 | 19-26,17-18 |

### 4.3. String / text (25 viewpoints)
* **Target / field type:** `String`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **STR-001** | ✓ |  | ✓ | ✓ |  | Any field | Valid letters | {field}=abc | Success. Value saved / returned exactly as sent |  | High | Positive |  | 08,17,20 |
| **STR-002** | ✓ |  | ✓ | ✓ |  | Any field | Numeric characters only | {field}=123 | Success. Treated as text '123' (search: records matching or empty list) |  | High | Positive |  | 08,17,20 |
| **STR-003** | ✓ |  | ✓ | ✓ |  | Any field | Special characters | {field}=@#\$%^&*()&lt;&gt;  (URL-encode in query) | Success. Stored/matched as literal text. Never 500 |  | High | Boundary |  | 08,17,20 |
| **STR-004** | ✓ |  | ✓ | ✓ |  | Any field | Spaces inside the value | {field}=red apple  (query: %20 and +) | Success. Matches 'red apple'. %20 and + give the same result |  | High | Positive |  | 08,17,20 |
| **STR-005** | ✓ |  | ✓ | ✓ |  | Any field | Leading / trailing spaces | {field}="  abc  " | Success. Value trimmed (same as 'abc'); never leaves hidden spaces |  | Medium | Boundary |  | 08,17,20 |
| **STR-006** | ✓ |  | ✓ | ✓ |  | Has min length | Min length | {field} = 1 character (or {min}) | Success |  | High | Boundary |  | 08,17,20 |
| **STR-007** | ✓ |  | ✓ | ✓ |  | Has min length (min &gt; 1) | Below min length | {field} = {min}-1 characters | 400 Bad Request + error body (A13) |  | High | Boundary |  | 08,17,20 |
| **STR-008** | ✓ |  | ✓ | ✓ |  | Has max length | Max length | {field} = {max} characters | Success |  | High | Boundary |  | 08,17,20 |
| **STR-009** | ✓ |  | ✓ | ✓ |  | Has max length | Max length + 1 | {field} = {max}+1 characters | 400 Bad Request + error body (A13) |  | High | Boundary |  | 08,17,20 |
| **STR-010** | ✓ |  | ✓ | ✓ |  | Any field | Vietnamese with accents | {field}=Nguyễn Văn Hồng | Success. UTF-8 saved and returned correctly |  | Medium | Positive |  | 08,17,20 |
| **STR-011** | ✓ |  | ✓ | ✓ |  | Search field | Accent-insensitive search | {field}=Nguyen Van Hong (no accents) | Matches accented value if supported, else empty list |  | Low | Positive |  | 08,17,20 |
| **STR-012** | ✓ |  | ✓ | ✓ |  | Any field | Emoji / 4-byte characters | {field}=😀 | Success or 400. Never 500 |  | Low | Boundary |  | 08,17,20 |
| **STR-013** | ✓ |  | ✓ | ✓ |  | Any field | Letter case | {field}=ABC vs abc | Store: case preserved. Search: same result for any case (if case-insensitive) |  | Medium | Positive |  | 08,17,20 |
| **STR-014** | ✓ |  | ✓ | ✓ |  | JSON | Wrong data type (number) | JSON {field}: 123 | 400 Bad Request + error body (A13) (strict) or accepted as '123' (per spec) |  | Medium | Negative |  | 08,17,20 |
| **STR-015** | ✓ |  | ✓ | ✓ |  | JSON | Wrong data type (boolean / array / object) | JSON {field}: true / ["a"] / {} | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 08,17,20 |
| **STR-016** | ✓ |  | ✓ | ✓ |  | Any field | Control characters / newline / NUL | {field}="a\nb\u0000c" | 400, or accepted with control chars removed. Never 500 |  | Low | Security |  | 08,17,20 |
| **STR-017** | ✓ |  | ✓ | ✓ |  | Any field | HTML / script content | {field}=&lt;script&gt;alert(1)&lt;/script&gt; | Stored escaped (or 400). Never executed when displayed |  | High | Security |  | 08,17,20 |
| **STR-018** | ✓ |  | ✓ | ✓ |  | Unique field | Value must be unique – duplicate | Create twice with same {field} | 409 Conflict + error body (A13) |  | High | Negative |  | 08,17,20 |
| **STR-019** | ✓ |  | ✓ | ✓ |  | Search field | Wildcard characters % and _ | {field}=%25 / {field}=_ | Treated as literal text, not SQL wildcard |  | Medium | Security |  | 08,17,20 |
| **STR-020** | ✓ |  | ✓ | ✓ |  | Search field | Search – no match | {field}=zzzzzzzz | 200 OK. Empty list (results=[], total=0). Not null, not 404 |  | High | Boundary |  | 08,17,20 |
| **STR-021** | ✓ |  | ✓ | ✓ |  | Search field | Search – partial match | {field}=ab (part of 'abc') | 200 OK. Records containing 'ab' |  | Medium | Positive |  | 08,17,20 |
| **STR-022** | ✓ |  | ✓ | ✓ |  | Search field | Search – missing / empty | Do not send {field} / {field}= | 200 OK. Default list |  | Medium | Boundary |  | 08,17,20 |
| **STR-023** | ✓ |  | ✓ | ✓ |  | Search field | Search – literal 'null' | {field}=null | 200 OK. Treated as text 'null' |  | Medium | Negative |  | 08,17,20 |
| **STR-024** | ✓ |  | ✓ | ✓ |  | Search field | Search – whitespace only | {field}=%20%20%20 | 200 OK. Default list (treated as empty) |  | Medium | Boundary |  | 08,17,20 |
| **STR-025** | ✓ |  | ✓ | ✓ |  | Search field | Search – numeric text | {field}=123 | 200 OK. Matching records or empty list |  | High | Positive |  | 08,17,20 |

### 4.4. Integer (19 viewpoints)
* **Target / field type:** `Integer`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **INT-001** | ✓ | ✓ | ✓ | ✓ |  | Any field | Valid value | {field}={valid} | Success: 200 (read) / 201 (create) |  | High | Positive |  | 10,11,15,21 |
| **INT-002** | ✓ | ✓ | ✓ | ✓ |  | Has min / max | Min value | {field}={min} | Success |  | High | Boundary |  | 10,11,15,21 |
| **INT-003** | ✓ | ✓ | ✓ | ✓ |  | Has min / max | Min value - 1 | {field}={min}-1 | 400 Bad Request + error body (A13) |  | High | Boundary |  | 10,11,15,21 |
| **INT-004** | ✓ | ✓ | ✓ | ✓ |  | Has min / max | Max value | {field}={max} | Success |  | High | Boundary |  | 10,11,15,21 |
| **INT-005** | ✓ | ✓ | ✓ | ✓ |  | Has min / max | Max value + 1 | {field}={max}+1 | 400 Bad Request + error body (A13) (or capped to max if spec says so) |  | High | Boundary | A4 | 10,11,15,21 |
| **INT-006** | ✓ | ✓ | ✓ | ✓ |  | Any field | Zero | {field}=0 | Valid or 400 depending on min (usually 400 when min = 1) |  | High | Boundary |  | 10,11,15,21 |
| **INT-007** | ✓ | ✓ | ✓ | ✓ |  | Value must be &gt;= 0 | Negative | {field}=-1 | 400 Bad Request + error body (A13) |  | High | Boundary |  | 10,11,15,21 |
| **INT-008** | ✓ | ✓ | ✓ | ✓ |  | Any field | Decimal | {field}=1.5 | 400 Bad Request + error body (A13) |  | High | Negative |  | 10,11,15,21 |
| **INT-009** | ✓ | ✓ | ✓ | ✓ |  | Any field | Text | {field}=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 10,11,15,21 |
| **INT-010** | ✓ | ✓ | ✓ | ✓ |  | JSON | Numeric string (JSON) | JSON {field}: "10" | 400 Bad Request + error body (A13) (strict) or coerced to 10 (per spec) |  | Medium | Negative |  | 10,11,15,21 |
| **INT-011** | ✓ | ✓ | ✓ | ✓ |  | JSON | Boolean (JSON) | JSON {field}: true | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 10,11,15,21 |
| **INT-012** | ✓ | ✓ | ✓ | ✓ |  | Any field | Overflow 32-bit | {field}=2147483648 | 400 Bad Request + error body (A13). Never 500 |  | High | Boundary |  | 10,11,15,21 |
| **INT-013** | ✓ | ✓ | ✓ | ✓ |  | Any field | Extremely large | {field}=99999999999999999999 / 1e308 | 400 Bad Request + error body (A13). Never 500 |  | Medium | Boundary |  | 10,11,15,21 |
| **INT-014** | ✓ | ✓ | ✓ | ✓ |  | Required field | Empty string | {field}="" | 400 Bad Request + error body (A13) | Optional: default value | High | Negative |  | 10,11,15,21 |
| **INT-015** | ✓ | ✓ | ✓ | ✓ |  | Any field | Special characters | {field}=@# | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 10,11,15,21 |
| **INT-016** | ✓ | ✓ | ✓ | ✓ |  | Any field | Spaces around value | {field}=%205 | Trimmed (OK) or 400 – consistent across all numeric fields |  | Low | Boundary |  | 10,11,15,21 |
| **INT-017** | ✓ | ✓ | ✓ | ✓ |  | Any field | Leading zeros | {field}=005 | Same as 5 (OK) |  | Low | Boundary |  | 10,11,15,21 |
| **INT-018** | ✓ | ✓ | ✓ | ✓ |  | JSON | Scientific notation | JSON {field}: 1e2 | 400 or accepted as 100 – consistent |  | Low | Boundary |  | 10,11,15,21 |
| **INT-019** | ✓ | ✓ | ✓ | ✓ |  | Any field | Value = null | {field}=null | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 10,11,15,21 |

### 4.5. Decimal / money (3 viewpoints)
* **Target / field type:** `Decimal`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **NUM-001** | ✓ |  | ✓ | ✓ |  | Has scale (e.g. 2 decimals) | Max decimal places | {field}=1.23 (allowed scale) | Success. Value stored exactly |  | High | Boundary |  | New (not in original 512) |
| **NUM-002** | ✓ |  | ✓ | ✓ |  | Has scale | More decimal places than allowed | {field}=1.234 | 400 Bad Request + error body (A13) or rounded per spec (document which) |  | High | Boundary |  | New (not in original 512) |
| **NUM-003** | ✓ |  | ✓ | ✓ |  | Any field | Rounding / precision | {field}=0.1+0.2 style values, 9999999.99 | No floating-point error in stored/returned value |  | Medium | Boundary |  | New (not in original 512) |

### 4.6. Boolean (10 viewpoints)
* **Target / field type:** `Boolean`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **BOOL-001** | ✓ |  | ✓ | ✓ |  | Any field | true | {field}=true | Success. Saved as true |  | High | Positive |  | 18,22 |
| **BOOL-002** | ✓ |  | ✓ | ✓ |  | Any field | false | {field}=false | Success. Saved as false |  | High | Positive |  | 18,22 |
| **BOOL-003** | ✓ |  | ✓ | ✓ |  | Optional field | Missing (default) | Do not send {field} | Success. Default value applied |  | Medium | Positive |  | 18,22 |
| **BOOL-004** | ✓ |  | ✓ | ✓ |  | Any field | null | {field}=null | 400 Bad Request + error body (A13) or default applied (per spec) |  | Medium | Negative |  | 18,22 |
| **BOOL-005** | ✓ |  | ✓ | ✓ |  | Any field | Empty | {field}="" | Default value, or 400 (per spec) |  | Medium | Boundary |  | 18,22 |
| **BOOL-006** | ✓ |  | ✓ | ✓ |  | Any field | String 'true' / 'True' / 'FALSE' | JSON {field}: "true" | 400 Bad Request + error body (A13) (strict) or mapped (per spec) |  | Medium | Boundary |  | 18,22 |
| **BOOL-007** | ✓ |  | ✓ | ✓ |  | Any field | Number 1 / 0 | {field}=1 | 400 Bad Request + error body (A13) (strict) or mapped to true/false (per spec) |  | Medium | Boundary |  | 18,22 |
| **BOOL-008** | ✓ |  | ✓ | ✓ |  | Any field | Value not in mapping | {field}=maybe | 400 Bad Request + error body (A13) |  | High | Negative |  | 18,22 |
| **BOOL-009** | ✓ |  | ✓ | ✓ |  | Any field | Text | {field}=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 18,22 |
| **BOOL-010** | ✓ |  | ✓ | ✓ |  | JSON | Array | JSON {field}: [true] | 400 Bad Request + error body (A13) |  | Low | Negative |  | 18,22 |

### 4.7. Date / datetime (17 viewpoints)
* **Target / field type:** `Date`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **DATE-001** | ✓ |  | ✓ | ✓ |  | Any field | Valid date | {field}=2026-10-01 | Success. Saved / returned in the same format |  | High | Positive |  | 12,23 |
| **DATE-002** | ✓ |  | ✓ | ✓ |  | Any field | Wrong format dd/MM/yyyy | {field}=01/10/2026 | 400 Bad Request + error body (A13). Message states expected format |  | High | Negative | A5 | 12,23 |
| **DATE-003** | ✓ |  | ✓ | ✓ |  | Any field | Text instead of date | {field}=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 12,23 |
| **DATE-004** | ✓ |  | ✓ | ✓ |  | Any field | Non-existent date | {field}=2026-02-30 | 400 Bad Request + error body (A13) |  | High | Negative |  | 12,23 |
| **DATE-005** | ✓ |  | ✓ | ✓ |  | Any field | Month 13 / day 32 | {field}=2026-13-32 | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 12,23 |
| **DATE-006** | ✓ |  | ✓ | ✓ |  | Any field | Leap day (valid year) | {field}=2024-02-29 | Success |  | Medium | Boundary |  | 12,23 |
| **DATE-007** | ✓ |  | ✓ | ✓ |  | Any field | Leap day (invalid year) | {field}=2026-02-29 | 400 Bad Request + error body (A13) |  | Medium | Boundary |  | 12,23 |
| **DATE-008** | ✓ |  | ✓ | ✓ |  | Any field | Datetime with time | {field}=2026-01-01T00:00:00Z | Success if datetime supported, else 400 |  | Medium | Boundary |  | 12,23 |
| **DATE-009** | ✓ |  | ✓ | ✓ |  | Any field | Datetime with timezone offset | {field}=2026-01-01T00:00:00+07:00 | Success; boundary computed in the right timezone (if supported) |  | Low | Boundary |  | 12,23 |
| **DATE-010** | ✓ |  | ✓ | ✓ |  | Any field | Timestamp number | {field}=1790000000 | 400 Bad Request + error body (A13) (or accepted if timestamps are supported) |  | Low | Negative |  | 12,23 |
| **DATE-011** | ✓ |  | ✓ | ✓ |  | Required field | Empty string | {field}="" | 400 Bad Request + error body (A13) | Optional: ignored / default | High | Negative |  | 12,23 |
| **DATE-012** | ✓ |  | ✓ | ✓ |  | Required field | null | {field}=null | 400 Bad Request + error body (A13) | Optional: ignored | High | Negative |  | 12,23 |
| **DATE-013** | ✓ |  | ✓ | ✓ |  | Any field | Date in the past | {field}=2000-01-01 | Success, or 400 if rule forbids past dates |  | Medium | Boundary |  | 12,23 |
| **DATE-014** | ✓ |  | ✓ | ✓ |  | Any field | Date in the future | {field}=2999-12-31 | Success, or 400 if above maximum. Never 500 |  | Low | Boundary |  | 12,23 |
| **DATE-015** | ✓ |  | ✓ | ✓ |  | Any field | Very old date / year 0000 / year 9999 | {field}=1900-01-01 / 0000-01-01 / 9999-12-31 | Success or 400. Never 500 |  | Low | Boundary |  | 12,23 |
| **DATE-016** | ✓ |  | ✓ | ✓ |  | Any field | Special characters / SQL | {field}=2026-01-01'-- | 400 Bad Request + error body (A13). Never 500 |  | Medium | Security |  | 12,23 |
| **DATE-017** | ✓ |  | ✓ | ✓ |  | Any field | Date = today | {field}={today} | Success. Boundary handled correctly |  | Medium | Boundary |  | 12,23 |

### 4.8. Date range (17 viewpoints)
* **Target / field type:** `from_date / to_date`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **DR-001** | ✓ |  | ✓ |  |  | Any field | Both dates valid | from=2026-01-01&to=2026-12-31 | 200 OK. Only records inside the range |  | High | Positive |  | 12 |
| **DR-002** | ✓ |  | ✓ |  |  | Any field | Neither date sent | No from / to | 200 OK. Default list |  | Medium | Positive |  | 12 |
| **DR-003** | ✓ |  | ✓ |  |  | Any field | Both empty | from=&to= | 200 OK. Default list |  | Medium | Boundary |  | 12 |
| **DR-004** | ✓ |  | ✓ |  |  | Any field | Only from_date | from=2026-01-01 | 200 OK. From that date onward |  | High | Positive | A5 | 12 |
| **DR-005** | ✓ |  | ✓ |  |  | Any field | Only to_date | to=2026-12-31 | 200 OK. Up to that date |  | High | Positive | A5 | 12 |
| **DR-006** | ✓ |  | ✓ |  |  | Any field | Empty from_date only | from=&to=2026-12-31 | 200 OK. No lower bound |  | Medium | Boundary | A5 | 12 |
| **DR-007** | ✓ |  | ✓ |  |  | Any field | Empty to_date only | from=2026-01-01&to= | 200 OK. No upper bound |  | Medium | Boundary | A5 | 12 |
| **DR-008** | ✓ |  | ✓ |  |  | Any field | Both = null | from=null&to=null | 400 Bad Request + error body (A13) |  | High | Negative |  | 12 |
| **DR-009** | ✓ |  | ✓ |  |  | Any field | from_date = null / to_date = null | from=null  \|  to=null | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 12 |
| **DR-010** | ✓ |  | ✓ |  |  | Any field | from &lt; to | from=2026-01-01&to=2026-01-31 | 200 OK. Records within range |  | High | Positive |  | 12 |
| **DR-011** | ✓ |  | ✓ |  |  | Any field | from = to | from=to=2026-01-15 | 200 OK. Records of that single day (inclusive) |  | High | Boundary | A5 | 12 |
| **DR-012** | ✓ |  | ✓ |  |  | Any field | from &gt; to | from=2026-02-01&to=2026-01-01 | 400 Bad Request + error body (A13). Message: from must not be after to |  | High | Boundary |  | 12 |
| **DR-013** | ✓ |  | ✓ |  |  | Any field | from in the future | from=2099-01-01 | 200 OK. Empty list |  | High | Boundary |  | 12 |
| **DR-014** | ✓ |  | ✓ |  |  | Any field | to in the future | to=2099-12-31 | 200 OK. All records up to now |  | High | Boundary |  | 12 |
| **DR-015** | ✓ |  | ✓ |  |  | Any field | Record exactly on from_date is included | Record dated = from | Record IS included (inclusive) |  | High | Boundary | A5 | 12 |
| **DR-016** | ✓ |  | ✓ |  |  | Any field | Record exactly on to_date is included | Record dated = to (23:59:59) | Record IS included (inclusive) |  | High | Boundary | A5 | 12 |
| **DR-017** | ✓ |  | ✓ |  |  | Any field | Both dates are text | from=abc&to=xyz | 400 Bad Request + error body (A13) |  | High | Negative |  | 12 |

### 4.9. Email (15 viewpoints)
* **Target / field type:** `Email`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **MAIL-001** |  |  | ✓ | ✓ |  | Any field | Valid email | user@example.com | Success: 200 (read) / 201 (create) |  | High | Positive |  | 24,27 |
| **MAIL-002** |  |  | ✓ | ✓ |  | Any field | Missing @ | userexample.com | 400 Bad Request + error body (A13) |  | High | Negative |  | 24,27 |
| **MAIL-003** |  |  | ✓ | ✓ |  | Any field | Missing domain | user@ | 400 Bad Request + error body (A13) |  | High | Negative |  | 24,27 |
| **MAIL-004** |  |  | ✓ | ✓ |  | Any field | Missing local part | @example.com | 400 Bad Request + error body (A13) |  | High | Negative |  | 24,27 |
| **MAIL-005** |  |  | ✓ | ✓ |  | Any field | Missing TLD | user@example | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 24,27 |
| **MAIL-006** |  |  | ✓ | ✓ |  | Any field | Contains spaces | us er@example.com | 400 Bad Request + error body (A13) |  | High | Negative |  | 24,27 |
| **MAIL-007** |  |  | ✓ | ✓ |  | Any field | Two @ characters | a@b@example.com | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 24,27 |
| **MAIL-008** |  |  | ✓ | ✓ |  | Any field | Leading / trailing spaces | "  user@example.com  " | Trimmed (OK) or 400 |  | Medium | Boundary |  | 24,27 |
| **MAIL-009** |  |  | ✓ | ✓ |  | Any field | Upper-case | USER@EXAMPLE.COM | Success. Normalised to lowercase (or case kept per spec) |  | Medium | Boundary |  | 24,27 |
| **MAIL-010** |  |  | ✓ | ✓ |  | Any field | Plus addressing | user+tag@example.com | Success |  | Low | Positive |  | 24,27 |
| **MAIL-011** |  |  | ✓ | ✓ |  | Any field | Unicode / Vietnamese characters | nguyễn@example.com | 400 (or accepted if IDN supported) |  | Low | Boundary |  | 24,27 |
| **MAIL-012** |  |  | ✓ | ✓ |  | Has max length | Max length (254) | 254 characters | Success |  | Medium | Boundary |  | 24,27 |
| **MAIL-013** |  |  | ✓ | ✓ |  | Has max length | Max length + 1 (255) | 255 characters | 400 Bad Request + error body (A13) |  | Medium | Boundary |  | 24,27 |
| **MAIL-014** |  |  | ✓ | ✓ |  | Unique field | Duplicate email | Email that already exists | 409 Conflict + error body (A13). Message does not leak other user's data |  | High | Negative |  | 24,27 |
| **MAIL-015** |  |  | ✓ | ✓ |  | Any field | Number instead of string | JSON email: 123 | 400 Bad Request + error body (A13) |  | Low | Negative |  | 24,27 |

### 4.10. Enum / droplist (12 viewpoints)
* **Target / field type:** `Enum / droplist`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **ENUM-001** | ✓ |  | ✓ | ✓ |  | Any field | Each valid value | One request per allowed value | Success: 200 (read) / 201 (create) for every value. Result count matches DB |  | High | Positive |  | 09,25 |
| **ENUM-002** | ✓ |  | ✓ | ✓ |  | Optional field | Missing | Do not send {field} | Default list / default value |  | High | Positive |  | 09,25 |
| **ENUM-003** | ✓ |  | ✓ | ✓ |  | Any field | Empty value | {field}= | Default list (optional) or 400 (required) |  | Medium | Boundary |  | 09,25 |
| **ENUM-004** | ✓ |  | ✓ | ✓ |  | Any field | Value not in mapping | {field}=99999 / abc | 400 Bad Request + error body (A13). Message lists allowed values |  | High | Negative |  | 09,25 |
| **ENUM-005** | ✓ |  | ✓ | ✓ |  | Any field | Text where number expected | {field}=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 09,25 |
| **ENUM-006** | ✓ |  | ✓ | ✓ |  | Any field | Wrong letter case | {field}=ACTIVE (valid is 'active') | 400 Bad Request + error body (A13) (case-sensitive) |  | Medium | Negative | A2 | 09,25 |
| **ENUM-007** | ✓ |  | ✓ | ✓ |  | Any field | Negative / decimal | {field}=-1 / 1.5 | 400 Bad Request + error body (A13) |  | Medium | Boundary |  | 09,25 |
| **ENUM-008** | ✓ |  | ✓ | ✓ |  | Any field | Special characters | {field}=@#\$ | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 09,25 |
| **ENUM-009** | ✓ |  | ✓ | ✓ |  | Any field | Leading / trailing space | {field}=" active" | 400 Bad Request + error body (A13) |  | Low | Boundary |  | 09,25 |
| **ENUM-010** | ✓ |  | ✓ | ✓ |  | Multi-select | Multiple values | {field}=1,2  /  {field}=1&{field}=2 | Union of both values if multi-select supported, else 400 |  | Medium | Positive |  | 09,25 |
| **ENUM-011** | ✓ |  | ✓ | ✓ |  | JSON | Wrong type (number / array) | JSON {field}: 1  /  ["a","b"] | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 09,25 |
| **ENUM-012** | ✓ |  | ✓ | ✓ |  | Any field | Value = null | {field}=null | 400 Bad Request + error body (A13) |  | High | Negative |  | 09,25 |

### 4.11. Array / list (12 viewpoints)
* **Target / field type:** `Array`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **ARR-001** |  |  | ✓ |  |  | Any field | Valid array | ["a","b"] | Success. Order preserved |  | High | Positive |  | 26 |
| **ARR-002** |  |  | ✓ |  |  | Any field | Empty array | [] | Success, or 400 if at least 1 item required |  | Medium | Boundary |  | 26 |
| **ARR-003** |  |  | ✓ |  |  | Any field | null | null | 400 Bad Request + error body (A13) or treated as empty (per spec) |  | Medium | Negative |  | 26 |
| **ARR-004** |  |  | ✓ |  |  | Any field | String instead of array | "a" | 400 Bad Request + error body (A13) |  | High | Negative |  | 26 |
| **ARR-005** |  |  | ✓ |  |  | Any field | Wrong element type | [1,true,null] | 400 Bad Request + error body (A13) |  | High | Negative |  | 26 |
| **ARR-006** |  |  | ✓ |  |  | Any field | Duplicate elements | ["a","a"] | Duplicates removed, or 400 (per spec) |  | Medium | Boundary |  | 26 |
| **ARR-007** |  |  | ✓ |  |  | Has max items | Max items | {max_items} items | Success |  | High | Boundary |  | 26 |
| **ARR-008** |  |  | ✓ |  |  | Has max items | Max items + 1 | {max_items}+1 items | 400 Bad Request + error body (A13) |  | High | Boundary |  | 26 |
| **ARR-009** |  |  | ✓ |  |  | Any field | Element too long | One element &gt; max length | 400 Bad Request + error body (A13) |  | Medium | Boundary |  | 26 |
| **ARR-010** |  |  | ✓ |  |  | Any field | Element empty string | [""] | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 26 |
| **ARR-011** |  |  | ✓ |  |  | Any field | Nested array | [["a"]] | 400 Bad Request + error body (A13) |  | Low | Negative |  | 26 |
| **ARR-012** |  |  | ✓ |  |  | Optional field | Missing (optional array) | Do not send field | Success with empty list |  | Medium | Positive |  | 26 |

### 4.12. Pagination - limit (16 viewpoints)
* **Target / field type:** `limit`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **LIM-001** | ✓ |  |  |  |  | Any field | Not sent | No limit | 200 OK. Default page size |  | Medium | Positive |  | 10 |
| **LIM-002** | ✓ |  |  |  |  | Any field | Empty | limit= | 200 OK. Default page size |  | Medium | Boundary |  | 10 |
| **LIM-003** | ✓ |  |  |  |  | Any field | Negative | limit=-1 | 400 Bad Request + error body (A13) |  | High | Boundary |  | 10 |
| **LIM-004** | ✓ |  |  |  |  | Any field | Zero | limit=0 | 400 Bad Request + error body (A13) |  | High | Boundary |  | 10 |
| **LIM-005** | ✓ |  |  |  |  | Any field | One | limit=1 | 200 OK. Exactly 1 record (the first) |  | High | Boundary |  | 10 |
| **LIM-006** | ✓ |  |  |  |  | Any field | Normal value | limit=5 | 200 OK. Exactly 5 records |  | High | Positive |  | 10 |
| **LIM-007** | ✓ |  |  |  |  | Any field | Max | limit={max_limit} | 200 OK. Up to max records |  | High | Boundary |  | 10 |
| **LIM-008** | ✓ |  |  |  |  | Any field | Max + 1 | limit={max_limit}+1 | 400 Bad Request + error body (A13) (or capped to max) |  | High | Boundary | A4 | 10 |
| **LIM-009** | ✓ |  |  |  |  | Any field | Greater than total records | limit = total+1 | 200 OK. All existing records (not an error) |  | High | Boundary |  | 10 |
| **LIM-010** | ✓ |  |  |  |  | Any field | Very large (32-bit overflow) | limit=2147483648 | 400 Bad Request + error body (A13) (or capped). Never 500 |  | High | Boundary |  | 10 |
| **LIM-011** | ✓ |  |  |  |  | Any field | Extremely large | limit=99999999999999999999 | 400 Bad Request + error body (A13). Never 500 |  | Medium | Boundary |  | 10 |
| **LIM-012** | ✓ |  |  |  |  | Any field | Decimal | limit=1.5 | 400 Bad Request + error body (A13) |  | High | Negative |  | 10 |
| **LIM-013** | ✓ |  |  |  |  | Any field | Text | limit=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 10 |
| **LIM-014** | ✓ |  |  |  |  | Any field | Special characters | limit=@# | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 10 |
| **LIM-015** | ✓ |  |  |  |  | Any field | null | limit=null | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 10 |
| **LIM-016** | ✓ |  |  |  |  | Any field | Spaces / leading zeros | limit=%205  /  limit=005 | Trimmed / same as 5 – consistent for all numeric params |  | Low | Boundary |  | 10 |

### 4.13. Pagination - offset (13 viewpoints)
* **Target / field type:** `offset`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **OFF-001** | ✓ |  |  |  |  | Any field | Not sent | No offset | 200 OK. Starts at first record |  | Medium | Positive |  | 11 |
| **OFF-002** | ✓ |  |  |  |  | Any field | Empty | offset= | 200 OK. offset = 0 |  | Medium | Boundary |  | 11 |
| **OFF-003** | ✓ |  |  |  |  | Any field | Negative | offset=-1 | 400 Bad Request + error body (A13) |  | High | Boundary |  | 11 |
| **OFF-004** | ✓ |  |  |  |  | Any field | Zero | offset=0 | 200 OK. First record first |  | High | Boundary |  | 11 |
| **OFF-005** | ✓ |  |  |  |  | Any field | Normal value | offset=5 | 200 OK. First 5 skipped; first returned = #6 |  | High | Positive |  | 11 |
| **OFF-006** | ✓ |  |  |  |  | Any field | Total - 1 | offset = total-1 | 200 OK. Exactly 1 record (the last) |  | High | Boundary |  | 11 |
| **OFF-007** | ✓ |  |  |  |  | Any field | Equal to total | offset = total | 200 OK. Empty list (not 404) |  | High | Boundary |  | 11 |
| **OFF-008** | ✓ |  |  |  |  | Any field | Greater than total | offset = total+1 | 200 OK. Empty list |  | High | Boundary |  | 11 |
| **OFF-009** | ✓ |  |  |  |  | Any field | Very large | offset=2147483648 | 200 empty list or 400. Never 500 |  | High | Boundary |  | 11 |
| **OFF-010** | ✓ |  |  |  |  | Any field | Decimal | offset=1.5 | 400 Bad Request + error body (A13) |  | High | Negative |  | 11 |
| **OFF-011** | ✓ |  |  |  |  | Any field | Text | offset=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 11 |
| **OFF-012** | ✓ |  |  |  |  | Any field | Special characters | offset=@# | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 11 |
| **OFF-013** | ✓ |  |  |  |  | Any field | null | offset=null | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 11 |

### 4.14. Pagination - combination (10 viewpoints)
* **Target / field type:** `limit + offset + filters`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **PAGE-001** | ✓ |  |  |  |  | Any field | All filters together | q + droplist + dates + limit + offset | 200 OK. Filters combined with AND; count correct |  | High | Positive |  | 14 |
| **PAGE-002** | ✓ |  |  |  |  | Any field | Filters with empty intersection | Conflicting filters | 200 OK. Empty list; total=0 |  | High | Boundary |  | 14 |
| **PAGE-003** | ✓ |  |  |  |  | Any field | Page 1 and page 2 do not overlap | limit=5&offset=0 then offset=5 | No duplicated / missing record between pages |  | High | Positive |  | 14 |
| **PAGE-004** | ✓ |  |  |  |  | Any field | Last partial page | offset = total-2, limit=5 | 200 OK. Exactly 2 records |  | High | Boundary |  | 14 |
| **PAGE-005** | ✓ |  |  |  |  | Any field | Page beyond the last page | offset &gt;= total | 200 OK. Empty list |  | High | Boundary |  | 14 |
| **PAGE-006** | ✓ |  |  |  |  | Any field | Total consistent on every page | Compare 'total' across pages | Same total = real number of matching records |  | Medium | Positive |  | 14 |
| **PAGE-007** | ✓ |  |  |  |  | Any field | Next / previous links | Check links on first / middle / last page | next=null on last page, previous=null on first page; links work |  | Medium | Positive |  | 14 |
| **PAGE-008** | ✓ |  |  |  |  | Any field | Same request twice | Identical GET twice | Same data and order (idempotent) |  | Low | Positive |  | 14 |
| **PAGE-009** | ✓ |  |  |  |  | Any field | Valid + invalid params mixed | limit=5&offset=abc | 400 Bad Request + error body (A13). Message names the invalid param |  | High | Negative |  | 14 |
| **PAGE-010** | ✓ |  |  |  |  | Any field | Deleted record not in list | Search for a deleted record | Deleted record NOT returned; total reduced |  | Medium | Positive |  | 14 |

### 4.15. Sorting (10 viewpoints)
* **Target / field type:** `sort_by / order`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SORT-001** | ✓ |  |  |  |  | API supports sorting | Sort ascending | sort_by={field}&order=asc | Sorted ascending |  | Medium | Positive |  | 13 |
| **SORT-002** | ✓ |  |  |  |  | API supports sorting | Sort descending | sort_by={field}&order=desc | Sorted descending |  | Medium | Positive |  | 13 |
| **SORT-003** | ✓ |  |  |  |  | API supports sorting | Sort by date field | sort_by=created_at&order=desc | Newest first |  | Medium | Positive |  | 13 |
| **SORT-004** | ✓ |  |  |  |  | API supports sorting | Sort field does not exist | sort_by=abc | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 13 |
| **SORT-005** | ✓ |  |  |  |  | API supports sorting | Sort field is SQL fragment | sort_by=name;DROP TABLE x | 400 Bad Request + error body (A13). No SQL executed |  | High | Security |  | 13 |
| **SORT-006** | ✓ |  |  |  |  | API supports sorting | Invalid order value | order=abc | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 13 |
| **SORT-007** | ✓ |  |  |  |  | API supports sorting | Empty order | order= | Default order |  | Low | Boundary |  | 13 |
| **SORT-008** | ✓ |  |  |  |  | API supports sorting | Upper-case order | order=ASC | Accepted or 400 – consistent with other enums |  | Low | Boundary | A2 | 13 |
| **SORT-009** | ✓ |  |  |  |  | API supports sorting | order without sort_by | order=desc | Default sort field with given order |  | Low | Negative |  | 13 |
| **SORT-010** | ✓ |  |  |  |  | API supports sorting | Sort stability | Sort by field with duplicate values and page through | No record duplicated / skipped (secondary sort key = id) |  | Medium | Boundary |  | 13 |

### 4.16. Path parameter (15 viewpoints)
* **Target / field type:** `Resource id`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **PATH-001** |  | ✓ |  |  |  | Any field | Valid id | /items/{valid_id}/ | 200 OK. Body is that record |  | High | Positive |  | 15 |
| **PATH-002** |  | ✓ |  |  |  | Any field | Id does not exist | /items/999999999/ | 404 Not Found + error body (A13) |  | High | Negative |  | 15 |
| **PATH-003** |  | ✓ |  |  |  | Any field | Id = 0 | /items/0/ | 404 (or 400) – consistent |  | High | Boundary |  | 15 |
| **PATH-004** |  | ✓ |  |  |  | Any field | Negative id | /items/-1/ | 400 Bad Request + error body (A13) or 404 (A6). Never 500 |  | High | Boundary | A6 | 15 |
| **PATH-005** |  | ✓ |  |  |  | Any field | Text id | /items/abc/ | 400 Bad Request + error body (A13) |  | High | Negative | A6 | 15 |
| **PATH-006** |  | ✓ |  |  |  | Any field | Decimal id | /items/1.5/ | 400 Bad Request + error body (A13) |  | Medium | Negative | A6 | 15 |
| **PATH-007** |  | ✓ |  |  |  | Any field | Id too large | /items/99999999999999999999/ | 404 or 400. Never 500 |  | Medium | Boundary |  | 15 |
| **PATH-008** |  | ✓ |  |  |  | Any field | Special characters | /items/@%23\$/ | 400 or 404. Never 500 |  | Medium | Negative |  | 15 |
| **PATH-009** |  | ✓ |  |  |  | Any field | Spaces | /items/%201/ | 400 or 404 |  | Low | Negative |  | 15 |
| **PATH-010** |  | ✓ |  |  |  | Any field | Leading zeros | /items/0001/ | Same as id=1, or 404 – consistent |  | Low | Boundary |  | 15 |
| **PATH-011** |  | ✓ |  |  |  | Any field | SQL fragment | /items/1%20OR%201=1/ | 400 or 404. 0 or 1 record. No SQL executed |  | High | Security |  | 15 |
| **PATH-012** |  | ✓ |  |  |  | Soft delete | Soft-deleted record | Id of a deleted record | 404 Not Found + error body (A13) |  | High | Negative |  | 15 |
| **PATH-013** |  | ✓ |  |  |  | Id is UUID | Invalid UUID format | /items/123-abc/ | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 15 |
| **PATH-014** |  | ✓ |  |  |  | Id is UUID | Valid UUID but not found | Random UUID | 404 Not Found + error body (A13) |  | Medium | Negative |  | 15 |
| **PATH-015** |  | ✓ |  |  |  | Any field | Extra path segment | /items/1/abc/ | 404 Not Found + error body (A13) |  | Low | Negative |  | 15 |

### 4.17. Header - general (2 viewpoints)
* **Target / field type:** `All headers`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **HDR-001** |  |  |  |  | ✓ | Any field | No header at all | Send request without any header | 401 Unauthorized + error body (A13) |  | High | Negative |  | 03 |
| **HDR-002** |  |  |  |  | ✓ | Any field | Header name in lower-case | authorization: Bearer ... | 200 OK (header names are case-insensitive) |  | Low | Positive |  | 03 |

### 4.18. Header - Accept (7 viewpoints)
* **Target / field type:** `Accept`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **ACC-001** |  |  |  |  | ✓ | Any field | Valid Accept | Accept: application/json | 200 OK; response Content-Type = application/json |  | High | Positive |  | 03 |
| **ACC-002** |  |  |  |  | ✓ | Any field | Accept missing | Remove Accept | 200 OK; default JSON |  | Medium | Negative | A9 | 03 |
| **ACC-003** |  |  |  |  | ✓ | Any field | Accept empty | Accept: | 200 OK; default JSON |  | Medium | Negative | A9 | 03 |
| **ACC-004** |  |  |  |  | ✓ | Any field | Accept = */* | Accept: */* | 200 OK; JSON |  | Medium | Positive |  | 03 |
| **ACC-005** |  |  |  |  | ✓ | Any field | Accept with charset | Accept: application/json; charset=utf-8 | 200 OK; JSON |  | Low | Positive |  | 03 |
| **ACC-006** |  |  |  |  | ✓ | Any field | Accept not supported | Accept: text/xml | 406 Not Acceptable + error body (A13) |  | High | Negative |  | 03 |
| **ACC-007** |  |  |  |  | ✓ | Any field | Accept invalid value | Accept: abc@@@ | 406 or 400. Never 500 |  | Medium | Negative |  | 03 |

### 4.19. Header - Content-Type (9 viewpoints)
* **Target / field type:** `Content-Type`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **CT-001** |  |  |  |  | ✓ | Any field | GET without Content-Type | Remove Content-Type on GET | 200 OK (ignored for GET) |  | Medium | Positive | A9 | 04,19 |
| **CT-002** |  |  |  |  | ✓ | Any field | GET with empty / invalid Content-Type | Content-Type: (empty) / abc on GET | 200 OK (ignored for GET) |  | Low | Negative | A9 | 04,19 |
| **CT-003** |  |  |  |  | ✓ | Endpoint with body | Body request without Content-Type | POST with body, no Content-Type | 415 Unsupported Media Type + error body (A13) |  | High | Negative | A7 | 04,19 |
| **CT-004** |  |  |  |  | ✓ | Endpoint with body | Empty Content-Type | POST with Content-Type empty | 415 Unsupported Media Type + error body (A13) |  | High | Negative | A7 | 04,19 |
| **CT-005** |  |  |  |  | ✓ | Endpoint with body | Content-Type = text/plain | JSON body + text/plain | 415 Unsupported Media Type + error body (A13) |  | High | Negative | A7 | 04,19 |
| **CT-006** |  |  |  |  | ✓ | Endpoint with body | Content-Type = text/xml | XML body + text/xml | 415 Unsupported Media Type + error body (A13) |  | High | Negative | A7 | 04,19 |
| **CT-007** |  |  |  |  | ✓ | Endpoint with body | Content-Type invalid value | Content-Type: abc@@@ | 415 or 400. Never 500 |  | High | Negative |  | 04,19 |
| **CT-008** |  |  |  |  | ✓ | Endpoint with body | Content-Type does not match body | application/json header with form-urlencoded body | 400 Bad Request + error body (A13) |  | High | Negative |  | 04,19 |
| **CT-009** |  |  |  |  | ✓ | Endpoint with body | Content-Type with charset | application/json; charset=utf-8 | Success |  | Medium | Positive |  | 04,19 |

### 4.20. Header - Authorization (16 viewpoints)
* **Target / field type:** `Authorization`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **AUTH-001** |  |  |  |  | ✓ | Any field | Authorization missing | Remove header | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-002** |  |  |  |  | ✓ | Any field | Authorization empty | Authorization: | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-003** |  |  |  |  | ✓ | Any field | Scheme only | Authorization: Bearer | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-004** |  |  |  |  | ✓ | Any field | Wrong scheme | Authorization: Basic &lt;token&gt; | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-005** |  |  |  |  | ✓ | Any field | Missing scheme | Authorization: &lt;token&gt; | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-006** |  |  |  |  | ✓ | Any field | Lower-case scheme | Authorization: bearer &lt;token&gt; | 200 OK (RFC 7235) or 401 if strict |  | Low | Boundary |  | 05 |
| **AUTH-007** |  |  |  |  | ✓ | Any field | Invalid token | Authorization: Bearer abc123 | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-008** |  |  |  |  | ✓ | Any field | Tampered token | Change 1 character of a valid token | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-009** |  |  |  |  | ✓ | Any field | Expired token | Token expired | 401. Message says token/session expired |  | High | Negative |  | 05 |
| **AUTH-010** |  |  |  |  | ✓ | Any field | Token from another environment | UAT token on PROD | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-011** |  |  |  |  | ✓ | Any field | Token of locked / deleted user | User locked after token issued | 401 (or 403) |  | High | Negative |  | 05 |
| **AUTH-012** |  |  |  |  | ✓ | Any field | Token after logout | Use token after logout | 401 Unauthorized + error body (A13) |  | High | Negative |  | 05 |
| **AUTH-013** |  |  |  |  | ✓ | Any field | Token after password change | Old token after password change | 401 (if tokens revoked) |  | Medium | Negative |  | 05 |
| **AUTH-014** |  |  |  |  | ✓ | Any field | Duplicate Authorization header | Two Authorization headers, one invalid | 401 or 400. Never 200 |  | Medium | Security |  | 05 |
| **AUTH-015** |  |  |  |  | ✓ | Any field | Valid Authorization | Authorization: Bearer &lt;valid&gt; | 200 OK |  | High | Positive |  | 05 |
| **AUTH-016** |  |  |  |  | ✓ | Any field | Token in URL | ?access_token=&lt;valid&gt; without header | 401 Unauthorized + error body (A13) (tokens only accepted in header) |  | Medium | Security |  | 05 |

### 4.21. Header - X-CSRFToken (7 viewpoints)
* **Target / field type:** `X-CSRFToken`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **CSRF-001** |  |  |  |  | ✓ | Any field | Safe method without CSRF | GET without X-CSRFToken | 200 OK (CSRF not enforced for GET) |  | Medium | Positive | A9 | 06 |
| **CSRF-002** |  |  |  |  | ✓ | Any field | Safe method with invalid CSRF | GET with empty / invalid token | 200 OK |  | Low | Negative | A9 | 06 |
| **CSRF-003** |  |  |  |  | ✓ | Cookie-session auth | Unsafe method without CSRF | POST/PUT/PATCH/DELETE without token | 403 Forbidden + error body (A13). No data changed |  | High | Negative | A9 | 06 |
| **CSRF-004** |  |  |  |  | ✓ | Cookie-session auth | Unsafe method with empty CSRF | X-CSRFToken: (empty) | 403 Forbidden + error body (A13). No data changed |  | High | Negative | A9 | 06 |
| **CSRF-005** |  |  |  |  | ✓ | Cookie-session auth | Unsafe method with invalid CSRF | X-CSRFToken: abc | 403 Forbidden + error body (A13). No data changed |  | High | Negative | A9 | 06 |
| **CSRF-006** |  |  |  |  | ✓ | Cookie-session auth | CSRF of another session | Token of another user | 403 Forbidden + error body (A13) |  | High | Negative | A9 | 06 |
| **CSRF-007** |  |  |  |  | ✓ | Cookie-session auth | Valid CSRF | Valid token | Success |  | High | Positive | A9 | 06 |

### 4.22. HTTP method & status (12 viewpoints)
* **Target / field type:** `Method / endpoint`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **MTD-001** |  |  |  |  |  | Any field | Valid request | Valid headers + params | 200 OK. Body matches schema |  | High | Positive |  | 01,02 |
| **MTD-002** |  |  |  |  |  | Any field | Wrong endpoint | GET /not-found/ | 404 + JSON body (not HTML) |  | High | Negative |  | 01,02 |
| **MTD-003** |  |  |  |  |  | Any field | Trailing slash | /resource vs /resource/ | 200 or 301/308 to canonical URL – consistent |  | Low | Boundary |  | 01,02 |
| **MTD-004** |  |  |  |  |  | Any field | Unsupported API version | /api/v99/resource/ | 404 Not Found + error body (A13) |  | Low | Negative |  | 01,02 |
| **MTD-005** |  |  |  |  |  | Endpoint does not support method | Unsupported method POST | POST on read-only endpoint | 405 + header Allow |  | High | Negative |  | 01,02 |
| **MTD-006** |  |  |  |  |  | Endpoint does not support method | Unsupported method PUT | PUT on read-only endpoint | 405 + header Allow |  | High | Negative |  | 01,02 |
| **MTD-007** |  |  |  |  |  | Endpoint does not support method | Unsupported method PATCH | PATCH on read-only endpoint | 405 + header Allow |  | High | Negative |  | 01,02 |
| **MTD-008** |  |  |  |  |  | Endpoint does not support method | Unsupported method DELETE | DELETE on read-only endpoint | 405 + header Allow. No data deleted |  | High | Negative |  | 01,02 |
| **MTD-009** |  |  |  |  |  | Any field | HEAD method | HEAD | 200, same headers as GET, empty body |  | Medium | Positive |  | 01,02 |
| **MTD-010** |  |  |  |  |  | Any field | OPTIONS method | OPTIONS | 200/204 + header Allow |  | Medium | Positive |  | 01,02 |
| **MTD-011** |  |  |  |  |  | Any field | Lower-case method | get /resource | 400 or 405. Never 500 |  | Low | Negative |  | 01,02 |
| **MTD-012** |  |  |  |  |  | Any field | Method override header | X-HTTP-Method-Override: DELETE on POST | Ignored or rejected. No data deleted |  | Medium | Security |  | 01,02 |

### 4.23. Authorization & permission (8 viewpoints)
* **Target / field type:** `Role / ownership`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **PERM-001** |  |  |  |  |  | Any field | Admin role | Call with Admin token | 200 OK. Full data |  | High | Positive |  | 07 |
| **PERM-002** |  |  |  |  |  | Any field | Role without permission | Normal user calls admin-only API | 403 Forbidden + error body (A13) |  | High | Negative |  | 07 |
| **PERM-003** |  |  |  |  |  | Any field | Read other user's data (IDOR) | User A requests record of user B | 403 or 404. No data of B |  | High | Security |  | 07 |
| **PERM-004** |  |  |  |  |  | Any field | Modify other user's data | User A updates record of B | 403 or 404. Data unchanged |  | High | Security |  | 07 |
| **PERM-005** |  |  |  |  |  | Any field | Delete other user's data | User A deletes record of B | 403 or 404. Data unchanged |  | High | Security |  | 07 |
| **PERM-006** |  |  |  |  |  | Any field | No create permission | Read-only user calls POST | 403 Forbidden + error body (A13). No record created |  | High | Negative |  | 07 |
| **PERM-007** |  |  |  |  |  | Any field | No delete permission | Read-only user calls DELETE | 403 Forbidden + error body (A13). Record still exists |  | High | Negative |  | 07 |
| **PERM-008** |  |  |  |  |  | Any field | Privilege escalation via body | Normal user sends role=admin | Ignored or 400/403. Role NOT changed |  | High | Security |  | 07 |

### 4.24. Body - JSON structure (15 viewpoints)
* **Target / field type:** `Request body`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **BODY-001** |  |  | ✓ |  |  | Any field | Valid body | All fields valid | 201 Created. Body has id and sent fields |  | High | Positive |  | 19,16 |
| **BODY-002** |  |  | ✓ |  |  | Any field | Body is not JSON | Plain text with Content-Type: application/json | 400 Bad Request + error body (A13) |  | High | Negative |  | 19,16 |
| **BODY-003** |  |  | ✓ |  |  | Any field | Missing closing brace | {"a":1 | 400 Bad Request + error body (A13). Message: invalid JSON |  | High | Negative |  | 19,16 |
| **BODY-004** |  |  | ✓ |  |  | Any field | Trailing comma | {"a":1,} | 400 Bad Request + error body (A13) |  | High | Negative |  | 19,16 |
| **BODY-005** |  |  | ✓ |  |  | Any field | Single quotes | {'a':'b'} | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 19,16 |
| **BODY-006** |  |  | ✓ |  |  | Any field | Empty body | No body | 400 Bad Request + error body (A13) |  | High | Negative |  | 19,16 |
| **BODY-007** |  |  | ✓ |  |  | Any field | Body = {} | {} | 400 Bad Request + error body (A13). Lists missing required fields |  | High | Negative |  | 19,16 |
| **BODY-008** |  |  | ✓ |  |  | Any field | Body = null | null | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 19,16 |
| **BODY-009** |  |  | ✓ |  |  | Any field | Body = array | [ {…} ] | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 19,16 |
| **BODY-010** |  |  | ✓ |  |  | Any field | Body = string / number | "abc" / 123 | 400 Bad Request + error body (A13) |  | Low | Negative |  | 19,16 |
| **BODY-011** |  |  | ✓ |  |  | Any field | Duplicate key in JSON | {"a":1,"a":2} | Last value used. Never 500 |  | Low | Boundary | A3 | 19,16 |
| **BODY-012** |  |  | ✓ |  |  | Any field | Deeply nested JSON | 1000 nested levels | 400 or 413. Server stable |  | Low | Security |  | 19,16 |
| **BODY-013** |  |  | ✓ |  |  | Any field | Payload too large | Body &gt; server limit | 413 Payload Too Large |  | Medium | Boundary |  | 19,16 |
| **BODY-014** |  |  | ✓ |  |  | Any field | UTF-8 BOM | Body starts with BOM | Success or 400 – consistent |  | Low | Boundary |  | 19,16 |
| **BODY-015** |  |  | ✓ |  |  | Any field | Invalid UTF-8 bytes | Invalid byte sequence | 400 Bad Request + error body (A13) |  | Low | Security |  | 19,16 |

### 4.25. Body - form-data (5 viewpoints)
* **Target / field type:** `Request body`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **FORM-001** |  |  |  | ✓ |  | Any field | Body is not multipart | JSON sent to multipart endpoint | 415 Unsupported Media Type + error body (A13) |  | High | Negative | A7 | 16 |
| **FORM-002** |  |  |  | ✓ |  | Any field | Missing boundary | multipart/form-data without boundary | 400 Bad Request + error body (A13) |  | High | Negative |  | 16 |
| **FORM-003** |  |  |  | ✓ |  | Any field | All parts missing | Empty multipart | 400 Bad Request + error body (A13) |  | High | Negative |  | 16 |
| **FORM-004** |  |  |  | ✓ |  | Any field | All parts null / empty | Every part empty | 400 Bad Request + error body (A13) |  | High | Negative |  | 16 |
| **FORM-005** |  |  |  | ✓ |  | Any field | Unknown extra part | Add unknown part | Success. Ignored |  | Low | Negative | A10 | 16 |

### 4.26. File upload (24 viewpoints)
* **Target / field type:** `File`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **FILE-001** |  |  |  | ✓ |  | Any field | Valid file | Allowed type, normal size | 201 (or 200). Body has file id/url/name/size |  | High | Positive |  | 16 |
| **FILE-002** |  |  |  | ✓ |  | Any field | File part sent as text | file=abc (not a file) | 400 Bad Request + error body (A13) |  | High | Negative |  | 16 |
| **FILE-003** |  |  |  | ✓ |  | Any field | Invalid extension (.exe .php .txt) | Upload test.exe | 415 Unsupported Media Type + error body (A13) (or 400). Not stored |  | High | Negative | A8 | 16 |
| **FILE-004** |  |  |  | ✓ |  | Any field | Extension in UPPER case | TEST.JPG | 201 (check is case-insensitive) |  | Medium | Boundary |  | 16 |
| **FILE-005** |  |  |  | ✓ |  | Any field | No extension | File named 'test' | 415 or 400 |  | Medium | Boundary | A8 | 16 |
| **FILE-006** |  |  |  | ✓ |  | Any field | Double extension | test.php.jpg | Rejected, or stored safely and never executed |  | High | Security |  | 16 |
| **FILE-007** |  |  |  | ✓ |  | Any field | Spoofed extension | malware.exe renamed .jpg | Rejected: real content (magic bytes) checked |  | High | Security |  | 16 |
| **FILE-008** |  |  |  | ✓ |  | Any field | Wrong MIME in part header | Part type image/jpeg but file is pdf | Rejected, or type detected from content |  | Medium | Security |  | 16 |
| **FILE-009** |  |  |  | ✓ |  | Any field | Size = max - 1 byte | {max_file_size}-1 | 201 |  | High | Boundary |  | 16 |
| **FILE-010** |  |  |  | ✓ |  | Any field | Size = max | {max_file_size} | 201 |  | High | Boundary |  | 16 |
| **FILE-011** |  |  |  | ✓ |  | Any field | Size = max + 1 byte | {max_file_size}+1 | 413 (or 400). Not stored |  | High | Boundary | A8 | 16 |
| **FILE-012** |  |  |  | ✓ |  | Any field | File 0 KB | Empty file | 400 Bad Request + error body (A13) |  | High | Boundary |  | 16 |
| **FILE-013** |  |  |  | ✓ |  | Any field | Corrupted file | Truncated file with valid extension | 400 Bad Request + error body (A13) (or 415) |  | Medium | Negative |  | 16 |
| **FILE-014** |  |  |  | ✓ |  | Any field | Password-protected file | Locked PDF / ZIP | Handled per spec. Never 500 |  | Low | Negative |  | 16 |
| **FILE-015** |  |  |  | ✓ |  | Any field | Filename very long | 256+ characters | 400 or truncated name. Never 500 |  | Medium | Boundary |  | 16 |
| **FILE-016** |  |  |  | ✓ |  | Any field | Filename special characters | te st@#\$%.jpg | Sanitised name, or 400 |  | Medium | Boundary |  | 16 |
| **FILE-017** |  |  |  | ✓ |  | Any field | Filename Vietnamese | tài liệu.jpg | 201. Name kept in UTF-8 |  | Medium | Positive |  | 16 |
| **FILE-018** |  |  |  | ✓ |  | Any field | Filename path traversal | ../../etc/passwd.jpg | Path stripped. Nothing written outside upload folder |  | High | Security |  | 16 |
| **FILE-019** |  |  |  | ✓ |  | Any field | Filename missing | Part without filename | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 16 |
| **FILE-020** |  |  |  | ✓ |  | Multi-file | Multiple files | 2+ files in one request | Success if supported, else 400 |  | Medium | Negative |  | 16 |
| **FILE-021** |  |  |  | ✓ |  | Multi-file | More files than max | max+1 files | 400 Bad Request + error body (A13) (or 413) |  | Medium | Boundary |  | 16 |
| **FILE-022** |  |  |  | ✓ |  | Any field | Same file twice | Upload identical file 2 times | 201 both (2 records) or 409 per spec |  | Low | Negative |  | 16 |
| **FILE-023** |  |  |  | ✓ |  | Any field | File + extra text fields | file + name=abc | 201. Text field saved correctly |  | High | Positive |  | 16 |
| **FILE-024** |  |  |  | ✓ |  | Any field | Uploaded file retrievable | Download via returned URL | 200. File identical (same hash) |  | High | Positive |  | 16 |

### 4.27. Login / authentication (26 viewpoints)
* **Target / field type:** `Credentials`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **LOGIN-001** |  |  | ✓ |  |  | Any field | Valid credentials | Correct email + password | 200 + token + expiry. NO password/hash in response |  | High | Positive |  | 27 |
| **LOGIN-002** |  |  | ✓ |  |  | Any field | Wrong password | Correct email, wrong password | 401. Generic message |  | High | Negative |  | 27 |
| **LOGIN-003** |  |  | ✓ |  |  | Any field | Unknown email | Email not registered | 401. SAME message as wrong password (no user enumeration) |  | High | Security |  | 27 |
| **LOGIN-004** |  |  | ✓ |  |  | Any field | Email = null | email: null | 400 Bad Request + error body (A13). Error points to email |  | High | Negative |  | 27 |
| **LOGIN-005** |  |  | ✓ |  |  | Any field | Email key absent | Only password sent | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-006** |  |  | ✓ |  |  | Any field | Password key absent | Only email sent | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-007** |  |  | ✓ |  |  | Any field | Email empty | email: "" | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-008** |  |  | ✓ |  |  | Any field | Password empty | password: "" | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-009** |  |  | ✓ |  |  | Any field | Both empty | email & password empty | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-010** |  |  | ✓ |  |  | Any field | Both null | email & password null | 400 Bad Request + error body (A13) |  | High | Negative |  | 27 |
| **LOGIN-011** |  |  | ✓ |  |  | Any field | Invalid email format | email: abc | 400 Bad Request + error body (A13) |  | Medium | Negative |  | 27 |
| **LOGIN-012** |  |  | ✓ |  |  | Any field | Email with surrounding spaces | "  user@x.com  " | Trimmed (200) or 400 – consistent |  | Low | Boundary |  | 27 |
| **LOGIN-013** |  |  | ✓ |  |  | Any field | Email upper-case | USER@X.COM | 200 (email case-insensitive) |  | Medium | Boundary |  | 27 |
| **LOGIN-014** |  |  | ✓ |  |  | Any field | Password is case-sensitive | Changed letter case | 401 |  | Medium | Negative |  | 27 |
| **LOGIN-015** |  |  | ✓ |  |  | Any field | Password with surrounding spaces | " pass " | 401 (spaces are part of password) |  | Low | Boundary |  | 27 |
| **LOGIN-016** |  |  | ✓ |  |  | Any field | Password max length | Max allowed length | 401 (wrong password). Never 500 |  | Low | Boundary |  | 27 |
| **LOGIN-017** |  |  | ✓ |  |  | Any field | Very long password | 10,000 characters | 400/401/413. No timeout / 500 |  | Medium | Security |  | 27 |
| **LOGIN-018** |  |  | ✓ |  |  | Any field | Locked account | Locked user | 403 (or 423). Message says locked |  | High | Negative |  | 27 |
| **LOGIN-019** |  |  | ✓ |  |  | Any field | Inactive / unverified account | Inactive user | 403. Message asks to activate |  | Medium | Negative |  | 27 |
| **LOGIN-020** |  |  | ✓ |  |  | Any field | SQL injection in email | ' OR 1=1 -- | 400/401. No login, no SQL error |  | High | Security |  | 27 |
| **LOGIN-021** |  |  | ✓ |  |  | Any field | SQL injection in password | ' OR '1'='1 | 401. No login |  | High | Security |  | 27 |
| **LOGIN-022** |  |  | ✓ |  |  | Any field | Brute force | 10+ wrong passwords | 429 or temporary lock. Retry-After header |  | High | Security | A14 | 27 |
| **LOGIN-023** |  |  | ✓ |  |  | Any field | Login after failed attempts | Correct password after 2 failures | 200. Failure counter reset |  | Medium | Positive |  | 27 |
| **LOGIN-024** |  |  | ✓ |  |  | Any field | Token is usable | Call protected API with new token | 200. Expiry matches login response |  | High | Positive |  | 27 |
| **LOGIN-025** |  |  | ✓ |  |  | Any field | GET on login endpoint | GET /login | 405 |  | Medium | Negative |  | 27 |
| **LOGIN-026** |  |  | ✓ |  |  | Any field | Credentials in URL | ?email=..&password=.. | Ignored → 400/401 |  | Medium | Security |  | 27 |

### 4.28. CRUD - Create (8 viewpoints)
* **Target / field type:** `POST`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **CRE-001** |  |  | ✓ |  |  | Any field | Create success | Valid body | 201 + Location header + id |  | High | Positive |  | 28 |
| **CRE-002** |  |  | ✓ |  |  | Any field | Record persisted | GET after create | 200. Data equals what was sent |  | High | Positive |  | 28 |
| **CRE-003** |  |  | ✓ |  |  | Any field | Server-generated fields | Check id / created_at / created_by | Generated by server |  | Medium | Positive |  | 28 |
| **CRE-004** |  |  | ✓ |  |  | Any field | Client sends read-only fields | id / created_at in body | Ignored; server values used |  | High | Security |  | 28 |
| **CRE-005** |  |  | ✓ |  |  | Any field | Foreign key does not exist | category_id not found | 400 Bad Request + error body (A13) (or 404/422). Nothing created |  | Medium | Negative |  | 28 |
| **CRE-006** |  |  | ✓ |  |  | Unique field | Unique constraint | Same unique value twice | 409 Conflict + error body (A13). Only 1 record |  | High | Negative |  | 28 |
| **CRE-007** |  |  | ✓ |  |  | Any field | Double submit | Same POST twice in 1 second | 1 record created, or 409 for the 2nd |  | Medium | Boundary |  | 28 |
| **CRE-008** |  |  | ✓ |  |  | Any field | No create permission | Read-only user | 403 Forbidden + error body (A13) |  | High | Negative |  | 28 |

### 4.29. CRUD - Update (14 viewpoints)
* **Target / field type:** `PUT / PATCH`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **UPD-001** |  |  | ✓ |  |  | Any field | PUT full update | All fields | 200. All fields updated; updated_at changed |  | High | Positive |  | 29 |
| **UPD-002** |  |  | ✓ |  |  | Any field | PUT missing required field | Remove required field | 400 Bad Request + error body (A13). No change |  | High | Negative |  | 29 |
| **UPD-003** |  |  | ✓ |  |  | Any field | PUT id does not exist | Update missing record | 404 Not Found + error body (A13) |  | High | Negative |  | 29 |
| **UPD-004** |  |  | ✓ |  |  | Any field | PUT id in body differs from URL | body id=2, URL id=1 | URL wins or 400. Record 2 unchanged |  | Medium | Security |  | 29 |
| **UPD-005** |  |  | ✓ |  |  | Unique field | PUT unique conflict | Change to existing unique value | 409 Conflict + error body (A13) |  | Medium | Negative |  | 29 |
| **UPD-006** |  |  | ✓ |  |  | Any field | PUT read-only field | Send created_at | created_at NOT changed |  | Medium | Security |  | 29 |
| **UPD-007** |  |  | ✓ |  |  | Any field | PUT idempotent | Same PUT 5 times | Always 200; same final state |  | Medium | Positive |  | 29 |
| **UPD-008** |  |  | ✓ |  |  | Any field | PATCH partial update | Only 1 field | 200. Only that field changed |  | High | Positive |  | 29 |
| **UPD-009** |  |  | ✓ |  |  | Any field | PATCH empty body | {} | 400 Bad Request + error body (A13) |  | Medium | Negative | A11 | 29 |
| **UPD-010** |  |  | ✓ |  |  | Any field | PATCH invalid value | Invalid value | 400 Bad Request + error body (A13). No change |  | High | Negative |  | 29 |
| **UPD-011** |  |  | ✓ |  |  | Any field | PATCH unknown field | unknown_field | 200, ignored |  | Low | Negative | A10 | 29 |
| **UPD-012** |  |  | ✓ |  |  | Any field | PATCH id does not exist | Patch missing record | 404 Not Found + error body (A13) |  | High | Negative |  | 29 |
| **UPD-013** |  |  | ✓ |  |  | Any field | PATCH set required field to null | field: null | 400 Bad Request + error body (A13) (required); 200 (nullable) |  | Medium | Negative |  | 29 |
| **UPD-014** |  |  | ✓ |  |  | Any field | Concurrent update | 2 users update same record | Last write wins or 409/412 with ETag. No corrupted data |  | Low | Boundary |  | 29 |

### 4.30. CRUD - Delete (8 viewpoints)
* **Target / field type:** `DELETE`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **DEL-001** |  | ✓ |  |  |  | Any field | Delete success | Existing id | 204 (or 200) |  | High | Positive |  | 30 |
| **DEL-002** |  | ✓ |  |  |  | Any field | Record gone after delete | GET deleted id | 404 Not Found + error body (A13) |  | High | Positive |  | 30 |
| **DEL-003** |  | ✓ |  |  |  | Any field | Delete twice | Same DELETE again | 404 (or 204 if idempotent) – consistent |  | Medium | Negative |  | 30 |
| **DEL-004** |  | ✓ |  |  |  | Any field | Delete id does not exist | id=999999999 | 404 Not Found + error body (A13) |  | High | Negative |  | 30 |
| **DEL-005** |  | ✓ |  |  |  | Any field | Delete invalid id | id=abc | 400 Bad Request + error body (A13) |  | High | Negative |  | 30 |
| **DEL-006** |  | ✓ |  |  |  | Any field | Delete with related data | Record referenced by others | 409 (or cascade per spec). No orphan data |  | Medium | Negative |  | 30 |
| **DEL-007** |  | ✓ |  |  |  | Any field | Delete on collection | DELETE /items/ | 405. No data deleted |  | High | Security |  | 30 |
| **DEL-008** |  | ✓ |  |  |  | Any field | Not in list after delete | List after delete | Deleted record absent; total -1 |  | Medium | Positive |  | 30 |

### 4.31. Response validation (19 viewpoints)
* **Target / field type:** `Response`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **RESP-001** |  |  |  |  |  | Any field | Field names | Compare with spec | All spec fields exist with exact name/case; no undocumented field |  | High | Positive |  | 31 |
| **RESP-002** |  |  |  |  |  | Any field | Data types | Check each field | Types match spec |  | High | Positive |  | 31 |
| **RESP-003** |  |  |  |  |  | Any field | Required fields not null | Each record | Present and not null |  | High | Positive |  | 31 |
| **RESP-004** |  |  |  |  |  | Any field | null vs missing | Optional empty fields | Consistent: null OR omitted |  | Medium | Positive |  | 31 |
| **RESP-005** |  |  |  |  |  | Any field | Content-Type header | Response header | application/json; charset=utf-8 |  | High | Positive |  | 31 |
| **RESP-006** |  |  |  |  |  | Any field | Pagination metadata | total / limit / offset / next / previous | Present and correct |  | High | Positive |  | 31 |
| **RESP-007** |  |  |  |  |  | Any field | Empty list shape | Search with no match | results=[] (not null, not 404); total=0 |  | High | Boundary |  | 31 |
| **RESP-008** |  |  |  |  |  | Any field | Datetime format | All date fields | ISO 8601, same format and timezone everywhere |  | Medium | Positive |  | 31 |
| **RESP-009** |  |  |  |  |  | Any field | Number format | Decimal / money | No rounding error; fixed decimals; no scientific notation |  | Medium | Positive |  | 31 |
| **RESP-010** |  |  |  |  |  | Any field | Data matches DB | Compare with DB | Values and counts equal |  | High | Positive |  | 31 |
| **RESP-011** |  |  |  |  |  | Any field | Default sort order | No sort param | Stable, documented order |  | Medium | Positive |  | 31 |
| **RESP-012** |  |  |  |  |  | Any field | UTF-8 encoding | Vietnamese text | No mojibake |  | Medium | Positive |  | 31 |
| **RESP-013** |  |  |  |  |  | Any field | Error response format | Trigger a 4xx | {code, message, errors[{field,message}]}; clear message; JSON |  | High | Positive |  | 31 |
| **RESP-014** |  |  |  |  |  | Any field | Error message language | Several errors | One language only |  | Low | Positive |  | 31 |
| **RESP-015** |  |  |  |  |  | Any field | No sensitive data | Scan body | No password, hash, secret, other users' tokens, internal fields |  | High | Security |  | 31 |
| **RESP-016** |  |  |  |  |  | Any field | No stack trace | Trigger error | No stack trace, SQL, file path, framework version |  | High | Security |  | 31 |
| **RESP-017** |  |  |  |  |  | Any field | No 500 for abnormal input | Fuzz params with %00, %FF | Never 500; clear 4xx |  | High | Security |  | 31 |
| **RESP-018** |  |  |  |  |  | Any field | Cache headers | Sensitive data | Cache-Control: no-store / private |  | Low | Security |  | 31 |
| **RESP-019** |  |  |  |  |  | Any field | Compression | Accept-Encoding: gzip | Content-Encoding: gzip; decodes correctly |  | Low | Positive |  | 31 |

### 4.32. Security (18 viewpoints)
* **Target / field type:** `Injection / transport / abuse`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **SEC-001** | ✓ |  | ✓ | ✓ | ✓ | Any field | SQL injection in text input | ' OR 1=1 -- | Normal/empty result or 400. NOT all records. No SQL error |  | High | Security |  | 32 |
| **SEC-002** | ✓ |  | ✓ | ✓ | ✓ | Any field | SQL UNION injection | ' UNION SELECT null,null -- | No extra data; no SQL error |  | High | Security |  | 32 |
| **SEC-003** | ✓ |  | ✓ | ✓ | ✓ | Any field | Time-based SQL injection | '; WAITFOR DELAY '0:0:5' -- | Response time same as normal |  | High | Security |  | 32 |
| **SEC-004** | ✓ |  | ✓ | ✓ | ✓ | Any field | SQL injection in body field | JSON field = ' OR 1=1 -- | Stored literally or 400. No SQL executed |  | High | Security |  | 32 |
| **SEC-005** | ✓ |  | ✓ | ✓ | ✓ | Any field | NoSQL injection | {"\$ne":null} in JSON field | 400 Bad Request + error body (A13). No login / no data leak |  | High | Security |  | 32 |
| **SEC-006** | ✓ |  | ✓ | ✓ | ✓ | Any field | Reflected XSS | &lt;script&gt;alert(1)&lt;/script&gt; in query | Not reflected unescaped; response is JSON |  | High | Security |  | 32 |
| **SEC-007** | ✓ |  | ✓ | ✓ | ✓ | Any field | Stored XSS | &lt;img src=x onerror=alert(1)&gt; in body | Stored escaped or 400; never executed in UI |  | High | Security |  | 32 |
| **SEC-008** | ✓ |  | ✓ | ✓ | ✓ | Any field | Mass assignment | is_admin=true, role=admin, owner_id | Privileged fields ignored |  | High | Security |  | 32 |
| **SEC-009** | ✓ |  | ✓ | ✓ | ✓ | Any field | Path traversal in param | q=../../etc/passwd | Empty list or 400. No file content |  | Medium | Security |  | 32 |
| **SEC-010** | ✓ |  | ✓ | ✓ | ✓ | Any field | HTTP instead of HTTPS | http:// | Redirect to HTTPS or refused. No data over HTTP |  | High | Security |  | 32 |
| **SEC-011** | ✓ |  | ✓ | ✓ | ✓ | Any field | CORS - untrusted origin | Origin: https://evil.example.com | No Access-Control-Allow-Origin for it |  | High | Security |  | 32 |
| **SEC-012** | ✓ |  | ✓ | ✓ | ✓ | Any field | CORS - preflight | OPTIONS with Origin + Request-Method | Correct Allow-Origin / Methods / Headers |  | Medium | Security |  | 32 |
| **SEC-013** | ✓ |  | ✓ | ✓ | ✓ | Any field | Security headers | Check response headers | X-Content-Type-Options, HSTS present; no version leak |  | Medium | Security |  | 32 |
| **SEC-014** | ✓ |  | ✓ | ✓ | ✓ | Any field | Rate limit | 100 requests in 1 minute | 429 + Retry-After after threshold |  | High | Security | A14 | 32 |
| **SEC-015** | ✓ |  | ✓ | ✓ | ✓ | Any field | CRLF header injection | %0d%0a in value | No injected header; 200 or 400 |  | Low | Security |  | 32 |
| **SEC-016** | ✓ |  | ✓ | ✓ | ✓ | Any field | Oversized header | 16 KB header | 431 (or 400/401). Server stable |  | Low | Security |  | 32 |
| **SEC-017** | ✓ |  | ✓ | ✓ | ✓ | Any field | Oversized URL | URL &gt; 8 KB | 414 (or 400). Server stable |  | Low | Security |  | 32 |
| **SEC-018** | ✓ |  | ✓ | ✓ | ✓ | Any field | Credentials not logged / in URL | Login request | Credentials only in body; not in access logs |  | Medium | Security |  | 32 |

### 4.33. Non-functional (9 viewpoints)
* **Target / field type:** `Performance / reliability`

| VP ID | Query | Path | JSON | Form | Header | Applies when | Viewpoint | Test data / how to test | Expected result (default) | Alternative / note | Priority | Test Type | Assumption | Source |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **NFR-001** |  |  |  |  |  | Any field | Response time – normal | Normal list request | &lt; SLA (e.g. 2000 ms at p95) |  | Medium | Performance |  | 33 |
| **NFR-002** |  |  |  |  |  | Any field | Response time – max limit | limit = max on large data | &lt; SLA for large (e.g. 5000 ms) |  | Medium | Performance |  | 33 |
| **NFR-003** |  |  |  |  |  | Any field | Response time – deep offset | offset = 100000 | Within SLA; no timeout |  | Low | Performance |  | 33 |
| **NFR-004** |  |  |  |  |  | Any field | Response time – search | Search on large data | &lt; SLA |  | Medium | Performance |  | 33 |
| **NFR-005** |  |  |  |  |  | Any field | Concurrent requests | 50 concurrent valid requests | All 200; correct data; no 5xx |  | Medium | Performance |  | 33 |
| **NFR-006** |  |  |  |  |  | Any field | Race condition on create | 2 simultaneous POST with same unique value | 1 succeeds (201), 1 gets 409; no duplicate |  | Medium | Performance |  | 33 |
| **NFR-007** |  |  |  |  |  | Any field | Timeout handling | Slow dependency | 504/503 + clear message; no hang |  | Low | Performance |  | 33 |
| **NFR-008** |  |  |  |  |  | Any field | Recovers after errors | 20 invalid requests then valid one | Valid request returns 200 |  | Low | Performance |  | 33 |
| **NFR-009** |  |  |  |  |  | Any field | Service unavailable | Stop DB / dependency | 503 + JSON error; no stack trace |  | Low | Performance |  | 33 |

