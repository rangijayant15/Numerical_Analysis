import numpy as np
size=int(input("enter the size of matrix  -->"))

matrix=np.zeros((size,size))

for i in range (0,size):
  for j in range (0,size):
	print ('entry in row: ',i+1,' column: ',j+1)
	matrix[i][j] = int(input())

def doolittle(mtr,sze):
	L=np.zeros((size,size))
	U=np.zeros((size,size))
	for i in range(sze):
		for k in range(i,sze):
			sum_=0
			for j in range(i):
				sum_=sum_+(L[i][j]*U[j][k])
			U[i][k] = mtr[i][k] - sum_
		for k in range(i,sze):
			if i==k:
				L[i][i]=1
			else:
				sum_=0
				for j in range(0,i):
					sum_=sum_+(L[k][j]*U[j][i])
				L[k][i] = (mtr[k][i] - sum_)/U[i][i]	
	return [L,U]
	
print("LU decompositon is :\n")
print("L is \n" + str(doolittle(matrix,size)[0]))
print("U is \n" + str(doolittle(matrix,size)[1]))				
