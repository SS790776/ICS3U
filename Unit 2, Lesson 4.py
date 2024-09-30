print("Factorial  calculator")
print("--------------------------------------------------")

#Declare variables
num = int(input("Please input a number to calculate: "))
count = 0
total = 1
#while count is less than the number, first check if count is equal to 0, if it is then print "0! = 1". Then, add 1 to count, then multiply count to total, then print "count#! = total"
while count < num:
    if count == 0:
        print(f"{count}! = 1")
    count += 1
    total *= count
    print(f"{count}! = {total}")
