# This code uses recursion to find the factorial of an input by the user
from time import perf_counter
t1 = perf_counter()

def factorial(x, m = 1):

    if m != x:
        k = factorial(x, m + 1)
    
    if m == x:
        return x
    
    else:
        return (k*m)




#Asks for input by user
number = 500

numberFactorial = factorial(number)

print(numberFactorial)

t2 = perf_counter()

print(t2 - t1)