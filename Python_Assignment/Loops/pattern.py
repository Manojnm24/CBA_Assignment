#Create a pattern to print a triangle of stars (user decides rows).

rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)

# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 pattern.py
# Enter number of rows: 5
# *
# **
# ***
# ****
# *****
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 pattern.py
# Enter number of rows: 7
# *
# **
# ***
# ****
# *****
# ******
# *******
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ 