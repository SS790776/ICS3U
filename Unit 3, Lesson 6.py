import math as m

def quicksort(unsorted):
    if len(unsorted) <= 1:
        return unsorted
    else:
        pivot = unsorted[0]
        left = [x for x in unsorted[1:] if x < pivot]
        right = [x for x in unsorted[1:] if x >= pivot]
        
        return quicksort(left) + [pivot] + quicksort(right)

def factorise(x):
    
    list = []
    i = m.floor(m.sqrt(x))
    for p in range(1,i+1):
        if x%p == 0 and x%p != x:
            list.append(p)
            if x//p != p and x//p != x:
                list.append(x//p)

    return quicksort(list)

def check(factors,num):
    sum = 0
    for x in factors:
        sum += int(x)
    if  sum > num:
        return ["abundant"] + [sum]
    elif sum == num:
        return ["perfect"] + [sum]
    elif sum < num:
        return ["deficient"] + [sum]
    
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
    again = ("Would you like to go again? (Y/N) : ")
    if again == "Y" or "y":
        p = 1
    else:
        p = 0 
        print("Thank you for playing!")
