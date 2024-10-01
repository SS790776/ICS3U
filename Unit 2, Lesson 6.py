print("Shape maker")
print("--------------------")
#Count variable to make the first shape
count = 1

#let the user input the count number, to determine the size. It has to be an even number though, or else the program will crash. Hence, the while loop
while count%2 !=0:
    count = int(input("Enter an EVEN number for the size of the shapes please: "))
input("Ready? \n")
#Make a second variable for the second shape
count2 = count
#Make 2 more variables for the third shape (will explain why later)
temp = 0
temp2 = 0
#String hash and string space variables
S = "#"
B = " "

#Will go down 
for i in range(count, 0, -1):
    print(S * i)
print("--------------------")

for x in range(0, int(count/2)):
    print(B*int((count/2)), end = f"{S+(S*(x*2))} \n")
    
    count -= 2

print("--------------------")

for x in range(int(-count2/2),int(count2/2)+1):
    i = abs(x)
    
    print(B*i,end = f"{S+(S*(temp2*2))} \n")
    
    if temp < count2/2:
        temp += 1
        temp2 +=1
    else:
        temp2 -=1
