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
  a,b = map(int, input().split())
  print(a+b)

#takes in argument and return no value
def swap1(a,b):
  c = a
  a = b
  b = c
  print("a=%d,b=%d"%(a,b))

'''
#takes no arguments and return value
def add3():
  a,b=map(int,input().split())
  return a+b
#takes in argument and return value
def add4(a,b):
  return int(a)+int(b)

value1 = add3()
print(value1)
value2= add4(4,5)
print(value2)
'''

def main():
  add1()
  a,b = map(int, input().split())
  swap1(a,b)
  print(a,b)

if __name__=="__main__":
  main()