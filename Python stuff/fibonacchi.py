n = 2
prev = 1
doublePrev = 0

for i in range(n-2):
    fib = prev + doublePrev
    doublePrev = prev
    prev = fib

if n == 1:
    fib = 0

if n == 2:
    fib = 1



print(fib)
