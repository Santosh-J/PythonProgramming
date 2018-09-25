import operator
# using operator library
message= "Meet me tonight."
print(message)
message2 ="""One of my favotite is: "I'm really bad"""
print(message2)
# understanding sorting
xs={'a':4,'b':3,'c':2}
print(sorted(xs.items(),key=operator.itemgetter(1)))
print(sorted(xs.items(),key= lambda x:x[1]))
x,y,z=0,1,0
if x==1 or y==1 or z==1:
    print("passes")
if 1 in (x,y,z):
    print("Passed")
if any((x,y,z)):
    print("good")

# example of namedtuple

from collections import namedtuple
Car=namedtuple('Car','color mileage engine')
my_Car=Car('red',31,'mach')
# accessing Car using my_Car
print(my_Car.engine)
print(my_Car)
Fruit=namedtuple('fruit','size color rate')
a=Fruit(10,'red','20')
print(a.size)
print(a)