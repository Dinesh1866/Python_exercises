'''Use for, .split(), and if to create a Statement that will 
print out words that start with 's':'''
st = 'Print only the words that start with s in this sentence'
for words in st.split():
      totalwords = words.lower()
      if totalwords[0] == 's':
            print(totalwords)


'''Use range() to print all the even numbers from 0 to 10'''
for nums in range(11):
      if nums%2 ==0:
        print(nums)

#or 
print(list(range(0,11,2)))


'''Use a List Comprehension to create a list of all numbers 
between 1 and 50 that are divisible by 3.'''
divby3 = [num for num in range(0,50) if num%3==0]
print(divby3)

#if normal method
divby3 =list(range(0,51,3)) 
print(divby3)


'''Go through the string below and if the 
length of a word is even print "even!"'''
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
      if len(word)%2 == 0:
            print(word +" has even lengtheven")


'''Write a program that prints the integers from 1 to 100. But for multiples of 
three print "Fizz" instead of the number, and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".'''
for num in range(1,101):
      if num%3 ==0 and num %5 ==0:
            print("FizzBuzz")
      elif num%3 ==0:
            print("Fizz")
      elif num% 5 ==0:
            print("Buzz")
      else:
            print(num)


'''Use List Comprehension to create a list of the 
first letters of every word in the string below:'''
st = 'Create a list of the first letters of every word in this string'
firstlet = [word[0] for word in st.split()]
print(firstlet)