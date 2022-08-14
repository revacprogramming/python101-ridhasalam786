def READ_DATA(r,c,matrix):
    for i in range(m):
        for j in range(n):
            matrix[i][j]=int(input())   

import numpy
m= int(input("\n Enter the row size of M "))
n=int(input("\n Enter the column size of N"))

matrix=numpy.ndarray(shape=(m,n), dtype=int)         #creating an array
print("size: \n",matrix.size)
print("shape: \n",matrix.shape)
print("Dimensions: \n",matrix.ndim)
print("\n Enter %d elements of %d x %d matrix" %(m*n,m,n))
READ_DATA(m,n,matrix)
print("\n %d x %d matrix are:"%(m,n))
print(matrix)
print("Diagonal Elements of matrix: ")
dia=matrix.diagonal()
print(dia)
r=int(input("Enter row number to display: "))
c=int(input("Enter column number to display: "))
row = matrix[r, :]
print(row)

# get index=2 along axis=1 - this means a column in 2D
col = matrix[:, c]
print(col)

