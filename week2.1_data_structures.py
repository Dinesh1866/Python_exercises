from sqlalchemy import union


print(5//2)
print(5.6//3)
print(7//3.2)
print(7.5//3.5)

print((1,2)+(3,4))

'''N,M= map(int,input().split())
print(N,M)'''

'''N,M,ch = input().split()
N = int(N)
M = float(N)
print("%d$%.2f$%c"%(N,M,ch))'''

st = "abcdefghijk"
print(st[7::-1])

st_lst = ['a','b',3,6,'c']
del st_lst[2]#for deleting
print(st_lst)
st_lst[2:2] = [3]#for inserting
print(st_lst)
st_lst[1:4] = [1000]#for modfying mul values
print(st_lst)

#if we concatinate them without converting them to a list
#the it will take all the individual elements and append it to the list
list1 = st_lst + ["haha"]#append
print(list1)

list1 = ["hehe"]+ st_lst#prepend
print(list1)

list1.append("hey!")#this can append the object to list
print(list1)

list1.insert(0,10)#take index and objt and insert them
print(list1)

list1.pop()#this will by default pop the last object in list
poped_list = list1.pop()#we can also able to store the values in variable
print(list1)
print(poped_list)

#Dictionary - key value pairs
#can only get values with keys
ipl_team = {}
ipl_team["CSK"] = "Dhoni"
print(ipl_team)
ipl_team["MI"] = ["Rohit","Bumrah","SKY","Ishan"]
print(ipl_team)
print(ipl_team["MI"])
print(ipl_team["MI"][2])#can also able to get objects within a value
del ipl_team["CSK"]
print(ipl_team)
print(ipl_team.get("MI"))#get can be used to return values
print(ipl_team.get("CSK",None))#can give a default value so if key not present
#it can return the default value
ipl_team["CSK"]=["Dhoni","Jadeja","Raina","Bravo"]
ipl_team["RCB"]=["Virat","Gayle","ABD"]
print(ipl_team.items())#items will return all the key,value pairs
print(ipl_team.keys())#will print all the keys in dict
print(ipl_team.values())#will return all the values in dict
print(ipl_team.pop("Delhi","key not found"))#takes in key and default values
#if key not present return the default message or value.
print(ipl_team.popitem())

#Sets - these are used to store unique values
#and these are immutable so we cannot use dicts and lists
S1 = set([4,5,6,6,7,4,8,9,5,8])#can give list itterable as input and make list
print(S1)
S2 = set("This is 100 Days of Code")#can itterable also be string
print(S2)
S3 = {4,6,4,8,9,0,6,0,8,5}#can directly provision using {}
print(S3)
S4 = {}#cannot create empty set with {} it will become dict
print(type(S4))
S5 = set()#can provision empty set with set() function
print(type(S5))
#methods that work in Sets
print(len(S2))
print("C" in S3)
print("C" in S2)
#operators that present in the set
print(S1.union(S2))
print(S1 | S2)#union method
print(S1.intersection(S2))#if no intersection we get empty set
print(S1 & S3)#intersection
print(S1.difference(S3))
print(S1 - S2)
S7 = {0,1,2,3,4,5,6,7,8,9,10}
print(S3.issubset(S7))#subset
print(S2.issubset(S3))
print(S3<= S7)
print(S7.issuperset(S3))#superset
print(S7>= S3)
#methods
S7.add(11)#adds the value
print(S7)#adds the value
S7.remove(11)#remove the value if value not present throw error
print(S7)
S7.discard(11)#remove value if no such value don't return error
print(S7)
print(S7.pop())#pop some random value in the set
S2.clear()#clear the whole list
print(S2)