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

#Will go down from count to 1, at -1 increment. So say count =10, then it will print 10 #, then 9 #, all the way to 1#
for i in range(count, 0, -1):
    print(S * i)
print("--------------------")
#The next shape goes from 0 to count/2-1. So say count is 10, it will go from 0 to 4. And the math goes it will print space 4 times, and print the string 1 time (because # + #*0*2 = one hashtag) and it will keep increasing in so space will decrease by 1 each time, and hastag will increase by 2 each time.
for x in range(0, int(count/2)):
    print(B*int((count/2)), end = f"{S+(S*(x*2))} \n")
    
    count -= 2

print("--------------------")

#Say count2 = 10, then it will start at -5, and increase by 1 to 5. i is the absoloute value of x, so if x = -5, i = 5. Then it will take B*i so if i = 5, then it will print 5 spaces, and # + #*0*2 which equals to 1 hashtag. 
#Then, as x increases the spaces will decrease by 1 and the hashtags will increase by two, while the temperary variables increase by 1 each time.
#Once temp reaches half of count2 (so 5), it will be the same time that x reaches 0. Then, it will flip the process by subtracting the temp2 variable that is used in calculations. Now, the spaces will increaase in number as x increases and the hashtags will decrease in number as  temp2 decreases.
#The reason why I needed temp AND temp2 is because if I just had 1 temperary variable, then once I decrease the value of the variable once it reaches half of count2, it will go back to the condition where the variable value will increase.
for x in range(int(-count2/2),int(count2/2)+1):
    i = abs(x)
    
    print(B*i,end = f"{S+(S*(temp2*2))} \n")
    
    if temp < count2/2:
        temp += 1
        temp2 +=1
    else:
        temp2 -=1
