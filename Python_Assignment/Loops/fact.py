#Factorial calculator using loop.

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")


# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 fact.py
# Enter a number: 6
# Factorial of 6 is 720
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 fact.py
# Enter a number: 9
# Factorial of 9 is 362880
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 fact.py
# Enter a number: 3
# Factorial of 3 is 6
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ 
