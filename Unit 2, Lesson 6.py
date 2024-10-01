print("Shape maker")
print("--------------------")
#Count variable to make the first shape
count = 1

while count%2 !=0:
    count = int(input("Enter an EVEN number for the size of the shapes please: "))
input("Ready? \n")
count2 = count
temp = 0
temp2 = 0
S = "#"
B = " "
for i in range(count+1, 0, -1):
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
