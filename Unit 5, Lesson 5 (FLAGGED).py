def getInt(prompt):
    p = 0
    try:
        response = int(input(prompt))
        while p == 0:
            inp = int(input("Please input a whole number greater than 0: "))
            if inp <=0:
                print("Please input a valid whole number")
                p = 0
            else:
                p = 1
    except ValueError as Err:
        print("Please input a valid whole number")
        p = 0
        
    return response

def fib(n):
    for i in range(1, n + 1):
        print(fib(i), end = " ")

tn = getInt("Please input a whole number greater than 0: ")

fib(tn)
