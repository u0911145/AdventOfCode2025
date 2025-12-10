import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.loadtxt(filename, dtype=int, delimiter=',')

distance_matrix = np.linalg.norm(data[:, None] - data[None, :], axis=-1)
distance_matrix[np.tril_indices_from(distance_matrix)] = np.inf
nums = np.array([[x // distance_matrix.shape[0], x % distance_matrix.shape[0]] for x in np.argsort(distance_matrix.flatten())[:10]])
print(nums)
print(distance_matrix[nums[:, 0], nums[:, 1]])
print(np.sort(distance_matrix.flatten())[:10])
for num in nums:
    print(data[num[0]], data[num[1]])
adjacency_matrix = np.zeros((distance_matrix.shape[0], distance_matrix.shape[0]), dtype=int)
adjacency_matrix[nums[:, 0], nums[:, 1]] = 1
adjacency_matrix[nums[:, 1], nums[:, 0]] = 1

points = np.arange(distance_matrix.shape[0])
groups = np.array([])
while points.size > 0:
    print("Points", points)
    adjacent = np.array([points[0]])
    i = 0
    while i < adjacent.size:
        a = adjacent[i]
        points = np.delete(points, np.where(points == a)[0])
        new_adjacent = np.unique(np.append(adjacent, np.where(adjacency_matrix[a])[0]))
        if (new_adjacent.size == adjacent.size):
            print("Adjacent", adjacent)
            groups = np.append(groups, adjacent.size)
            break
        adjacent = new_adjacent
        i += 1
print("Groups", groups)
print(np.sort(groups)[-3:])
print(int(np.sort(groups)[-3:].prod()))