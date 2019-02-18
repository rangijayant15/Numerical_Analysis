import numpy as np
size=int(input("enter the size of matrix  -->"))

A=np.zeros((size,size))
b=np.zeros((size,1))
X=np.zeros((size,1))
print("Enter the A matrix for Ax=b\n")
for i in range (0,size):
  for j in range (0,size):
	print ('entry in row: ',i+1,' column: ',j+1)
	A[i][j] = int(input())

print("Enter the b vector\n")
for i in range(0,size):
	print('enter in row: ',i+1)
	b[i]=int(input())

print("Enter the initial x vector\n")
for i in range(0,size):
	print('enter in row: ',i+1)
	X[i]=int(input())	

def gauss_seidel(a,x,b,sze):
	x_initial=x
	L=np.zeros((sze,sze))
	U=np.zeros((sze,sze))
	for i in range(sze):
		for j in range(i+1):
			L[i][j]=a[i][j]
	U=a-L
	while(np.linalg.norm((np.matmul(a,x_initial)-b),2)>0.0001):
		x_initial=np.matmul(np.linalg.inv(L),b-np.matmul(U,x_initial))
	return x_initial		

print("Answer is : ")
print(gauss_seidel(A,X,b,size))	