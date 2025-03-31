# mapper1.py
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header

for row in reader:
    shooter = row[19]  # player_name
    defender = row[14]  # CLOSEST_DEFENDER
    fgm = int(row[17])  # FGM

    print(f"{shooter}\t{defender}\t{fgm}\t1")
