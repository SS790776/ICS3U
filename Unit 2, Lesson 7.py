import math as m
#create variables
N = 10
N2 = 0
N3 = 0
N4 = 0
#create header
s = "%3s |%5s |%7s |%5s" % ("N","SQR","Cubes","Roots")

print(s)
print("----+------+--------+-------------")
#from 10, to 190 increasing by 15 each time. N = x, N2 = x squared, N3 = x cubed, N4 = x square root.
for x in range(10,201,15):
    N = x
    N2 = x**2
    N3 = x**3
    N4 = m.sqrt(N)
    print("%3d |%5d |%7d |%5.2f" % (N,N2,N3,N4))
    
