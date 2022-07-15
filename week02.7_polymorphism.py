#Polymorphism Duck Typing - Poly-> many , Morphism->forms or behaviour

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
p2 =Phone()
p2.callFunc(phoneApp)#now we can able to call with our current default app
#here it did not see any data-type etc, it just saw the function and called it
#this is called "Duck Typing"