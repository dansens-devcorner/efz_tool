📊 Excel → CSV Guide (for the user)

This part is important, otherwise your script will break.

✅ Required format in Excel

Your Excel file must look like this:

Name	MemberID	Age
Max Mustermann	1234	27
Peter Müller	54321	18
🔴 Only keep these 3 columns:
Column A: Name
Column B: Member ID
Column C: Age

👉 Delete EVERYTHING else:

No extra columns
No empty columns in between
No headers (optional, but safer to remove)
🧹 Clean your data

Before exporting:

Remove:
Empty rows
Formatting (colors, merged cells)
Formulas (convert to values if needed)
Make sure:
Member IDs are pure numbers (no spaces!)
Age is a number
No weird characters
💾 Export as CSV (VERY IMPORTANT)
In Excel:
Click File
Click Save As

Choose:

CSV UTF-8 (Comma delimited) (*.csv)

Save file as:

input.csv

Move it into:

/input/input.csv
⚠️ Important for Germany/Europe

Excel often uses semicolon (;) automatically — which is GOOD.

If not:

Open CSV in editor (Notepad++)

Ensure it looks like:

Max Mustermann;1234;27

NOT:

Max Mustermann,1234,27
🧪 Example final CSV
Max Mustermann;1234;27
Peter Müller;54321;18
🚀 If you want improvements next

You’re already close to a production tool. I can help you:

Add automatic Excel → CSV conversion
Add a GUI (drag & drop file)
Export results as Excel instead of .txt
Add logging + stats (how many valid/invalid)

Just tell me 👍