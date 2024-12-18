"""
Sean S
12/16/2024
ICS3U 
Programming Assignment 4


Variable dictionary:
    arr - An array that contains the words or dates needed to be processed in functions
    date - An array of integers representing merged dates in YYYYMMDD format.
    words - An array of strings containing words from the Wordle archive.
    m - A string representing the month (eg. "Jan", "Feb").
    d - A string representing the day (eg. "01", "15").
    y - A string representing the year (eg. "2024").
    merged - An integer representing a merged date in YYYYMMDD format.
    low - The starting index for binary search.
    high - The ending index for binary search.
    target - The value being searched for in an array.
    size - The size of the array being sorted in exchange_sort.
    temp - A temporary variable used for swapping words in exchange_sort.
    temp2 - A temporary variable used for swapping dates in exchange_sort.
    dw - User input to decide whether to search by date or word.
    gety - User input for the year to search.
    getm - User input for the month to search.
    getd - User input for the day to search.
    gotd - The merged integer date based on user input.
    targword - A string that holds the desired word to be searched for.
    index - The index of the target value found in the array.
    sortedwords - An array, holding the sorted words.
    sorteddates - An array, holding the corresponding dates.
    u - A control variable for the program's main loop.
"""

def merge(m,d,y):
    """
    This function merges the month, date, and year into one number in YYYYMMDD format.

    :param m: The month as a string (eg. "Jan", "Feb").
    :param d: The day as a string (eg. "01", "15").
    :param y: The year as a string (eg. "2024").
    :return: An integer representing the merged date in YYYYMMDD format.
    """
    months = { #A dictionary for easier pulling of string to int
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
    m = m.capitalize() #capitalize for consistency
    num = y + months[m] + d #merge the variables together
    return int(num) #return the YYYYMMDD as an integer
    
def search(arr, low, high, target):
    """
    This function uses binary search to find a target value in a sorted array.

    :param arr: The sorted array to search, could be word or date array
    :param low: The starting index for the search.
    :param high: The ending index for the search.
    :param target: The value to search for in the array.
    :return: The index of the found target.
    """
    if high >= low: #if the highest index is greater than or equal to the lowest
        mid = (high + low) // 2 #get the mean (average)  and assign to mid

        if arr[mid] == target: #if mid is the target, the return it
            return mid
    
        elif arr[mid] > target: #if mid is greater than the target
            #recursion, put it back into the search function but the high is now mid-1
            return search(arr, low, mid - 1, target)
    

        else:#if mid is less than the target
            #recursion, put it back into the search function but the low is now mid+1
            return search(arr, mid + 1, high, target)
    
    else:
        #if we can't find the target, return -1
        return -1



def exchange_sort(arr,date):
    """
    This function sorts an array in ascending order using the exchange sort algorithm
    and swaps elements in the date array correspondingly.

    :param arr: The word array to sort.
    :param date: The date array that is swapped correspondingly
    :return: The sorted word array and date.
    """
    size = len(arr) #size is equal to the length of the array

    for i in range(size - 1): #iterate through size -1

        for j in range(i + 1, size): #iterate from i+1 to size

            if arr[i] > arr[j]: #if arr[i] is greater than arr[j]
                temp = arr[i] #make temp as arr[i]
                arr[i] = arr[j] #swap arr[j] into arr[i]
                arr[j] = temp #swap temp(arr[i]) into arr[j]
                temp2 = date[i] #make temp2 as date[i]
                date[i] = date[j] #swap date[j] into date[i]
                date[j] = temp2 #swap temp2 (date[i]) into date[j]
    return arr,date #return sorted arr, and corresponding date.




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
        date.append(merged) #add the merged date into the date array
    
    fh.close()#close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print out the error
    exit() #stop the program




u = 1 #create variable u and assign a value of 1
while u == 1: #while u has a value of 1
    #ask user if they want to search for date or words
    dw = input("do you want to search for date or words? (D/W): ") 
    
    if dw == "D" or dw == "d": #if the user inputted a variation of "D"
                
        #sort the dates chronologically and store into datesorteddates,  
        #while swapping words elements correspondingly
        datesorteddates, datesortedwords = exchange_sort(date,words)

        print("What date would you like to search?") #Ask for desired date
        gety = input("Please enter the year: ") #Ask for year
        #ask for month
        getm = input("Please enter the month using the first three letters (Eg.Jan): ")
        getd = input("Please enter the day: ") #ask for day
        gotd = merge(getm,getd,gety) #merge into YYYYMMDD format
        gotd = int(gotd) #turn into integer
        if gotd > 20240421: #if the date is greater than the latest records
            print("Our records only go until 20240421, Sorry.") #say that we don't have it
            exit() #exit the program
        elif gotd < 20210619: #if the date is less than the earliest records
            print("Our earliest records are 20210619, Sorry.") #say that we don't have it
            exit() #exit the program
        #get the index of the target date
        index = search(datesorteddates,0,len(datesorteddates),gotd) #find the index of the date
        if index == -1:
            print("date not found")
            print(date)
            exit()
        
        print(f"The word entered on {gotd} was {datesortedwords[index]}.") #output the corresponding word
        
        u = 0 #assign u to a value of 0 which exits the while loop
    elif dw == "W" or dw == "w": #if the user inputted a variation of "W"
        #sort the words alphabetically and store into sortedwords,  
        #while swapping date elements correspondingly
        sortedwords,sorteddates = exchange_sort(words,date)
        targword = input("Please enter the desired word: ") #ask for desired word
        targword = targword.upper() #make it uppercase
        #get index of target word
        index = search(sortedwords,0,len(sortedwords),targword) 
        if index == -1: #if the word doesn't exsist
            #say that it doesn't exsist
            print(f"The word {targword} was not found in the database.")
            exit() #exit the program
        print(f"The word {targword} was the solution on {date[index]}.") #ouput the corresponding date
        u = 0 #assign u to a value of 0 which exits the while loop
    else: #if the user input is a response that was not expected
        print("not a valid response, please try again") #ask for user input again
        u = 1 #assign u to a value of 1 which continues the loop
