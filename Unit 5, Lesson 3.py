def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(C): 
    for i in range(len(C)): #iterate through each element
        for j in range(i+1,len(C)-1,1): #changed so it won't swap what's already been swapped
            if (C[i] > C[j]): #if the current number is greater than the number we're on
                swap(C, i, j) #swap the two

A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
