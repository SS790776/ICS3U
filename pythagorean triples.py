import math as m

def triplets(max):
    tripletsarr = []
    for x in range(3,max+1,2):
        if x**2 + ((x/2) * (x+1))**2 == ((x/2)*(x+1) + 1)**2:
            tripletsarr.append(x)

    return tripletsarr

print("""pythagorean triples
----------------------------------------------""")
p = 1
while p == 1:
    x = 1
    while x == 1:
        try:
            max = int(input("Please input an odd number as max: "))
            x = 0
        except ValueError:
            print("Please input an odd INTEGER")
            x = 1
    if max %2 == 1:
        p = 0
    else: 
        p = 1
        print("Please input an ODD number")
        print("--------------------------------")
print(triplets(max))

        
