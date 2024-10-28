"""
    Sean Shi
    790776
    10/23/2024
    ISC3U Assignment 2
    
    Variables:
    p = an integer, 1 or 0, condition for the while loop
    N = an integer, the input of the user for how many photos
    factorsarr = an array, with the returned value of function factors, holding half of the factors of N
    index = an integer, which will get the index of the last element in "factorsarr"
    best = an integer, which will be the last element (the greatest) in "factorsarr"
    ndbest = an integer, which will be the result of dividing N, by "best"
    
"""
import math as m

def factors(N):
    """
    factors function takes an integer N, and finds all the factors of N up to the square root.
    :param N: N is an integer, most likely the amount of photos.
    :return: returns an array of all of the factors of N up to the square root (half of the factors)
    facts = the array that will hold the return value of half of the factors
    index = the floored value of the square root of N
    """ 
    facts = []
    index = m.floor(m.sqrt(N))
    for x in range(1, index+1): #iterate from 1 to the square root of N
        if N % x == 0: #is N divisible by x?
            facts.append(x) #add x to the facts array
    
    return facts

p = 1 #make p = 1, which be like "True"

print("The School Yearbook Planner Program! ")
print("If at any time you wish to stop the program, type 'done' \n")

while p == 1: #keep looping as long as p = 1
    N = input("Please enter the number of photographs: ") #get the user input
    
    try:
        N = int(N) #try to turn N into an integer, if python doesn't throw an exception, then continue
        if N <= 0: #is x equal to or less than 0?
            print(f"{N} is not a valid number, please try again \n") #then print that N is not a valid number
            p = 1 #and ask for user input again
        else: #if N is a valid integer
            factorsarr = factors(N) #then call the function "factors" with paramiter N and assign it to factorsarr, this will get us an array with half of the factors of N
            index = len(factorsarr)-1 #get the length of factorsarr minus 1
            best = factorsarr[index] #get the last element of factorsarr and assign it to best
            ndbest = m.floor(N/best) #get the second factor, so N divided by "best"
            print(f"The minimum perimiter is {2*(best + ndbest)}, with dimensions {best}x{ndbest}. \n") #output the most efficient perimeter (2 multiplied by (best + ndbest)) and the dimensions "best" by "ndbest"
            p = 1 #and ask for user input again
    except ValueError: #python threw an exception while trying to turn N into an integer, so N would not be an integer.
        if N == "done" or N == "Done" or N== "DONE": #if the user inputted a variation of "done" then we know they're trying to stop the program
            print("Hope we've helped, happy yearbook planning!")
            p = 0 #stop the loop so the program ends.
        else:#anything else and we don't know what the user is trying to say
            print(f"Please input a valid integer, I don't understand what '{N}' is \n") #ouput that we don't know what the user is trying to say.
            p = 1 #and ask again for user input
