"""
EFZ Checker Script
------------------

This script compares a list of members (input/input.csv) against a reference file
(efzFile/list.csv) to determine whether a valid "Führungszeugnis" (EFZ) exists.
Vibecoded the shit out of this to quickly get a working tool, bear with me.

OUTPUT:
- output/report.txt

LOGIC:
- Only members with age >= 16 are checked
- A member is VALID if:
    - At least one row in llist.csv contains:
        - their member ID
        - the term "Führungszeugnis"
    - AND the latest date found in those rows is >= 2026-05-26

- Otherwise, they are marked INVALID
- afterwards, a report is created in output/report.txt

FOLDER STRUCTURE:
main.py
input/input.csv
efzFile/llist.csv
output/report.txt
"""

import csv
import os
from datetime import datetime

# === CONFIGURATION ===

# Base directory (where main.py is located)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
INPUT_FILE = os.path.join(BASE_DIR, "input", "input.csv")
EFZ_FILE = os.path.join(BASE_DIR, "efzFile", "list.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "output", "report.txt")

# Minimum valid EFZ date
DATE_THRESHOLD = datetime.strptime("2026-05-26", "%Y-%m-%d")


# === HELPER FUNCTIONS ===

def extract_member_id_from_row(row):
    """
    Extracts a member ID from a row.

    A valid member ID is:
    - numeric
    - length 4 or 5 digits

    Returns:
        str or None
    """
    for item in row:
        item = item.strip()
        if item.isdigit() and len(item) in [4, 5]:
            return item
    return None


def extract_dates_from_row(row):
    """
    Extracts all valid dates (YYYY-MM-DD) from a row.

    Returns:
        list of datetime objects
    """
    dates = []
    for item in row:
        item = item.strip()
        try:
            dates.append(datetime.strptime(item, "%Y-%m-%d"))
        except:
            continue
    return dates


# === LOAD EFZ REFERENCE DATA ===

efz_data = {}

with open(EFZ_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')  # IMPORTANT: semicolon CSV

    for row in reader:
        member_id = extract_member_id_from_row(row)

        if not member_id:
            continue

        # Store all rows per member ID
        if member_id not in efz_data:
            efz_data[member_id] = []

        efz_data[member_id].append(row)


# === PROCESS INPUT FILE ===

valid_list = []
invalid_list = []
error_list = []

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')  # IMPORTANT: semicolon CSV

    for row in reader:
        try:
            # Extract relevant columns
            name = row[0].strip()
            member_id = row[1].strip()
            age = int(row[2])

            # Skip under 16
            if age < 16:
                continue

            # Get EFZ rows for this member
            rows = efz_data.get(member_id, [])

            # Filter rows containing "Führungszeugnis" (case insensitive)
            efz_rows = [
                r for r in rows
                if any("führungszeugnis" in cell.lower() for cell in r)
            ]

            # No EFZ found
            if not efz_rows:
                invalid_list.append(f"{name}({member_id}), {age} hat kein EFZ")
                continue

            # Find latest date across all EFZ rows
            latest_date = None

            for r in efz_rows:
                dates = extract_dates_from_row(r)

                if dates:
                    max_date = max(dates)
                    if not latest_date or max_date > latest_date:
                        latest_date = max_date

            # No valid date found
            if not latest_date:
                invalid_list.append(f"{name}({member_id}), {age} hat kein gültiges Datum im EFZ")
                continue

            # Check validity
            if latest_date < DATE_THRESHOLD:
                formatted = latest_date.strftime("%d.%m.%Y")
                invalid_list.append(
                    f"{name}({member_id}), {age} hat ein EFZ, welches zum {formatted} abgelaufen ist"
                )
            else:
                formatted = latest_date.strftime("%d.%m.%y")
                valid_list.append(
                    f"{name}({member_id}), {age} hat ein EFZ gültig bis {formatted}"
                )

        except Exception as e:
            error_list.append(f"Fehler bei Zeile {row}: {e}")


# === WRITE OUTPUT REPORT ===

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("=== GÜLTIGE EFZ ===\n")
    for line in valid_list:
        f.write(line + "\n")

    f.write("\n=== UNGÜLTIG / FEHLT ===\n")
    for line in invalid_list:
        f.write(line + "\n")

    f.write("\n=== FEHLER ===\n")
    for line in error_list:
        f.write(line + "\n")

print("Report erstellt:", OUTPUT_FILE)