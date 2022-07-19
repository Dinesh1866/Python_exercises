'''Array Problems'''

# 1. Input and Output Array
'''You are given an integer N representing the size of the array and N
elements of the array. Your task is to input the array and output it.'''
T = int(input())
while T>0:
  N =int(input())
  arr = list(map(int,input().split()))
  for i in range(N):
    print(arr[i],end=" ")
  print()
  T -=1



# 2. Multiplication of Array Elements
'''he is giving you this problem.
You are provided with the size of the array represented by N and N array elements. 
You need to output the multiplication of all the elements'''
T =int(input())
while T>0:
  n = int(input())
  arr = list(map(int,input().split()))
  value = 1
  for ele in range(n):
    value *=arr[ele]
  print(value)
  T -= 1



# 3. Find Even and Odd element