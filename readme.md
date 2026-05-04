# EFZ Checker – User Instructions

If you don't know how to run a Python script, ask someone who does.

---

## 📁 Setup

Project structure:

```
project/
│
├── main.py
├── input/
├── efzFile/
└── output/
```

⚠️ IMPORTANT:
- Each folder (`input/`, `efzFile/`) must contain EXACTLY ONE CSV file
- If there are 0 or more than 1 CSV files → script will fail

---

## 📊 Input File (Excel → CSV)

### Step 1: Excel format

Keep ONLY these columns:

| Name | MemberID | Age |
|------|----------|-----|
| Max Mustermann | 1234 | 27 |
| Peter Muster | 54321 | 18 |

Rules:
- Column order must be: Name → MemberID → Age
- No extra columns
- No empty rows
- No formatting / merged cells
- MemberID = 4–5 digit number only
- Age = number

---

### Step 2: Export CSV

Excel:
- File → Save As
- Format: CSV UTF-8 (Comma delimited)
- Save into: `input/`

No specific filename needed.

---

### Step 3: IMPORTANT delimiter check

File MUST look like this:

```
Max Mustermann;1234;27
Peter Muster;54321;18
```

If you see commas:

```
Max Mustermann,1234,27
```

→ fix export settings or replace with `;`

---

## 📊 Reference File (eVewa export)

- Export full dataset from eVewa (Excel export)
- Save as CSV
- Put into:
  `efzFile/`

No manual cleanup required.

---

## ▶️ Run Script

```
python main.py
```

---

## 📄 Output

```
output/report.txt
```

---

## 📅 What gets checked

- Only people aged ≥ 16
- MemberID matched against reference CSV
- Searches for "Führungszeugnis"
- Uses latest found date

---

## ✅ Results

### VALID
```
Max Mustermann(1234), 27 hat ein EFZ gültig bis 26.04.27
```

### INVALID
```
Max Mustermann(1234), 18 hat kein EFZ
Peter Muster(54321), 29 hat ein EFZ, welches zum 14.02.2024 abgelaufen ist
```

### ERRORS
- Only processing issues
- Under-16 entries are ignored (not reported)

---

## 📌 Check Date

```
2026-05-26
```

Defined in `main.py` (editable)

---

## ⚠️ Notes

- Multiple EFZ entries per person supported
- Latest date always wins
- Script fails if:
  - no CSV found in folder
  - more than one CSV found in folder