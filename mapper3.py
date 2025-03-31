#!/usr/bin/env python3
import sys
import csv

def clean(s):
    return s.strip().upper().replace('\r', '').replace('\n', '').replace('\t', ' ')

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        if row[0] == "Summons Number":
            continue  # skip header
        if len(row) >= 25:
            county = clean(row[21])
            street = clean(row[24])
            if county and street:
                key = f"{county} {street}"  # use space in key
                print(f"{key}\t1")          # only one tab in total
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        continue
