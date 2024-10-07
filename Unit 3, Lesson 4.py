ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]

total = [] #set variable
for x in (ar2): #loop through the 3 arrays
    temp = 0 #reset temp to 0 for each array
    for i in (x):#loop through each element in the current array
        temp += int(i) #add it to temp variable
    total.append(temp)#add temp (which would be the total of the numbser in the array) to the total

print(total) #print [16,26,10]
