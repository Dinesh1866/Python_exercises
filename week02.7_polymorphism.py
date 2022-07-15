'''Polymorphism Duck Typing - Poly-> many , Morphism->forms or behaviour'''

class truecaller():
      def call(self):
            print("Ringing")
            print("Caller data")

class Phone:
      def callFunc(self,phoneApp):#here phoneApp is the object and it do want an class 
            #so we create truecaller to call
            phoneApp.call()

phoneApp = truecaller()#we make the phoneApp to truecaller so we can use the call function in this app 
#to call the class and we can use it
p1=Phone()
p1.callFunc(phoneApp)

#eg: we can also have another class let's say we have a default phone app and we want to use it
class DefaultPhone():
      def call(self):
            print("Calling...")
phoneApp = DefaultPhone()
#here the both app work because we can able to see call func in both the classes
p2 =Phone()
p2.callFunc(phoneApp)#now we can able to call with our current default app
#here it did not see any data-type etc, it just saw the function and called it
#this is called "Duck Typing"



'''Operator Overloading'''
#here lets take the add func and add two value from diff instances
class Student:
      def __init__(self,x,y):
            self.x =x
            self.y =y

      def __add__(self,other):
            ans1 =self.x + other.x #here what happen is it will take other value and at it this value
            ans2 = self.y +other.y
            return ans1 + ans2
#lets make another operator over loading now for lesser than symbol
      def __lt__ (self,other):
            ans1 = self.x + self.y
            ans2 = other.x + other.y
            if (ans1<ans2):
                  return True
            else:
                  return False


S1 = Student(10,20)
S2 = Student(5,6)
S3 = S1+S2 #here S1 values will become self.values and s2 will be other.values
''' So how the above one work is like
S3 = Student.__add__(S1,S2) because here S1 and S2 are student type so Student is called if not then 
int.__add__(5,6) will be called based on type functions are called'''
print(S3)
#So what we here done is we over riden the default add function and made it
# i.e: the + sign function got overriden here
S3 = S1<S2
print(S3)
# I.e: the < or lt function is over rideen here