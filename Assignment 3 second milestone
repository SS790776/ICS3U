"""
Sean S
11/20/2024
ICS3U 
Assignment 3 - Making a graphics plotter in Turtle

Variable dictionary:
    t - turtle.turtle(), makes for coding lines and using the turtle object functions a lot
        easier.
    file - a string that holds the name of the xpm file the code needs to use in order to
        plot the dots.
    fh - open(file, "r"), makes for opening files a lot easier,
        instead of needing to code out the whole function I could just use fh.readline().
    line - a string that holds the current line being read, will extract information from
        this variable.
    firstinf - an array that holds the information from the first line of the file.
        This includes the x and y dimensions, and the total number of colours.
    xdim - a variable split from firstinf that contains the x/horizontal dimension
        of the xpm file that needs to be drawn.
    ydim - a variable split from firstinf that contains the y/vertical dimension
        of the xpm file that needs to be drawn.
    colournum - a variable split from firstinf, holds the total number of colours
        needed to draw the picture.
    colour - a dictionary that holds the colours and their corresponding symbol.
    symb - a temporary variable split from line that holds the corresponding symbol
        of a colour.
    c - a variable needed for unpacking and splitting colour definitions.
    rainbow - a temporary variable split from line that holds the colour corresponding
        to a symbol.
    image - an array that holds all of the characters/symbols of the image,
        each index being a seperate line.
    err - a variable that holds the error message for OSError
    err2 - a variable that holds the error message for EOFError
    u - an integer that is either 1 or 0, a condition for a while loop.
    o - an integer that is either 1 or 0, a condition for a while loop.
    p - an integer that is either 1 or 0, a condition for a while loop.
    ld - a string that holds the user input for background customisation.
        L for light grey, D for dark grey, and W for white.
    space - an integer that holds the desired spacing of the dots when drawing.
    size - an integer that holds the desired size of the dots when drawing.
    rotation - an integer that holds the desired rotation in degrees when drawing.
    counter - an integer that keeps count of the amount of lines drawn. Is used
        for calculations when drawing.
    position - a variable that holds the turtle's calculated starting position
        when drawing.
    pointc - a temporary variable that holds the corresponding colour of a symbol
        when drawing.
"""

import turtle #import the turtle library


def uprightgraph(xdim,ydim,space,size):
    """
    uprightgraph takes the x and y dimensions, space and size of dots, and draws the
        image at an upright 0 degree angle.
    :param xdim: xdim is an integer, the x dimension of the drawing so we know when to
        stop drawing for a line.
    :param ydim: ydim is an integer, the y dimension of the drawing so we know when the
        last line is to stop drawing.
    :param space: space is an integer, holds the desired spacing of the dots when drawing.
    :param size: size is an integer, holds the desired size of the dots when drawing.

    :return: draws the image based off of the xpm file and finishes the function.
    
    counter - an integer that keeps count of the amount of lines drawn. Is used
        for calculations when drawing.
    position - a variable that holds the turtle's calculated starting position
        when drawing.
    """ 
    print("ploting...") #tell the user that turtle is currently plotting
    counter = 0 #create variable counter and assign to a value of 0
    
    #make the turtle go to the coordinates of xdim*-space/2, ydim*space/2
    #this coordinate places the turtle at the perfect position top left to create
    #a centered upright drawing
    t.goto(int(xdim)*-space/2,int(ydim)*space/2) 
    position = t.pos() #assign the current position coordinates to variable position
    for i in image: #iterate through each index (line) of the array image
        counter += space #add the value of space to the counter
        #go to the value of counter below the original starting point
        t.goto(position[0],position[1]-counter)
        for x in i: #iterate through each element in the current line
            pointc = colour[x] #get the corresponding colour of the current symbol
            t.dot(size,pointc) #create the dot with the desired size and corresponding colour
            t.forward(space) #move forward (to the right) by the value of space

def upsidedowngraph(xdim,ydim,space,size):
    """
    upsidedowngraph takes the x and y dimensions, space and size of dots, and draws the
        image at an upside down 180 degree angle.
    :param xdim: xdim is an integer, the x dimension of the drawing so we know when to
        stop drawing for a line.
    :param ydim: ydim is an integer, the y dimension of the drawing so we know when the
        last line is to stop drawing.
    :param space: space is an integer, holds the desired spacing of the dots when drawing.
    :param size: size is an integer, holds the desired size of the dots when drawing.

    :return: draws the image based off of the xpm file and finishes the function.
    
    counter - an integer that keeps count of the amount of lines drawn. Is used
        for calculations when drawing.
    position - a variable that holds the turtle's calculated starting position
        when drawing.
    """ 
    print("plotting...") #tell the user that turtle is currently plotting
    counter = 0 #create variable counter and assign to a value of 0
    
    #make the turtle go to the coordinates of xdim*space/2, ydim*-space/2
    #this coordinate places the turtle at the perfect position bottom right to create
    #a centered upside down drawing
    t.goto(int(xdim)*space/2,int(ydim)*-space/2)
    position = t.pos() #assign the current position coordinates to variable position
    for i in image: #iterate through each index (line) of the array image
        counter += space #add the value of space to the counter
        #go to the value of counter above the original starting point
        t.goto(position[0],position[1]+counter)
        for x in i: #iterate through each element in the current line
            pointc = colour[x] #get the corresponding colour of the current symbol
            t.dot(size,pointc) #create the dot with the desired size and corresponding colour
            t.backward(space) #move backwards (to the left) by the value of space
def ninetygraph(xdim,ydim,space,size):
    """
    ninetygraph takes the x and y dimensions, space and size of dots, and draws the
        image at a rotated 90 degree angle.
    :param xdim: xdim is an integer, the x dimension of the drawing so we know when to
        stop drawing for a line.
    :param ydim: ydim is an integer, the y dimension of the drawing so we know when the
        last line is to stop drawing.
    :param space: space is an integer, holds the desired spacing of the dots when drawing.
    :param size: size is an integer, holds the desired size of the dots when drawing.

    :return: draws the image based off of the xpm file and finishes the function.
    
    counter - an integer that keeps count of the amount of lines drawn. Is used
        for calculations when drawing.
    position - a variable that holds the turtle's calculated starting position
        when drawing.
    """ 
    print("ploting...") #tell the user that turtle is currently plotting
    counter = 0 #create variable counter and assign to a value of 0
    
    #make the turtle go to the coordinates of xdim*space/2, ydim*space/2
    #this coordinate places the turtle at the perfect position top right to create
    #a centered 90 degree drawing
    t.goto(int(xdim)*space/2,int(ydim)*space/2)
    position = t.pos() #assign the current position coordinates to variable position
    t.right(90) #turn the turtle object right by 90 degrees so it faces down
    for i in image: #iterate through each index (line) of the array image
        counter += space #add the value of space to the counter
        #go to the value of counter to the left of the original starting point
        t.goto(position[0]-counter,position[1])
        for x in i: #iterate through each element in the current line
            pointc = colour[x] #get the corresponding colour of the current symbol
            t.dot(size,pointc) #create the dot with the desired size and corresponding colour
            t.forward(space) #move forward (downwards) by the value of space
def twoseventygraph(xdim,ydim,space,size):
    """
    twoseventygraph takes the x and y dimensions, space and size of dots, and draws the
        image at a rotated 270 degree angle.
    :param xdim: xdim is an integer, the x dimension of the drawing so we know when to
        stop drawing for a line.
    :param ydim: ydim is an integer, the y dimension of the drawing so we know when the
        last line is to stop drawing.
    :param space: space is an integer, holds the desired spacing of the dots when drawing.
    :param size: size is an integer, holds the desired size of the dots when drawing.

    :return: draws the image based off of the xpm file and finishes the function.
    
    counter - an integer that keeps count of the amount of lines drawn. Is used
        for calculations when drawing.
    position - a variable that holds the turtle's calculated starting position
        when drawing.
    """ 
    print("ploting...") #tell the user that turtle is currently plotting
    counter = 0  #create variable counter and assign to a value of 0
    
    #make the turtle go to the coordinates of xdim*-space/2, ydim*-space/2
    #this coordinate places the turtle at the perfect position bottom left to create
    #a centered 270 degree drawing
    t.goto(int(xdim)*-space/2,int(ydim)*-space/2)
    position = t.pos() #assign the current position coordinates to variable position
    t.left(90) #turn the turtle object left by 90 degrees so it faces up
    for i in image: #iterate through each index (line) of the array image
        counter += space #add the value of space to the counter
        #go to the value of counter to the right of the original starting point
        t.goto(position[0]+counter,position[1])
        for x in i: #iterate through each element in the current line
            pointc = colour[x] #get the corresponding colour of the current symbol
            t.dot(size,pointc) #create the dot with the desired size and corresponding colour
            t.forward(space) #move forward (upwards) by the value of space

t = turtle.Turtle() #for easier coding while using functions in turtle

#the three files used for the assignment
#file = "smiley_emoji_mod.xpm"
#file = "cool_smiley_mod.xpm"
#file = "rocky_bullwinkle_mod.xpm"

#ask the user for file input
print("""What file would you like to draw?
(1)'rocky_bullwinkle_mod.xpm' (2)'smiley_emoji_mod.xpm'
(3)'cool_smiley_mod.xpm'  or  (4) 'insert the file name of your choosing'""")

file = input("") #take in the input as a string
if file == '1': #if the input is "1" then the file is rocky_bulliwnkle_mod.xpm
    file = "rocky_bullwinkle_mod.xpm"
elif file == '2': #if the input is "2" then the file is smiley_emoji_mod.xpm
    file = "smiley_emoji_mod.xpm"
elif file == '3': #if the input is "3" then the file is cool_smiley_mod.xpm
    file = "cool_smiley_mod.xpm"
else: 
    #and if the input is not "1" "2" or "3" then the file name would be what was typed
    pass
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

t.penup() #stops the turtle object from drawing lines
t.hideturtle() #hides the turtle object from view
turtle.tracer(0,0) #stops tracing the turtle for faster drawing

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

o = 1 #create variable o and assigne a value of 1
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
        uprightgraph(xdim,ydim,space,size) #call uprightgraph function

    elif rotation == 180: #if the user inputted 180
        upsidedowngraph(xdim,ydim,space,size) #call upsidedowngraph function

    elif rotation == 90: #if the user inputted 90
        ninetygraph(xdim,ydim,space,size) #call ninetygraph function

    elif rotation == 270: #if the user inputted 270
        twoseventygraph(xdim,ydim,space,size) #call twoseventygraph function

    else: #if the user gave a response unexpected
        #ask for valid user input again
        print("You did not give a valid rotation number, please try again")
        p = 1 #assign p to a value of 1 which continues the loop
    
turtle.update() #update the turtle once it's finished drawing to see the final result
#tell the user that turtle has finished drawing.
print("Done! Please check to see if the Turtle graphics window has opened.")
