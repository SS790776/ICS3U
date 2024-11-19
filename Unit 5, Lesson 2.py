import turtle

t = turtle.Turtle()

file = "txt.txt"
array = [[]]
firstinf = []
try:
    fh = open(file, "r")
    firstinf = fh.readline()
    xdim, ydim, colournum = firstinf.split(" ")
    print(xdim, ydim, colournum)

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
    
    print(colour)
    
    image = [[""]*int(xdim)]*int(ydim)
    
    for i in range(int(ydim)):
        line = fh.readline()
        for x in range(int(xdim)):
            image[i][x] = line[x]
    print(image)

    fh.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)



