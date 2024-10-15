import math as m

def quicksort(unsorted): #quicksort function I made
    if len(unsorted) <= 1: #if the unsorted array has 1 or less elements, there's nothing to sort
        return unsorted
    else:
        pivot = unsorted[0] #assign the first number to the variable pivot
        left = [x for x in unsorted[1:] if x < pivot] #if a number is less than the pivot, then it gets assigned to the "left" array
        right = [x for x in unsorted[1:] if x >= pivot] #if a number is more or equal to the pivot, then it gets assigned to the "right" array
        
        return quicksort(left) + [pivot] + quicksort(right) #return quicksort(left) which means to send the array into another quicksort function to sort it again, plus the pivot, and quicksort(right)

def factorise(x): #factorise function I made
    
    list = [] #create list variable
    i = m.floor(m.sqrt(x))  #assign i to the rounded square root of the number (x)
    for p in range(1,i+1): #iterate through each value between 1 and i + 1
        if x%p == 0 and x%p != x: # if the number (x), divided by the current number in the loop's remainder is equal to 0 AND not equal to (X) (removes 1 and x so it's only proper factors)
            list.append(p) #then add p (the current loop value) to list
            if x//p != p and x//p != x: #if the rounded value of x divided by p does not equal to p, and the same equation does not equal to x, then add p to the list (this removes duplicates)
                list.append(x//p) #add the rounded division of x and p to list (eg, if p was 3 and x was 24, then it would add 8, another factor)

    return quicksort(list) #return the sorted list

def check(factors,num): #abundant, perfect, or defficient function I made
    sum = 0 #start with the sum being 0
    for x in factors: #iterate throguh all the factors
        sum += int(x) #add the factors to the sum to get the sum of all of the factors of the number
    if  sum > num: #if sum is greater than the number, then it's abundant
        return ["abundant"] + [sum]
    elif sum == num: #if sum in equal to the number, then it's perfect
        return ["perfect"] + [sum]
    elif sum < num: #if sum is less than the number, then it's deficient
        return ["deficient"] + [sum]
    
"""
    p is an integer, to determine if the while loop continues or not
    fact is an array, which will eventually hold alll of the factors of the number
    list is an array, which will eventaully hold the sum of all of the factors of the number, and the status of the number (abundant, perfect, deficient)
    fac is an integer, which is the number we use to calculate
    sum pulls the sum from the list array
    status pulls the status from the lsit array
    again will hold the response from the user to see if they want to continue using the program or not.
"""
p = 1
fact = []
list = []
print("Proper factors!")
print("------------------------------")
while p == 1:
    fac = int(input("Please enter a number: "))
    fact = factorise(fac)
    list = check(fact,fac)
    sum = list[1]
    status = list[0]
    print(f"Factor sum: {sum}")
    print(f"The number {fac} is {status}")
    again = input("Would you like to go again? (Y/N) : ")
    if again == "Y" or again == "y":
        p = 1
    else:
        p = 0
        print("Thank you for playing!")
