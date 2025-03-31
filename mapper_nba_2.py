# mapper_nba_3.py
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # Skip header
'''
1 - under the hoop, heavily contested
2 - mid-range, moderately contested, inside 3-line
3 - wide open 3 pointers, lightly contested
4 - heavily contested 3 pointer, fast break open layup, buzzer beater toss up, misc.
'''
def assign_zone(shot_dist, close_def_dist, shot_clock):
    if shot_dist <= 10 and close_def_dist <= 3 and shot_clock >= 15:
        return 1
    elif 10 < shot_dist <= 20 and 3 < close_def_dist <= 6 and 7 < shot_clock < 15:
        return 2
    elif shot_dist > 20 and close_def_dist > 6 and shot_clock <= 7:
        return 3
    else:
        return 4

for row in reader:
    try:
        player = row[19]
        shot_dist = float(row[11])
        close_def = float(row[16])
        shot_clock = float(row[9])
        fgm = int(row[17])
        
        zone = assign_zone(shot_dist, close_def, shot_clock)
        print(f"{player}\t{zone}\t{fgm}\t1")
    except:
        continue
