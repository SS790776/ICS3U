"""
Sean S
10/31/2024
ICS3U 
U3 L11

Start with an ordered array
traverse the array sequentially in a for loop
for each index i
temp = B[i]
j = a random number between 0 and the array length - 1
B[i] = B[j]
B[j] = temp
return the array to the main program
print the newly-scrambled array
"""

import random as r

def shuffle(A):
    # Precondition: A must be a 1D array
    # Randomizes a list

    for i in range(0,len(A)-1): #from iterate through each element in the array
        index = r.randint(0,len(A)-1)
        temp = A[i] #temp is the current index element
        #the current index element will be another random integer from the array
        A[i] = A[index] 
        #The random integer will hnow be the current index elemtn
        A[index] = temp
        
    return A
    
print("Array shuffler")
size = int(input("Please enter the desired size of array: "))
B = []
for x in range(0,size+1):
    B.append(x)


print(B) # before
B = shuffle(B)
print(B) # after
