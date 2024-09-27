import math

x = int(input("Please input a whole number between 1 and 20: "))
#if x is greater than or equal to one, and also less than or equal to 20, then ask for y. if not, then print "number entered not valid, unable to compute"
if x >= 1 and x <= 20:
    y = int(input("Please input another nonzero whole number between 1 and 20: "))
    #if y is greater than or equal to one, and also less than or equal to 20, then continue. if not, then print "number entered not valid, unable to compute"
    if y >= 1 and y <= 20:
        #see if x is divisible by y, if it is then print "Yes! y is a factor of x" if not, then print ("no, y is not a factor of x")
        if y != 0:
            rem = x%y
        if rem == 0:
            print("Yes!", y, "is a factor of",x)
        else:
            print("No,",y, "is not a factor of",x)

    else:
        print("Number entered not valid, unable to compute")
        
    
else:
    print("Number entered not valid, unable to compute")


