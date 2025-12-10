import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.genfromtxt(filename, dtype=str, delimiter=1)

count = 0
out = (data[0] == 'S').astype(int)
for row in data:
    for point in np.where(out)[0]:
        if row[point] == '^':
            count += 1
            out[[point-1, point, point+1]] = [1, 0, 1]
print(count)