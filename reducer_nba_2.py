# reducer_nba_3.py
import sys
from collections import defaultdict

# (player, zone) → [FGM, attempts]
stats = defaultdict(lambda: [0, 0])

for line in sys.stdin:
    player, zone, fgm, count = line.strip().split('\t')
    fgm = int(fgm)
    count = int(count)
    key = (player, int(zone))
    stats[key][0] += fgm
    stats[key][1] += count

# Output: player \t zone \t hit_rate \t attempts
for (player, zone), (fgm_total, shot_total) in stats.items():
    hit_rate = fgm_total / shot_total if shot_total > 0 else 0
    print(f"{player}\tZone {zone}\t{hit_rate:.3f}\t{shot_total}")
