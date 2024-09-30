print("Triangular AND Factorial  calculator")
print("--------------------------------------------------")

#Declare variables
num = int(input("Please input a number to calculate: "))
factotal = 1
tritotal = 0

for x in range(num):
    if x == 0:
        print("Num  Tri   Factorial")
    x += 1
    factotal *= x
    tritotal += x
    print("%d %5d %10d" %(x,tritotal,factotal))
