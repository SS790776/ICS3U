"""
Sean S
12/16/2024
ICS3U 
Programming Assignment 4

Variable dictionary:
    variable - description
"""

def merge():
    """
    this function takes x, and does y, and returns z
    :param variable: description

    :return: description
    
    variable - description.

    """ 
    print("ploting...") #tell the user that turtle is currently plotting
    counter = 0 #create variable counter and assign to a value of 0
def search():
    """
    this function takes x, and does y, and returns z
    :param variable: description

    :return: description
    
    variable - description.

    """ 
    print("ploting...") #tell the user that turtle is currently plotting
    counter = 0 #create variable counter and assign to a value of 0
    

file = 'wordle.dat'

firstinf = [] #create the array for the first line of information
try: #make a try and except in case opening the file goes wrong
    fh = open(file, "r") #open the file
    firstinf = fh.readline() #assign firstinf to the first line of the file
    #split the first line of the file and assign into the x dimension, y dimension, 
    #and total number of colours.
    xdim, ydim, colournum = firstinf.split(" ") 

    colour = { #create the colour dictionary to store colours and corresponding symbols
        
        }
    
    for x in range(int(colournum)): #iterate for every colour
        line = fh.readline() #read the next line
        line.strip() #strip the leading/trailing whitespace from the text of the line
        #split and assign the line into symb (the symbol, c, and rainbow (the colour)
        symb, c, rainbow = line.split() 
        
        if symb == "~": #if the symbol is "~" then assume it is a space " "
            symb = " "
            #put the symbol and corresponding colour together into the dictionary
            colour.update({symb:rainbow}) 

        else: #if the symbol is not "~"
            #put the symbol and corresponding colour together into the dictionary
            colour.update({symb:rainbow})
    
    
    
    image = [] #create array that will store the symbols/characters of the image

    for i in range(int(ydim)): #iterate through each line
        line = fh.readline()#read the next line
        #get rid of the "\n" endline character from what we're extracting
        line = line.replace('\n', '') 
        image.append(line) #add the extracted line into the image array




    fh.close()#close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print out the error
    exit() #stop the program

u = 1 #create variable u and assign a value of 1
while u == 1: #while u has a value of 1
    #ask for user input of what type of background they'd like
    ld = input("Would you like a darker or lighter background? L/D or W for no background: ") 
    
    if ld == "L" or ld == "l": #if the user inputted a variation of "L"
        turtle.bgcolor("gray70") #make the background a lighter gray
        u = 0 #assign u to a value of 0 which exits the while loop
    elif ld == "D" or ld == "d": #if the user inputted a variation of "D"
        turtle.bgcolor("gray40") #make the background a darker gray
        u = 0 #assign u to a value of 0 which exits the while loop
    elif ld == "W" or ld == "w": #if the user inputted a variation of "W"
        turtle.bgcolor("white") #make the background white
        u = 0 #assign u to a value of 0 which exits the while loop
    else: #if the user input is a response that was not expected
        print("not a valid response, please try again") #ask for user input again
        u = 1 #assign u to a value of 1 which continues the loop

o = 1 #create variable o and assign a value of 1
#ask for user input of the desired spacing and size of the dots
print("""Please enter the desired spacing and size of the dots.
*Recommended amount is space = 2 and size = 4""")

while o == 1:#while o has a value of 1
    try: #make a try and except in case the user doesn't input an integer
        space = int(input("Space: ")) #ask and take in user input for spacing
        size = int(input("Size: ")) #ask and take in user input for size
        o = 0 #assign o to a value of 0 which exits the while loop
    except ValueError: #catch the value error expection when converting to int
        #ask again for a valid user input
        print("You did not give a valid integer, please try again \n")
        o = 1 #assign o to a value of 1 which continues the loop
        
p = 1 #create variable p and assigne a value of 1
while p == 1:#while p has a value of 1
    try:#make a try and except in case the user doesn't input an integer
        #ask for user input for the desired rotation of the image
        rotation = int(input("Please enter the desired rotation (0, 90, 180, 270): "))
        p = 0 #assign p to a value of 0 which exits the while loop
    except ValueError: #catch the value error expection when converting to int
        print("You did not give an integer, please try again \n")
        p = 1 #assign p to a value of 1 which continues the loop
    if rotation == 0: #if the user inputted 0
        uprightgraph(xdim,ydim,space,size,image) #call uprightgraph function

    elif rotation == 180: #if the user inputted 180
        upsidedowngraph(xdim,ydim,space,size,image) #call upsidedowngraph function

    elif rotation == 90: #if the user inputted 90
        ninetygraph(xdim,ydim,space,size,image) #call ninetygraph function

    elif rotation == 270: #if the user inputted 270
        twoseventygraph(xdim,ydim,space,size,image) #call twoseventygraph function

    else: #if the user gave a response unexpected
        #ask for valid user input again
        print("You did not give a valid rotation number, please try again")
        p = 1 #assign p to a value of 1 which continues the loop
    
print("Done! Please check to see if the Turtle graphics window has opened.")
