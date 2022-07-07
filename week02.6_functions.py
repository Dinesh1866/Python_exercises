#Functions are of two types user defined and inbuild functions
#user defined can be of four types

'''one that
1. takes in no arguments and return no value
2. takes in argument and return no value
3. takes in no argument and return value
4. takes in argument and returns value
'''

# takes in no arguments and return no value
from tempfile import tempdir


def add1():
  a,b = map(int, input("values for addition: ").split())
  print(a+b)

#takes in argument and return no value
def swap1(a,b):
  c = a
  a = b
  b = c
  print("a=%d,b=%d"%(a,b))

def swap2(a,b):
  print(type(a),type(b))
  c = a[0]
  a[0] = b[0]
  b[0] = c
  print("a=%d,b=%d"%(a[0],b[0]))


#takes no arguments and return value
def add3():
  a,b=map(int,input("value for Addition: ").split())
  return a+b
#takes in argument and return value
def add4(a,b):
  return int(a)+int(b)

value1 = add3()
print("sum=",value1)
value2= add4(4,5)
print("sum=",value2)


def main():
  add1()
  a,b = map(int, input("swapping values: ").split())
  swap1(a,b)#here only the value of this function changes
  print(a,b)#just because it's direct function here the original value remain as it is 
  a,b = map(int, input("swapping values: ").split())
  x=[0]*1
  y=[0]*1
  x[0]=a
  y[0]=b
  swap2(x,y)#here we are giving the input in list so it will automatically get converted to list
  print(x[0],y[0])#here just because its not direct method and we gave attri as list. the value will also change 

if __name__=="__main__":
  main()