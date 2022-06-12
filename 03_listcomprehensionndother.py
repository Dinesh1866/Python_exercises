listmo =[1,2,3,4,5,6,7,8]
[print(num) for num in listmo]

no = 0
while no <= 25:
      print(no)
      no += 1
else:
      print("done")
num = list(range(1,20))
print(num)

for x in 'word':
      print(x)

firstword = [x for x in 'word']
print(firstword)

#even numbers using list comprehension
listmo =[1,2,3,4,5,6,7,8]
[print(num) for num in listmo if num%2==0]

#coverting celsius to farenheit
celsius = [0,20,26,31,35,28.5,32.5]
for temp in celsius:
      farenheit = (9/5)*temp + 32
      print(farenheit)

#in one line
farenheit=[((9/5)*temp+ 32) for temp in celsius]
print(farenheit)

#performing netsed list comprehension
lst= [x**2 for x in [x**2 for x in range(11)]]
print(lst)