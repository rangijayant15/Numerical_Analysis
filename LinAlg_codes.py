import numpy as np 
from math import sqrt

while(True):
	print("which method you want to check:\n")
	print("FOR CROUT METHOD ENTER 1 \n")
	print("FOR DOOLITTLE METHOD ENTER 2 \n")
	print("FOR CHOLESKY METHOD ENTER 3 \n")
	print("FOR GAUSS_JACOBI METHOD ENTER 4 \n")
	print("FOR GAUSS_SEIDEL METHOD ENTER 5 \n")
	choice=int(input("CHOICE-->"))
	if choice==1:
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

	if choice==2:
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

	if choice==3:
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

	if choice==4:

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

	if choice==5:

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






	