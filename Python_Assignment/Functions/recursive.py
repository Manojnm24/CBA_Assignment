#Write a recursive function to calculate Fibonacci numbers

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")


# 0 1 1 2 3 5