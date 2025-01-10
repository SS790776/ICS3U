def triangle (ch, num):

  if (num>=7): # base case
    print(ch)

    return
  else: # recursive step
    triangle(ch, num + 1)
  print(ch*num)
  return


c = "#"
n = 7
triangle(c, n)
