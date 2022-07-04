#if else
#sample 
a = 5
b = 3
if a > b:
      print("a is grater than b")
else:
      print("b is grater!")

#lets add elif 
a = 5
b = 5
if a > b:
      print("a is grater than b")
elif a ==b:
      print("both a and b are equal")
else:
      print("b is grater!")

#find greater value in three value
a = 5
b = 7
c = 6
print(max(a,b,c))

#or
if a>b and a > c:
      print("a is greater")
elif b>a and b>c:
      print("b is greater")
else:
      print("c is greater")

#print sll the while loops using while
n= 50
i= 1
while (i<=n):
      if i%2==0:
            print(i)
      i += 1

#reverse
i = 50
while(i>0):
      if i%2==0:
            print(i)
      i-=1

#to print all in same line
i = 50
while(i>0):
      if i%2==0:
            print(i,end=" ")
      i-=1

#using break
i = 50
while(i>0):
      if i%2==0:
            print(i)
            if i==32:
                  break #this will break once the valuye is equal to 32
      i-=1

#using continue
'''i = 1
while(i<=50):
      if i==30:
            continue 
      print(i,end=" ")
      i+=1''' # here the loop runs continuously because when 11 then everything below 
      #don't get executed and number don't increment so we stuck in infinite loop

#so
i = 1
while(i<=50):
      if i==30:
            i+=1
            continue #this will not print 30 but will continue even after 32
      print(i,end=" ")
      i+=1
print()


#For Loop
'''x = input()
y = input()
x=int(x)
y=int(y)
if x>0 and y<2000:
  print(x+y)'''
#if input are provided with space
'''x,y = map(int,input().split())
print(x+y)'''

#for loop with range function
for i in range(0,21):#print all the vlaues from 0 - 20
      print(i)

for i in range(0,21,2):
      print(i)#we will get output from 0 to 20 with step cout 2

for i in range(20,0,-1):#this will print all the values in reverse
      print(i)
#the third value in range can be used for incrementing or decrementing

#for loop with strings
for words in "Dineshkumar":
      print(words)

#or
name = "Dineshkumar"
for words in range(len(name)):
      print(name[words])

#using break and continue in for loop
for words in  range(len(name)):
      if name[words]=="k":
            break
      print(name[words])

for words in range(len(name)):
      if name[words]=="k":
            continue
      print(name[words])

#Nested Loop
#lets print all posibilites when two dice are thrown
for x in range(1,7):
      for y in range(1,7):
            print((x,y))

'''a = 0  
while a < 5:  
    print(a)  
    a += 1  
    if a == 3:  
        break  
else:  
    print(0)'''
