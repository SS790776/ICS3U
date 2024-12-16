def printIt(sorted):
    for i in range(40):
        if i % 10 == 0: #if the remainder of i divided by 10 is 0
            print("\n") #create newline
            print(words[i], end = " ")
        else:
            print(words[i], end = " ")

def swap(words,i,j):
    temp = words[i] #create temp
    words[i] = words[j] #swap for j into i
    words[j] = temp #swap for i into j
    return words
def sort(words):
    
    for i in range(1,len(words)):
        for j in range(len(words)-1):
            if words[i] < words[j]:
                words = swap(words,i,j)
    return words

try:
    file = 'words40.dat'
    fh = open(file, "r")#open file
    words = []#create words array
    for i in range(40): #iterate through each word
        temp = fh.readline() #read the next word
        temp = temp.strip()#strip of newline characters
        words.append(temp) #append to words
    sorted = sort(words) #sort it
    printIt(sorted) #print it formmated

    
    fh.close() #close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print 
