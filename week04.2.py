#lets try to make a matrix addition

#lets first initialize the size of the matrix
n,m = map(int,input().split())
mat1 = []
for i in range(n):
      mat1.append(list(map(int,input().split())))

mat2 = []
for i in range(n):
      mat2.append(list(map(int,input().split())))

mat3 = []
for i in range(n):
      mat3.append([0]*m)

print("Matrix after Addition: ")
#Adddition
for i in range(n):
      for j in range(m):
            mat3[i][j]=mat1[i][j]+mat2[i][j]

#note even for printing our matrix we want loop
for i in range(n):
      for j in range(m):
            print(mat3[i][j], end=" ")
      print()

print("Matrix after Multiplication: ")
#Multiplication
mat4 = []
for i in range(n):
      mat4.append([0]*m)

for i in range(n):
      for j in range(m):
            for k in range(n):
                  mat4[i][j]=mat4[i][j]+(mat1[i][k]*mat2[k][j])
for i in range(n):
      for j in range(m):
            print(mat4[i][j], end=" ")
      print()