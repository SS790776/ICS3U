def printIt(sorted):
    for i in range(40):
        if i % 10 == 0:
            print("\n")
            print(words[i], end = " ")
        else:
            print(words[i], end = " ")

def swap(words,i,j):
    temp = words[i]
    words[i] = words[j]
    words[j] = temp
    return words
def sort(words):
    
    for i in range(1,len(words)):
        for j in range(len(words)-1):
            if words[i] < words[j]:
                words = swap(words,i,j)
    return words

try:
    file = 'words40.dat'
    fh = open(file, "r")
    words = []
    for i in range(40):
        temp = fh.readline()
        temp = temp.strip()
        words.append(temp)
    sorted = sort(words)
    printIt(sorted)

    
    fh.close() #close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print 
