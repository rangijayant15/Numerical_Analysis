import numpy as np
size=int(input("enter the size of matrix  -->"))

matrix=np.zeros((size,size))

for i in range (0,size):
  for j in range (0,size):
	print ('entry in row: ',i+1,' column: ',j+1)
	matrix[i][j] = int(input())

def crout(mtr,sze):
	L=np.zeros((size,size))
	U=np.zeros((size,size))
	for j in range(sze):
		
		U[j][j] = 1             # set the j,j-th entry of U to 1
		for i in range(j, sze):  # starting at L[j][j], solve j-th column of L
			a = float(mtr[i][j])
			for k in range(j):
				a -= L[i][k]*U[k][j]
			L[i][j] = a
		for i in range(j+1, sze):# starting at U[j][j+1], solve j-th row of U
			U2 = float(mtr[j][i])
			for k in range(j):
				U2 -= L[j][k]*U[k][i]
			if int(L[j][j]) == 0:
				L[j][j] = e-40
			U[j][i] = U2/L[j][j]
	return [L, U]

		
print("LU decompositon is :\n")
print("L is \n" + str(crout(matrix,size)[0]))
print("U is \n" + str(crout(matrix,size)[1]))
