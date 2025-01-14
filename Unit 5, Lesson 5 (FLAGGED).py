def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    result= fib(n-1) + fib(n-2)
    return result

p = 1
while p == 1:
    try:
        tn = int(input("Please input a whole number greater than 0: "))
        if tn >0:
            p=0
        else:
            p=1
    except ValueError as Err:
        print("ValueError:",Err)
        p = 1


for i in range(1,tn+1):
    print(fib(i),end=" ")
