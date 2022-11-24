# Calcular um sistema linear no Python 3
import numpy as np
# Forma Ax=b
A = np.array([[1,2],[3,5]])
B = np.array([[5],[4]])
x = np.linalg.solve(A,B)
x


