items = []
howmany = int(input("How many items are you entering? "))
#loop for the value of howmany. every time they enter a string, store it in a temperary variable and append it to the items array.
for x in range(howmany):
    temp = input(f"{x+1}: Enter item: ")
    items.append(temp)
    
print(f"You have entered {len(items)} items!")#len = elements in items
for x in items:
    print(x)
