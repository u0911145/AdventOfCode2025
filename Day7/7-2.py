import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.genfromtxt(filename, dtype=str, delimiter=1)

out = (data[0] == 'S').astype(np.int64)
for row in data:
    for point in np.where(out)[0]:
        if row[point] == '^':
            out[[point-1, point+1]] += out[point]
            out[point] = 0
print(out.sum())