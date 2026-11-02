import sys
from collections import Counter

logs = sys.argv[1]

with open(logs) as f:
    lines = f.readlines()

print("Total lines:", len(lines))

dict = Counter()
for i in lines:
    fields = i.split()

    if len(fields) >= 6:
        key = fields[5]
        dict[key] += 1

print("Top1:")
for i, n in dict.most_common(1):
    print(i, n)
