'''
Numbers - normal numeric characters like numbers - integers nd float

Strings - everything withing a quotes is string i.e: double or single quotes
      strings are immutable and can be itterated or sliced

Lists - list is a collection of data within a squre brackets
      it can be of anything like strings , numbers and even another list.
      these can be muted and can slided and itterated.

Tuples - Tuples are  immutable and can be sliced and ittrated

Dictionaries - are the key value pairs and can be sliced and itterated
      and wrote within set brackets'''


#use all the srithmatic operators qand bring value equal to 100.25
print(100/2*2+1-0.75)


#square root and square
print(4**0.5)
print(3**2)


# in hello string return e
s = "hello"
print(s[1])
print(s[-4])


#reverse string using slicing
print(s[::-1])


#build list in two ways
a = [0,0,0]
b = [0]*3

print(a)
print(b)


#reassign "hello" in nested list to say "Goodbye"
list1  = [1,2,[3,4,'hello']]
list1[2][2] = "goodbye"
print(list1)


#sort the list
list1 =[5,3,4,6,1]
list1.sort()
print(list1)

listsorted = sorted(list1)
print(listsorted)


#grab the "hello using the indexing and keys"
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])


#difference between list and tuple and create simple tuple
''' 
      - Tuples are immutable
      - a = (1,2,3,4)'''


#what is unique about set
'''
Set are unique set of values, can use to find unique set of values'''

#use a set to find the unique values of the list below
list5 = [1,2,2,33,4,4,11,22,3,3,2]
list_set = set(list5)
print(list_set)


#use print formating to print some text
print("this is what %s have thought to print"%'I')