"""
Sean S
11/20/2024
ICS3U 
U5 L2
    Variable dictionary
    t = turtle.turtle()
    file = "smiley_emoji_mod.xpm"
    array, holds array
"""

import turtle

t = turtle.Turtle()

file = "smiley_emoji_mod.xpm"
firstinf = []
try:
    fh = open(file, "r") #open file
    firstinf = fh.readline()
    xdim, ydim, colournum = firstinf.split(" ")

    colour = {
        
        }
    
    for x in range(int(colournum)):
        line = fh.readline()
        line.strip()
        symb, c, rainbow = line.split()
        
        if symb == "~":
            symb = " "
            colour.update({symb:rainbow})

        else:
            colour.update({symb:rainbow})
    
    
    
    image = []

    for i in range(int(ydim)):
        line = fh.readline()
        line = line.replace('\n', '')
        image.append(line)




    fh.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)

turtle.bgcolor("gray40")
t.penup()
t.hideturtle()
turtle.tracer(0,0)
print(colour)
print(image)
counter = 0
t.goto(int(xdim)*-5/2,int(ydim)*5/2)
position = t.pos()

for i in image:
    counter += 5
    t.goto(position[0],position[1]-counter)
    for x in i:
        pointc = colour[x]
        t.dot(5,pointc)
        t.forward(5)
        
turtle.update()
