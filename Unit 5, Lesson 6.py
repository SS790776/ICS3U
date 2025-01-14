def triangle (ch, num):
    if (num == 1): # base case
        print(ch)
        return

    else: # recursive step
        print(ch*num)
        triangle(ch, num - 1)



c = "#"
n = 7
triangle(c, n)
