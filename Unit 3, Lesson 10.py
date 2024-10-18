def tripple(limit):
    """
        This function takes an integer as a limit, and prints out all of the pythagorean triples going up to the limit.
    """
    a = 0
    b = 0 
    c = 0
    for x in range(3,limit+1):
        if x % 2 == 1:
            if x**2 + (x//2 * (x+1))**2 == (x//2 * (x+1) + 1) **2:
                a = x
                b = x//2 * (x+1)
                c = x//2 * (x+1) + 1
            print([a,b,c], "=>", a, "+",b,"=",c)
        if x % 2 == 0:
            m = x**2//4
            a = x
            b = m-1
            c = m+1
            print([a,b,c], "=>", a, "+",b,"=",c)
            
          
print("Pythagorean Triple calculator \n")  
limit = int(input("Please enter a limit: "))

tripples = tripple(limit)
print(tripples)
