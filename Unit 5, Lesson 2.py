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

"""
# Using arrays
colorDefs = [[0] * 2] * numColors # declare the array
for i in range(numColors):
   colorLine = fh.readline() # file handle must be open
   colorLine.strip() 
   sym, c, color = colorLine.split()
   # you need to insert code here to exchange
   # the tilde (~) for a space in the symbols!
   colorDefs[i][0] = sym
   colorDefs[i][1] = color

fh.close()
"""

