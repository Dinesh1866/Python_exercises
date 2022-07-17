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