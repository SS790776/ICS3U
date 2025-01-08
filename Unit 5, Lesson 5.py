def fib(n):
  pass  
    

p = 0
try:
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
except TypeEror as Err:
    print("Please input a valid whole number")
    p = 0
    
    
print(fib(n), end = " ")
print()
