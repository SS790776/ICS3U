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

def mergedate(m,y):
    """
    This function merges the month and year into one number in YYYYMM format.

    :param m: The month as a string (eg. "4").
    :param y: The year as a string (eg. "2024").
    :return: An integer representing the merged date in YYYYMM format.
    """
    if int(m) < 10: #if the month is 1 digit
        m = (f"0{m}") #add a zero before the digit
    num = y + m  #merge the variables together
    return int(num) #return the YYYYMMDD as an integer

def merge():
    pass

def merge_sort(expdate,name,cctype,ccnumber):
    """
    This function sorts an array in ascending order using the merge sort algorithm
    and swaps elements in the date array correspondingly.

    :param expdate: The expiry date array to sort.
    :param name: The name array that is swapped correspondingly
    :param cctype: The credit card type array that is swapped correspondingly
    :param ccnumber: The credit card number array that is swapped correspondingly 
    :return: The sorted expdate, name, cctype, and ccnumber arrays.
    """
    
def status_check(expdate,status):
    """
    This function will go through each exp date in the array and check whether or not
    the date is expired, close to expiry, or not expired.
    
    :param expdate: The expiry date array
    :param status: The array containing the status data
    
    """

file = 'data.dat'

expdate = [] #create the array to store the merged expiry dates in YYYYMM format
name = [] #create array to store the Name and Surname
cctype = [] #create the array to store the credit card type
ccnumber = [] #create the array to store the credit card number
status = [] #create the array to store the expiry status

try: #make a try and except in case opening the file goes wrong
    fh = open(file, "r") #open the file
    formatline = fh.readline()
    for i in range(200):
        line = fh.readline() #assign line to the next line of the file
        line = line.strip() #clear line of "\n" characters
        #split the line and assign into the name, surname, cctype, ccnumber, exp-mo,and exp-yr
        n, sn, ct, cn, em, ey = line.split(",")
        name.append(f"{n} {sn}") #add name and surname to name array, seperated by a space
        merged = mergedate(em,ey) #merge the month and year into one number YYYYMM format
        expdate.append(merged) #add the merged date into the date array
        cctype.append(ct) #add the credit card type into the cctype array
        ccnumber.append(cn) #add the credit card number into the ccnumber array
    
    fh.close()#close the file as we're done extracting information from it
except OSError as err: #if there is an operating system error, catch it
    print("OSError: ", err) #print out the error
    exit() #stop the program
except EOFError as err2: #if there is an error opening file error, catch it
    print("EOFError: ", err2) #print out the error
    exit() #stop the program

print(expdate,name,cctype,ccnumber)


#create = write(statussheet.txt,"w")
    
#create.close()
