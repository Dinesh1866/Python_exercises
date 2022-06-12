'''
LESSER OF TWO EVENS: 
Write a function that returns the lesser of two given numbers
if both numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
      return min(a,b)
    else:
      return max(a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))



'''
ANIMAL CRACKERS: 
Write a function takes a two-word string and returns 
True if both words begin with same letter
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False'''
def animal_crackers(text):
    wordlist = text.split()
    if wordlist[0][0] == wordlist[1][0]:
            return True
    else:
            return False
# Check
print(animal_crackers('Levelheaded Llama'))
# Check
print(animal_crackers('Crazy Kangaroo'))



'''MAKES TWENTY: 
Given two integers, return True if the sum of the integers is 20 
or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False'''
def makes_twenty(n1,n2):
    #if n1 ==20 or n2==20:
    if 20 in (n1,n2):
      return True
    elif (n1+n2)==20:
      return True
    else:
      return False
# Check
print(makes_twenty(20,10))
# Check
print(makes_twenty(2,3))
#check
print(makes_twenty(12,8))