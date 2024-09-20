import math
print("Area of a Norman Window shape")
radius = float(input("Please input the circle's radius: "))
area = 0.5 * math.pi * (math.pow(radius,2)) + 4*(math.pow(radius,2))
print("The area of a Norma Window with the radius", radius, "is:", area)
