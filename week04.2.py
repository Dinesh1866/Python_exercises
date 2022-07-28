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




'''Scalar Multiplication'''
m,n,k = map(int,input().split())
mat1 = []
for i in range(n):
  mat1.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    print(mat1[i][j]*k,end=" ")
  print()




'''Lower and Upper Triangular Matrices'''
#UpperTriangle
def UpperTriangle(mat1,n,m):
  for i in range(n):
    for j in range(m):
      if i>j:
        print("0", end=" ")
      else:
        print(mat1[i][j],end=" ")
    print()
    
    
#LowerTriangle
def LowerTriangle(mat1,n,m):
  for i in range(n):
    for j in range(m):
      if i<j:
        print("0", end=" ")
      else:
        print(mat1[i][j],end=" ")
    print()


def main():
  n,m = map(int,input().split())
  mat1 = []
  for i in range(n):
    mat1.append(list(map(int,input().split())))
  LowerTriangle(mat1,n,m)
  UpperTriangle(mat1,n,m)
    
if __name__ =="__main__":
  main()



'''Rearrange the Array'''
def rearrange(arr, n):
  temp = n*[None]
  small, large = 0, n-1
  flag = True
  for i in range(n):
    if flag is True:
      temp[i] = arr[large]
      large -= 1
    else:
      temp[i] = arr[small]
      small += 1
    flag = bool(1-flag)
  for i in range(n):
    arr[i] = temp[i]
  return(arr)
 
def printarr(arr,n):
  for i in range(n):
    print(arr[i],end=" ")
  print()


def main():
  T = int(input())
  while T>0:
    N = int(input())
    arr = list(map(int,input().split()))
    n= len(arr)
    rearrange(arr,n)
    printarr(arr,n)
    T-=1
    

if __name__=="__main__":
  main()