import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.loadtxt(filename, dtype=int, delimiter=',')

distance_matrix = np.linalg.norm(data[:, None] - data[None, :], axis=-1)
distance_matrix[np.tril_indices_from(distance_matrix)] = np.inf
nums = np.array([[x // distance_matrix.shape[0], x % distance_matrix.shape[0]] for x in np.argsort(distance_matrix.flatten())])
print(nums)

l = 0
r = distance_matrix.shape[0]
while l < r:
    edge = (l + r) // 2
    adjacency_matrix = np.zeros((distance_matrix.shape[0], distance_matrix.shape[0]), dtype=int)
    adjacency_matrix[nums[:edge, 0], nums[:edge, 1]] = 1
    adjacency_matrix[nums[:edge, 1], nums[:edge, 0]] = 1
    
    adjacent = np.array([0])
    i = 0
    while i < adjacent.size:
        a = adjacent[i]
        for num in np.where(adjacency_matrix[a])[0]:
            if num not in adjacent:
                adjacent = np.append(adjacent, num)
        i += 1
    print("Edge",edge,"Size",adjacent.size)
    if adjacent.size < distance_matrix.shape[0]:
        l = edge + 1
    else:
        r = edge
    print("l",l,"r",r)
print(data[nums[r, 0]][0])
print(data[nums[r, 1]][0])
print(data[nums[r, 0]][0] * data[nums[r, 1]][0])