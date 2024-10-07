import math 
def add(num1,num2):
    return num1 + num2

def mypow(num1,num2):
    return math.pow(num1,num2)
x = 1
while x == 1: #while they don't enter an integer
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        x = 0 #if both don't throw an exception, then exit the loop
    except ValueError:
        print("Sorry, you need to enter an integer")
        x = 1 #continue asking.

sum = add(num1,num2)#call the sum function
pow = mypow(num1,num2)#call the pow function
print("Sum: %.2f"%sum) #round by 2 decimal points
print("pow: %.2f" %pow) #round by 2 decimal points
