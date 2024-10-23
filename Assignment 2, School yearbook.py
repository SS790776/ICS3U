"""
    Sean Shi
    790776
    10/23/2024
    ISC3U Assignment 2
    
"""
import math as m

def factors(N):
    """
    
    """
    facts = []
    index = m.floor(m.sqrt(N))
    for x in range(1, index+1):
        if N % x == 0:
            facts.append(x)
    
    return facts

p = 1

print("The School Yearbook Planner Program! ")
print("If at any time you wish to stop the program, type 'none' \n")

while p == 1:
    N = input("Please enter the number of photographs: ")
    
    try:
        N = int(N)
        if N <= 0:
            print(f"{N} is not a valid number, please try again \n")
            p = 1
        else:
            factorsarr = factors(N)
            index = len(factorsarr)-1
            best = factorsarr[index]
            ndbest = m.floor(N/best)
            print(f"The minimum perimiter is {2*(best + ndbest)}, with dimensions {best}x{ndbest}. \n")
            p = 1
    except ValueError:
        if N == "none" or N == "None" or N== "NONE":
            print("Hope we've helped, happy yearbook planning!")
            p = 0
        else:
            print(f"Please input a valid integer, I don't understand what '{N}' is \n")
            p = 1
