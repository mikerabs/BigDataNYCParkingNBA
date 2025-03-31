# reducer_nba_1.py
import sys
from collections import defaultdict

# Dictionary: (shooter, defender) -> [FGM, attempts]
stats = defaultdict(lambda: [0, 0])

for line in sys.stdin:
    shooter, defender, fgm, count = line.strip().split('\t')
    fgm = int(fgm)
    count = int(count)

    key = (shooter, defender)
    stats[key][0] += fgm
    stats[key][1] += count

# Output only if attempts >= 8
for (shooter, defender), (fgm_total, shot_total) in stats.items():
    if shot_total >= 8:
        hit_rate = fgm_total / shot_total
        print(f"{shooter}\t{defender}\t{hit_rate:.3f}\t{shot_total}")
