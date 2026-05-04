# EFZ Checker – User Instructions


If you don't know, how to run a python script, go and find someone that knows to help you. 

## 📁 Setup

Make sure your folder structure looks like this:

```
project/
│
├── main.py
├── input/
├── efzFile/
│   └── llist.csv
└── output/
```

---

## 📊 Prepare Input File (from Excel)

You must create `input.csv` manually from Excel.

### 1. Format your Excel file

Only keep these 3 columns:

| Name           | MemberID | Age |
| -------------- | -------- | --- |
| Max Mustermann | 1234     | 27  |
| Peter Muster   | 54321    | 18  |

### Important:

* Column order must be:

  1. Name
  2. Member ID
  3. Age
* Delete all other columns
* Remove empty rows
* No merged cells or formatting
* Member ID must be 4–5 digits (numbers only)
* Age must be a number

---

### 2. Export as CSV

In Excel:

1. Click **File → Save As**
2. Choose:

   ```
   CSV UTF-8 (Comma delimited) (*.csv)
   ```
3. Save as:

   ```
   input.csv
   ```
4. Move the file to:

   ```
   input/input.csv
   ```

---

### 3. Check delimiter (VERY IMPORTANT)

Open the file in a text editor.

It must look like this:

```
Max Mustermann;1234;27
Peter Muster;54321;18
```

If you see commas instead:

```
Max Mustermann,1234,27
```

Replace them with semicolons (`;`) or export again with correct regional settings.

---

## 📊 Reference File (from eVewa)

Get the full export from eVewa for all members(Excel mit beziehungen).
Export it as csv. No need to sanitize the data this time.

save as efzFile/list.csv



## ▶️ Run the Script

Open a terminal in the project folder and run:

```
python main.py
```

---

## 📄 Output

The result will be written to:

```
output/report.txt
```

---

## 📅 What gets checked

* Only people aged **16 or older**
* Member ID is matched against `list.csv`
* Script searches for **"Führungszeugnis"**
* Latest date in matching entries is used

---

## ✅ Result Types

### Valid:

```
Max Mustermann(1234), 27 hat ein EFZ gültig bis 26.04.27
```

### Invalid:

```
Max Mustermann(1234), 18 hat kein EFZ
Peter Müller(54321), 29 hat ein EFZ, welches zum 14.02.2024 abgelaufen ist
```

### Errors:

* Only shown if something could not be processed
* Under-16 entries are NOT listed here

---

## 📌 Check Date

EFZ validity is checked against:

```
2026-05-26
```

(Defined inside `main.py` and can be changed there)

---

## ⚠️ Notes

* Multiple EFZ entries per person are supported
* The **latest date always counts**
* People under 16 are ignored completely
