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
'''You are given an array of size N, containing N integers. person is asking you to print all the even elements 
in the first line and all odd elements in the second line.The array will contain at least one even and one odd element.'''
n = int(input())
arr = list(map(int,input().split()))
for ele in range(n):
  if arr[ele]%2==0:
    print(arr[ele],end=" ")
print()
for ele in range(n):
  if arr[ele]%2!=0:
    print(arr[ele],end=" ")
print()



# 4. Minimum House Number
'''person lives in a colony, where N houses are built in a single row numbered from 0 to N - 1.
The first house has a house number 0, the second house has a house number 1 and so on, 
every house pays some rent at the end of the month.
Help PrepBuddy in finding out the house number of the house paying the minimum rent.
Note: All house rents are unique.'''
T = int(input())
while T>0:
  N= int(input())
  arr = list(map(int,input().split()))
  maxi = 1001
  n = 0
  for i in range(N):
    if arr[i]<maxi:
      maxi = arr[i]
      n = i
  print(n)
  T -=1


