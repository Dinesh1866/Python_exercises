#Class

'''
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
      m2.calling'''

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


#def main():
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