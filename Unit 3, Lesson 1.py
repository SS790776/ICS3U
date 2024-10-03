count = 0
progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."
#iterate through each character, if you see a space then add 1 to the counter
for x in progname:
    if x == " ":
        count +=1
print(count)
