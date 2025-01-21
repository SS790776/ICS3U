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

def merge(arr, arr2, arr3, arr4, left, mid, right):
    """
    This function merges arrays, as a part of the mergesort algorithm.
        This function is optimized to swap and merge multiple arrays following the 
        same order of the exp date array being sorted.
    :param arr: The primary array used for sorting (expdate).
    :param arr2: Second array that follows the corresponding sorting of arr (name).
    :param arr3: Third array that follows the corresponding sorting of arr (cctype).
    :param arr4: Fourth array that follows the corresponding sorting of arr (ccnumber).
    :param left: Leftmost index of the subarray to be merged.
    :param mid: Middle index, dividing the subarrays.
    :param right: Rightmost index of the subarray to be merged.
    """
    n1 = mid - left + 1 # Length of the first subarray
    n2 = right - mid # Length of the second subarray

    # Create temp arrays
    L,L2,L3,L4 = [0] * n1, [0] * n1, [0] * n1, [0] * n1
    R,R2,R3,R4 = [0] * n2, [0] * n2, [0] * n2, [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i] # Primary array left half
        L2[i] = arr2[left + i] # Array 2 left half (replicate)
        L3[i] = arr3[left + i] # Array 3 left half (replicate)
        L4[i] = arr4[left + i] # Array 4 left half (replicate)
    
    for j in range(n2):
        R[j] = arr[mid + 1 + j] # Primary array right half
        R2[j] = arr2[mid + 1 + j] # Array 2 right half (replicate)
        R3[j] = arr3[mid + 1 + j] # Array 3 right half (replicate)
        R4[j] = arr4[mid + 1 + j] # Array 4 right half (replicate)

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]: #compare the elements and merge in sorted order
            arr[k] = L[i]
            arr2[k] = L2[i] #replicate
            arr3[k] = L3[i] #replicate
            arr4[k] = L4[i] #replicate
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j] #replicate
            arr3[k] = R3[j] #replicate
            arr4[k] = R4[j] #replicate
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i] #replicate
        arr3[k] = L3[i] #replicate
        arr4[k] = L4[i] #replicate
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j] #replicate
        arr3[k] = R3[j] #replicate
        arr4[k] = R4[j] #replicate
        j += 1
        k += 1

def merge_sort(arr,arr2,arr3,arr4,left,right):
    """
    This function sorts an array in ascending order using the merge sort algorithm
    and swaps elements in the date array correspondingly.

    :param arr: The expiry date array to sort.
    :param arr2: The name array that is swapped correspondingly
    :param arr3: The credit card type array that is swapped correspondingly
    :param arr4: The credit card number array that is swapped correspondingly 
    :param left: Leftmost index of the array.
    :param right: Rightmost index of the array.
    :return: The sorted expdate, name, cctype, and ccnumber arrays.
    """
    if left < right:
        mid = (left + right) // 2 #find the middle point

        # using recursion, sort the first and second halves
        merge_sort(arr, arr2, arr3, arr4, left, mid)
        merge_sort(arr, arr2, arr3, arr4, mid + 1, right)
        # Merge the sorted halves
        merge(arr, arr2, arr3, arr4, left, mid, right)
    
def status_check(expdate,status):
    """
    This function will go through each exp date in the array and check whether or not
    the date is expired, close to expiry, or not expired. Then append the status 
    into the status array accordingly
    
    :param expdate: The expiry date array
    :param status: The array containing the status data
    
    """
    for i in expdate: #iterate through every expiry date
        if i <202501: #if the date is earlier than jan 2025
            status.append("EXPIRED") #it is expired
        elif i ==202501: #if the date is during jan 2025
            status.append("RENEW IMMEDIATELY") #renew immediately
        else: #if the date is after jan 2025
            status.append("NOT EXPIRED") #it is not expired

file = 'data.dat' #declare the file we are taking information from

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
        name.append(f"{n} {sn}") #add name and surname to name array, seperated by a comma
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

merge_sort(expdate,name,cctype,ccnumber,0,len(expdate)-1) 
#sort the expiry date array, and mimic the sorting in the other arrays corresponding to the expdate.
status_check(expdate,status)#make a status for every expiry date

try: #make a try and except in case opening the file goes wrong
    create = open('statussheet.txt',"w") #open/create the file "statussheet.txt"
    for i in range(len(expdate)): #iterate through every element in the expdate array
        if status[i] == "NOT EXPIRED": #if the status of the person we're on is "NOT EXPIRED" 
            break #Then we break the for loop because we don't want to write any not exepired credit cards into the sheet.
        else: #if the status is "EXPIRED" or "RENEW IMMEDIATELY"
            line = ("%-38s %-13s %s %s %s" %(name[i]+":",cctype[i],ccnumber[i],expdate[i],status[i])) + "\n"
            create.write(line) #then write the line "Name: cctype, ccnumber, expdate, and status.
    create.close() #close the file as we're doing writing now.
except IOError as err: #if there is an input output error, catch it
    print("IOError: ", err) #print out the error
     exit() #stop the program
except OSError as err2:  #if there is an operating system error, catch it
    print("OSError: ", err2) #print out the error
     exit() #stop the program
except PermissionError as err3:  #if there is a permission error, catch it
    print("PermissionError: ", err3) #print out the error
     exit() #stop the program
print("The file 'statussheet.txt' has successfully been created, please check your folders")
