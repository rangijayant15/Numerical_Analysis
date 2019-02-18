import numpy as np
from math import sqrt

def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)
size=int(input("enter the size of matrix  -->"))

matrix=np.zeros((size,size))

for i in range (0,size):
  for j in range (0,size):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
    

def cholesky(mtr,sze):
	mat=np.zeros((size,size))
	for i in range(sze):
		for j in range(i+1):
			sum_=0
			if j==i:
				for k in range(j):
					sum_=sum_+(mat[j][k]**2)
				mat[j][j]= sqrt(mtr[j][j]-sum_)
			else:
				for k in range(j):
					sum_=sum_+(mat[i][k] * mat[j][k])
				mat[i][j]=(mtr[i][j] - sum_)/mat[j][j]
	return mat
if is_pos_def(matrix):
	print("lower triangular matrix is : \n")
	print(cholesky(matrix,size))
	print("tarnspose of lower triangular matrix is :\n")
	print(cholesky(matrix,size).T)							
else:
	print("matrix is not positive defininte\n")	