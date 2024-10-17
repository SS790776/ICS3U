
def validate(S):
    #False is a 2d array that stores the false letter, and the position. count is a count for each time the for loop iterates
    #This function will go through each element in S, and if it finds a letter other than A C G or T, it will get the letter, and it's position in the string. Then, it will return True if it finds no errors, or returns the false variable if it does.
    false = []
    count = 0
    for x in S: #iterate through each element in S
    
        if x == "A":
            pass
        elif x == "C":
            pass 
        elif x == "G":
            pass 
        elif x == "T":
            pass 
        else:
            temp = [x,count]
            false.append(temp)
        count += 1

    if len(false) >= 1:
        return false
    else:
        return True
        
    
S = input("")

status = validate(S)

if status == True:
    print("Valid")
else:
    print("Not Valid")
    for x in range(len(status)):
        letter = status[x][0]
        position = status[x][1]
        print(f"{letter} found in position {position}")

