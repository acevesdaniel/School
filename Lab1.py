'''
Compute the result of 12 raised to the power of 3,
54 raised to the power of 5, and
125 raised to the power of 4
using the appropriate arithmetic operator. 


a = 12 ** 3
b = 54 ** 5
c = 125 ** 4

print()
print()
print("Twelve to the power of three is equal to:", a)
print("Fifty-four raised to the power of five is equal to:", b)
print("One-hundred-twenty-five raised to the power of four is equal to:", c)
print()

'''



'''
3.	Write a program that prompts the user for a radius and then prints the area
and circumference of a circle with that radius. Input needs to be converted into
float.

import math

pi = math.pi

print()
print()

print("Please enter a value you would like to use for a radius for use in")
radius = int(input("calculating the area and circumference for a circle with that radius:\t"))

floatRadius = float(radius)

#Calculations
#A=pi*r²

area = pi * (floatRadius ** 2)
circumference = 2 * pi * floatRadius

#Prompts
print()
print("The entered value to be used as a radius is: %d" %radius)
print("The area of circle with this radius is: %.02f." %area)
print("The circumference of a circle with this radius is: %.02f." %circumference)
print()
print()

'''


'''
4.	Define two points with the coordinates (1,3) and (9,2). Then compute the distance
in between the two pointsusing the following formula:


import math

x1 = 1
x2 = 9

y1 = 3
y2 = 2

innards = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)

distance = math.sqrt(innards)

print()
print("The distance between points (%d, %d) and (%d, %d) is: %.02f" %(x1, x2, y1, y2, distance))
print()

'''

print()
print("Stamp vending machine. 'First-Class' stamps cost $0.49 ea.")
tendered = float(input("Remaining change will purchase 'Penny' stamps ($0.01 ea). Please insert bills here:\t"))

premiumStamps = 0.49

print("You entered $%.02f." %tendered)
print()

maxPremium = (tendered / premiumStamps)
premiumStampTotal = int(maxPremium)
print("You are able to purchase %d 'First-Class' stamps." %premiumStampTotal)

print()
totalCostSoFar = float(premiumStampTotal * premiumStamps)
print("This will cost $%.02f." %totalCostSoFar)

print()
change = float(tendered - totalCostSoFar)
print("Your change is: $%.02f." %change)

print()
resultB = int(change * 100)
print("Your change will purchase %d 'Penny' stamps" %resultB)
print()
