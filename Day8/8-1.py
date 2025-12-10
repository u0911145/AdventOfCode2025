import sys
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else exit('Please provide an input file.')
data = np.loadtxt(filename, dtype=int, delimiter=',')
distance_matrix = np.linalg.norm(data[:, None] - data[None, :], axis=-1)
np.fill_diagonal(distance_matrix, np.inf)
nums = np.array([[x % distance_matrix.shape[0], x // distance_matrix.shape[0]] for x in np.argsort(distance_matrix.flatten())[:10]])
adjacency_matrix = np.zeros_like(distance_matrix)
adjacency_matrix[nums[:, 0], nums[:, 1]] = 1
adjacency_matrix[nums[:, 1], nums[:, 0]] = 1
print(adjacency_matrix)