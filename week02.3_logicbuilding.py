#print the first letter from the input without indexing
'''n = int(input())
rem = 0
while n!=0:
      rem = n%10
      n = n//10
print(rem)'''


#one pattern
'''print
1
11
111
1111
11111'''
for i in range(0,5):
      for j in range(i,5):
            print('1',end=" ")
      print()

#or
for i in range(5,0,-1):
      for j in range(i,0,-1):
            print("1", end=" ")
      print()

#but for above solution
for i in range(1,6):
      print("1"*i)

#but what if the pattern changes like instead 1 print *
#or print 123 numbers 
for i in range(1,6):
      for j in range(i):
            print("1",end="")
      print()

#print numbers
for i in range(1,6):
      for j in range(1,i+1):
            print(j,end="")
      print()

#same above pattern in reverse
for i in range(6,1,-1):
      for j in range(i):
            print("1",end="")
      print()

#above in mirror 
for i in range(5,0,-1):
      for j in range(5,i,-1):
            print("1",end=" ")
      print()

#another try
pattern = 4
for i in range(1,6):
      for k in range(1,pattern+1):
            print(end=" ")
      pattern -=1
      for j in range(i,0,-1):
            print(j,end="")
      print()


#v pattern
'''
1        1
12      21
123    321
1234  4321
1234554321'''
#ch = input()
pattern = 8
for i in range(1,6):
      for j in range(1,i+1):
            print(j,end="")
      for k in range(1,pattern+1):
            print(end=" ")
      pattern -=2
      for j in range(i,0,-1):
            print(j,end="")
      print()