import time

def fibIt(n):
    fib = [0,1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]

def fibRe(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibRe(n-1) + fibRe(n-2)

#allow user to enter how many fibonacci terms they want and print those number both using iteration and recursion
running = True
while running:
    while True:
        n = input("number of fibonacci terms wanted\n")
        try:
            n = int(n)
            if 3 <= n <= 30:
                break
            elif n == 0:
                running = False
                break
            else:
                print("integer must be between 3 and 30 inclusively")
        except ValueError as e:
            print("value must be integer, error =", e)
    
    print("iteratively:")
    for i in range(0, n+1):
        print(fibIt(i))
    
    print("\nrecursively:")
    for i in range(0, n+1):
        print(fibRe(i))


#compare times for 10 and 20 numbers
start = time.time()
for i in range(0, 11):
    fibIt(i)
print(f"calculating first 10 fibonacci numbers using iteration took {round(time.time()-start, 6)} seconds")
start = time.time()
for i in range(0, 11):
    fibRe(i)
print(f"calculating first 10 fibonacci numbers using recursion took {round(time.time()-start, 6)} seconds")
start = time.time()
for i in range(0, 21):
    fibIt(i)
print(f"calculating first 20 fibonacci numbers using iteration took {round(time.time()-start, 6)} seconds")
start = time.time()
for i in range(0, 21):
    fibRe(i)
print(f"calculating first 20 fibonacci numbers using recursion took {round(time.time()-start, 6)} seconds")