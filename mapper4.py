#!/usr/bin/env python3
import sys
import csv

#Q: Which color of the vehicle is most likely to get a ticket?

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        if row[0] == "Summons Number":
            continue  # skip header
        if len(row) >= 25:
            vcolor = row[33].strip().upper()
            if vcolor:
                print(f"{vcolor}\t1")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        continue
