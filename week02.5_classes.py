#Class

#we create a class using Mobile as example
class Mobile:
      def __init__(self):
            self.brandName = "Samsung"
            self.color ="Mate Black"
            self.isJack =False

      def calling(self):
            print("Calling")

      def cameraClick(self):
            print("Picture is clicked")

      def message(self):
            print("Message sent")


def main():
      m1 = Mobile()
      print(m1.brandName)
      print(m1.color)
      print(m1.isJack)
      m1.calling
      m1.cameraClick
      m1.message
      print("____________________")
#we can print as many we want
      m2= Mobile()
      print(m2.brandName)
      print(m2.color)
      print(m2.isJack)
      m2.calling

#in the above as many mobiles we create everything will be same
#so if we want mobiles to be from other manufactureres and diff colour

#we can pass them as parametes and get them and print them 

#eg

class Mobile:
      def __init__(self,brandName,color,isJack):
            self.brandName = brandName
            self.color = color
            self.isJack = isJack

      def calling(self,name):
            print("Calling "+name)

      def cameraClick(self):
            print("Picture is clicked")

      def message(self):
            print("Message sent")


def main():
      m1 = Mobile("Samsung","Mate Black",True)
      print(m1.brandName)
      print(m1.color)
      print(m1.isJack)
      m1.calling("Dinesh")
      m1.cameraClick
      m1.message
      print("____________________")
#we can print as many we want
      m2= Mobile("Apple","Army Green",False)
      print(m2.brandName)
      print(m2.color)
      print(m2.isJack)
      m2.calling("Sanjay")


#creating a class student

from sqlalchemy import false, true


class Student():
      def __init__(self,studentName,studentRegNo,studentclass):
            self.studentName = studentName
            self.studentRegNo = studentRegNo
            self.studentClass = studentclass


student1 = Student("Dineshkumar","11711397","E1707")
student2 = Student("Jey","11753463","M1703")
print(student1.studentName, student1.studentRegNo,student1.studentClass)
print(student2.studentName,student2.studentRegNo,student2.studentClass)



#create class for showing 
'''Instance Variable and Class Variable'''
class Mobile:
      tempered = true
      chargingwithbox = false
      #the above two are class variables and we can access with any instance

      def __init__(self,brandName,colour,isJack):
            self.brandName = brandName
            self.colour = colour
            self.isJack = isJack
            #the above are instance variables these change for every value

mobileM1 = Mobile("Oppo","Black",true)
mobileM2 = Mobile("OnePlus","Blue",false)   
print(mobileM1.brandName)
print(mobileM2.colour)

#we can also able to create a instance variable
#eg:
mobileM1.screen = "LED"
print(mobileM1.screen)
#now this will print LED but if we use for other instance that is M2 
#now we will get error and this is why it is known as Instance variable

#now will create a class variable
Mobile.year ="2022"
#now we can use this to any instance we create
print(mobileM1.year)
print(mobileM2.year)
#i.e: the variables that are limited to certain instance are called Instance variable and to the class are called Class Variable




#Inheritance
#will create a parent class and derived class and know how inheritance work

class Car:
      def __init__(self,gears,seats,maxSpeed):
            self.gears = gears
            self.seats = seats
            self.maxSpeed = maxSpeed

      def accelerate(self):
            print("Speed increased")

      def break_now(self):
            print("Speed decreased and stopped")

class Thar(Car):#above for thar we haven't initiated any attributes but it still asks for atributes 
#this is called inheritance
      def fourwheeldrive(self):
            print("four wheel drive mode on!")
      #the derived need not only to have parent class attributes it can have its own too

car1 = Thar("5","4","140") 
print(car1.accelerate())
print(car1.fourwheeldrive())
#like normal we can also able to create instance with car class
car2 = Car("6","7","170")
print(car2.accelerate())

#we can have as many derived class as we want eg:
class Urus(Car):
      def sportsmode(self):
            print("Sports mode activated huhu!!")

car3 = Urus("6","5","240")
print(car3.maxSpeed)
print(car3.sportsmode())
print(car3.gears)