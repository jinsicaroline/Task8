#Program 1
class Circle:
# constructor
 def __init__(self):
# initializing instance variable
    self.num=[10,501,22,37,100,999,87,351]

# a method
def read_number(self):
    print(self.num)

# creating object of the class. This invokes constructor
obj = Circle()

# calling the instance method using the object obj
obj.read_number()

#output:
[10, 501, 22, 37, 100, 999, 87, 351]

#...........................................................................................................#

#Program 2

class myClass:
 a = 33;
def __privMeth(self):
   print("I’m inside class myClass")
def hello(self):
   print("Private Variable value: ",myClass.a)
foo = myClass()
foo.hello()
foo.a

#output
Private Variable value: 33

#..........................................................................................................#

#Program 3

class Circle():

 def __init__(self, r):
     self.radius = r

def area(self):
    return self.radius**3.141

def perimeter(self):
    return 2*self.radius*3.141

NewCircle = Circle(7)
print(NewCircle.area())
print(NewCircle.perimeter())

#output
451.2871252038085 43.974000000000004

#.........................................................................................................#

#Program 4
#Part A
def __init__(self,brand,price,onoFFstatus,volume=50):
 self.brand = brand
 self.price = price
 self.inches = inches
 self.onoFF = onoFF
 self.volume = volume
 self.channel = channel

def increaseVolume(self):
    if self.volume<100:
        self.volume+=1

def  decreaseVolume(self):
    if self.volume>0:
        self.volume-=1

def changechannel(self:channelNumber):
    if 0<=channelNumber<=50:
        self.channel=channelNumber

def reset(self):  
 self.channel = 1
 self.volume = 50

 def showstatus(self)  :
    print(f"{self.brand}at channel,{self.channel},volume(self.volume)")

#......................................................................................................#
#Part B

class plasma(TVclass):
      pass
class LEDTV(TVclass):
    pass

    plasma = plasma("Sorry",100000,50,"on")  
    plasma.showstatus
    plasma.increasevolume()
    plasma.changechannel(29)
    plasma.showstatus    