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
        if len(row) >= 36:
            vyear = clean(row[35])
            vmake = clean(row[7])
            vbody = clean(row[6])
            if vyear and vmake and vbody:
                # 👇 Output only ONE tab here!
                print(f"{vyear} {vmake} {vbody}\t1")
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        continue

