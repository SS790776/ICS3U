"""
Sean S
12/16/2024
ICS3U 
Programming Assignment 4

Variable dictionary:
    variable - description
"""

def merge(m,d,y):
    """
    this function takes the month, date, and year, and merges it into one number
    :param variable: description

    :return: description
    
    variable - description.

    """
    months = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    m = m.capitalize()
    num = y + months[m] + d
    return int(num)
    
def search(arr, low, high, target):
    """
    this function takes x, and does y, and returns z
    :param variable: description

    :return: description
    
    variable - description.

    """ 
    if high >= low:
    
        mid = (high + low) // 2

        if arr[mid] == target:
            return mid
    
        elif arr[mid] > target:
            return search(arr, low, mid - 1, target)
    

        else:
            return search(arr, mid + 1, high, target)
    
    else:
        return -1



def exchange_sort(arr,date):
    """
    this function takes x, and does y, and returns z
    :param variable: description

    :return: description
    
    variable - description.

    """ 
    size = len(arr)

    for i in range(size - 1):

        for j in range(i + 1, size):

            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                temp2 = date[i]
                date[i] = date[j]
                date[j] = temp2
    return arr,date




print("You have entered the wordle archives...")

file = 'wordle.dat'

date = [] #create the array to store the merged dates
words = [] #create array to store the words

try: #make a try and except in case opening the file goes wrong
    fh = open(file, "r") #open the file
    for i in range(1038):
        line = fh.readline() #assign line to the next line of the file
        line = line.strip() #clear line of "\n" characters
        #split the line and assign into the month, day, year, and word
        m, d, y, w = line.split()
        words.append(w) #add word to words array
        merged = merge(m,d,y) #merge the month, date,and year into one number
        date.append(merged) #
    
    fh.close()#close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print out the error
    exit() #stop the program

sortedwords,sorteddates = exchange_sort(words,date) #sort the words alphabetically and store into sortedwords

u = 1 #create variable u and assign a value of 1
while u == 1: #while u has a value of 1
    #ask user if they want to search for date or words
    dw = input("do you want to search for date or words? (D/W): ") 
    
    if dw == "D" or dw == "d": #if the user inputted a variation of "L"
        print("What date would you like to search?")
        gety = input("Please enter the year: ")
        getm = input("Please enter the month using the first three letters (Eg.Jan): ")
        getd = input("Please enter the day: ")
        gotd = merge(getm,getd,gety)
        gotd = int(gotd)
        if gotd > 20240421:
            print("Our records only go until 20240421, Sorry.")
            exit()
        elif gotd < 20210619:
            print("Our earliest records are 20210619, Sorry.")
            exit()
        index = search(sorteddates,0,len(sorteddates),gotd)

        
        print(f"The word entered on {gotd} was {words[index]}.")
        u = 0 #assign u to a value of 0 which exits the while loop
    elif dw == "W" or dw == "w": #if the user inputted a variation of "W"
        targword = input("Please enter the desired word: ")
        targword = targword.upper()
        index = search(sortedwords,0,len(sortedwords),targword)
        if index == -1:
            print("The word {targword} was not found in the database.")
            exit()
        print(f"The word {targword} was the solution on {date[index]}.")
        u = 0 #assign u to a value of 0 which exits the while loop
    else: #if the user input is a response that was not expected
        print("not a valid response, please try again") #ask for user input again
        u = 1 #assign u to a value of 1 which continues the loop
