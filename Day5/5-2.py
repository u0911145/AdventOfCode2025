import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = open(filename).read().split("\n\n")
ranges = np.array([[int(x) for x in line.split("-")] for line in data[0].splitlines()])
ranges.sort(axis=0)

count = 0
nr = ranges[0]
for r in ranges:
    if nr[1] < r[0]:
        count += nr[1] - nr[0] + 1
        nr = r
    else:
        if nr[1] < r[1]:
            nr[1] = r[1]
count += nr[1] - nr[0] + 1
print(count)