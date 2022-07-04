#sum of digits given in input
#102345 -> 1+0+2+3+4+5=15
'''X = input()
value = 0
for numbers in X:
  value += int(numbers)
print(value)'''

#reverse the number



#Print in the output the exact pattern provided below
'''
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1'''
'''value = input()
for a in range(1,6):
      for b in range(1,a+1):
            print(value,end=" ")
      print()'''


'''Print in the output the exact pattern provided below
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1'''
value = input()

for x in range(1,6):
      for y in range(1,x):
            print(y,end=" ")
      print()