#!/usr/bin/env python3
import sys
import csv

#Q: When are tickets most likely to be issued?

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        if row[0] == "Summons Number":
            continue  # skip header
        if len(row) >= 25:
            date = row[4].strip().upper()
            splitdate = date.split("/")
            month = splitdate[0]
            if date:
                print(f"{month}\t1")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        continue
