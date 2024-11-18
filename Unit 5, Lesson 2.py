import turtle

t = turtle.Turtle()

file = "txt.txt"
array = [[]]
firstinf = []
try:
    fh = open(file, "r")
    firstinf = fh.readline()
    fh.close()
except OSError as err:
    print("OSError: ", err)
except EOFError as err2:
    print("EOFError: ", err2)
print(firstinf)

xdim, ydim, colournum = firstinf.split(" ")
print(xdim, ydim, colournum)


