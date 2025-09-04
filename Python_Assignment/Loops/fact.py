#Factorial calculator using loop.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")



# Enter a number: 6
# Factorial of 6 is 720

# Enter a number: 9
# Factorial of 9 is 362880

# Enter a number: 3
# Factorial of 3 is 6

