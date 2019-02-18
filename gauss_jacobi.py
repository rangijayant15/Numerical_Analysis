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

def gauss_jacobi(a,x,b,sze):
	x_initial=x
	D=np.zeros((sze,sze))
	R=np.zeros((sze,sze))
	for i in range(sze):
		D[i][i]=a[i][i]
	R=a-D	
	while(np.linalg.norm((np.matmul(a,x_initial)-b),2)>0.0001):
		x_initial=np.matmul(np.linalg.inv(D),b-np.matmul(R,x_initial))
	return x_initial

print("Answer is : ")
print(gauss_jacobi(A,X,b,size))		



