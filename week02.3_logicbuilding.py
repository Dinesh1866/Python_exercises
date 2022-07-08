# Print first Integer. takes in Number of Test cases and Integer
#print the first letter from the input without indexing

#implimentation eg:
n = int(input())
rem = 0
while n!=0:
      rem = n%10
      n = n//10
print(rem)

#answer
for value in range(int(input())):
  N = int(input())
  nrem =0
  while N >0:
    nrem = N%10
    N=N//10
  print(nrem)



#Sum of Digits - ie : we input a number with certain gigits and wanna find sum of each nums
#eg: 12345 = 15

X = input()
value = 0
for numbers in X:
  value += int(numbers)
print(value)



#favourite number - i.e: a number with certain digits will be given
#and we'll select a num and if the number present in the input digit 
#we should print the number and how many times do they occured

for val in range(int(input())):
  N = input()
  count = 0
  for value in range(len(N)):
    if N[value] =="5":
      count = count + 1
  print(count)



#Reverse the Number - i.e: an input should be number with certain digits
#we should reverse the number without using inbuild numbers
#the given number or input shjould not staret with z or end with zero

'''X = input()
print(X[::-1])'''

num=int(input())
result = 0
while num!=0:
  last_digit = num %10
  num = num//10
  result = result *10 + last_digit
print(result)



#Find Relation between two numbers - Operators. i.e: we input two integers X and Y
# and we should find X is greater Than Y or Smaller or equal to Y.

X,Y = map(int,input().split())
if X >Y:
  print("%d is greater than %d" %(X,Y))
elif X <Y:
  print("%d is smaller than %d"%(X,Y))
else:
  print("%d is equal to %d"%(X,Y))



#Character value - i.e: for every input character we should print a predefined character or string
#eg: D or d - Dineshkumar , R or r - Radha , S or s - Subramanian, sanjay
ch = input()
if ch=="D"or ch=="d":
      print("Dineshkumar")
elif ch=="S"or ch=="s":
      print("Subramanian, Sanjay")
elif ch=="R"or ch=="r":
      print("Radha")



#Find the given year is a leap year or not. and takes in test cases as input and Years
def getLeapyear(year):
  if year %4 ==0:
    if year %100==0:
      if year %400 ==0:
        print("Yes")
      else:
        print("No")
    else:
      print("Yes")
  else:
    print("No")

for years in range(int(input())):
  getLeapyear(int(input()))



#Find the Second smallest integer from the given three values
X,Y,Z = map(int,input().split())
max_val=max(X,Y,Z)
min_val=min(X,Y,Z)
if X!= max_val and X!=min_val:
      print(X)
elif Y!= max_val and Y!=min_val:
      print(Y)
else:
      print(Z)



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
'''
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1'''
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