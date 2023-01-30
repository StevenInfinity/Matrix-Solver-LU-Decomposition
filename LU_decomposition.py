#Modules
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve


#Defining matrix A and B
l_a1 = list(map(int,input("Enter row 1 of matrix A: ").strip().split()))[:10]
l_a2 = list(map(int,input("Enter row 2 of matrix A: ").strip().split()))[:10]
l_a3 = list(map(int,input("Enter row 3 of matrix A: ").strip().split()))[:10]
l_a4 = list(map(int,input("Enter row 4 of matrix A: ").strip().split()))[:10]
l_a5 = list(map(int,input("Enter row 5 of matrix A: ").strip().split()))[:10]
l_a6 = list(map(int,input("Enter row 6 of matrix A: ").strip().split()))[:10]
l_a7 = list(map(int,input("Enter row 7 of matrix A: ").strip().split()))[:10]
l_a8 = list(map(int,input("Enter row 8 of matrix A: ").strip().split()))[:10]
l_a9 = list(map(int,input("Enter row 9 of matrix A: ").strip().split()))[:10]
l_a10 = list(map(int,input("Enter row 10 of matrix A: ").strip().split()))[:10]
l_b = list(map(int,input("Enter of matrix B: ").strip().split()))[:10]

A = np.array([l_a1, l_a2, l_a3, l_a4, l_a5, l_a6, l_a7, l_a8, l_a9, l_a10])
B = np.array(l_b)
B.shape = (10,1)


#Matrix factorization
P, L, U = lu(A)

print('The Lower Triangular matrix is : ')
print(L)
print()
print('The Upper Triangular matrix is : ')
print(U)
print()
print("The values of X matrix are : ")

#Factorization
LU, p = lu_factor(A)

#Solution
mat_x = lu_solve((LU, p), B)
print(mat_x)

