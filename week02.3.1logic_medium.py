#Boxes and Toys
n = int(input())
count =0
while n>0:
      T,C = map(int,input().split())
      if (C-T)==2:
            count +=1
      n -=1
print (count)
