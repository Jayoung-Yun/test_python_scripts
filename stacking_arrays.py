import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('A = ')
print(A)

B=np.hstack([A,A])
print('B = ')
print(B)

C=np.vstack([A,A])
print('C = ')
print(C)

