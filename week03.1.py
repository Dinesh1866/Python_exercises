'''Arrays'''
#getting input as array or list

# 1. we can use for loop
arr = []
for ele in input().split():
      arr.append(int(ele))
for i in range(len(arr)):
      print(arr[i],end=" ")


# 2. we can get it through map function
arr2 = list(map(int,input().split()))
for i in range(len(arr2)):
      print(arr2[i],end=" ")



'''Min and Max'''

#based on what i know
T = int(input())
while T>0:
      N = int(input())
      arr = list(map(int,input().split()))
      if len(arr)== N:
            print(min(arr),max(arr))
      T -=1

#try based on what they thought
#use for loop and if statement
T = int(input())
while T>0:
      N = int(input())
      arr1 = list(map(int,input().split()))
      if N == len(arr1):
            maxi = -1 #coz the possible lower digit can be this
            mini = 10000001 #coz the possible higghest value can be this
            for ele in range(N):
                  if arr1[ele]<mini:
                        mini = arr1[ele]
            for ele in range(N):
                  if arr1[ele]>maxi:
                        maxi = arr1[ele]
            print(mini,maxi)
      T -=1