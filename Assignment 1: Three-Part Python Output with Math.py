"""
Author: Sean Shi
Student Number: 790776
Date: 24 September 2024
Description: Assignment to code a python
script that can perform multiple calculations
given different inputs.
Variable Dictionary:
    length = length of rectangle
    width = width of rectangle
    rectarea = rectangle area
    r = radius 
    circarea = circle area
    cylh = cylinder height
    cylr = cylinder radius
    cylsa = cylinder surface area
    cylv = cylinder volume
    g = gravity
    l = length
    p = time
"""

import math as m

#rectangle, rectarea = rectangle area
print("First calculation: Area of a rectangle")
length = float(input("Please enter length: "))
width = float(input("Please enter width: "))
rectarea = length * width
print("The area of the rectangle with length %.2f and width %.2f is %.2f units squared" %(length,width,rectarea))
print("---------------------------------------")
#Circle, r = radius, circarea = circle area
print("Second calculation: Area of a circle")
r = float(input("Please enter radius: "))
circarea = m.pi*r**2
print("The area of the circle with radius %.2f is %.2f units squared" %(r,circarea))
print("---------------------------------------")
#SA and volume of cylinder, cylh = cylinder height, cylr = cylinder radius, cylsa = cylinder surface area, cylv = cylinder volume.
print("Third calculation: Surface Area and Volume of a cynlinder")
cylh = float(input("Please enter height: "))
cylr = float(input("Please enter radius: "))
#SA = 2pirh + 2pir^2
cylsa = 2*m.pi*cylr*cylh + 2*m.pi*cylr**2*cylh
#V = pir^2h
cylv = m.pi*cylr**2*cylh
print("The surface area and volume of the cylinder with height %.2f and radius %.2f is SA = %.2f units squared and V = %.2f units cubed" %(cylh,cylr,cylsa,cylv))
print("--------------------------------------")
#period for a pendulum g = gravity, l = length, p = time
print("Fourth calculation: the period of time it takes for a pendulum to make on back and forth swing")
g = 9.8
l = float(input("Please enter length (in meters): "))
p = 2*m.pi*m.sqrt(l/g)
print("The time it takes for a pendulum of  length %.2f meters and gravity of %.2fg to make one back and forth swing is = %.2f seconds" %(l,g,p))
