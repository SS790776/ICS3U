import math as m

def factorise(x):
    
    list = []
    i = m.floor(m.sqrt(x))
    for p in range(i,x):
        if x%p == 0:
            list.append(p)

    return list

print(factorise(24))
