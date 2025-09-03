#Prime number checker for given input.

num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 prime.py
# Enter a number: 5
# 5 is a prime number
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 prime.py
# Enter a number: 16
# 16 is not a prime number
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ 