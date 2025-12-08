import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.array([[r[0], ''.join(r[1:])] for r in np.roll(np.genfromtxt(filename, dtype=str, delimiter=1).transpose(), shift=1, axis=1)])
data = data[:, 1].reshape((-1, 3))
print(data)
# op = ""
# count = 0
# temp = 0
# for line in data:
#     if (line[1].isspace()):
#         count += temp
#         temp = 0
#     else:
#         if not line[0].isspace():
#             op = line[0]
#         num = int(line[1])
#         temp = num if temp == 0 else temp * num if op == '*' else temp + num