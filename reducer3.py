#!/usr/bin/env python3
import sys

print("Reducer started...", file=sys.stderr)

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        key, count = line.rsplit("\t", 1)
        count = int(count)
    except ValueError:
        continue

    if key == current_key:
        current_count += count
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = count

if current_key is not None:
    print(f"{current_key}\t{current_count}")
