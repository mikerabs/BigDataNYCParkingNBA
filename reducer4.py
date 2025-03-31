#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")
    
    if len(parts) != 2:
        continue

    key = f"{parts[0]}"
    try:
        count = int(parts[1])
    except ValueError:
        continue

    if key == current_key:
        current_count += count
    else:
        if current_key:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = count

if current_key:
    print(f"{current_key}\t{current_count}")
