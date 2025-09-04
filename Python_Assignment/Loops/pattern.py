#Create a pattern to print a triangle of stars (user decides rows).

rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


# Enter number of rows: 5
# *
# **
# ***
# ****
# *****

# Enter number of rows: 7
# *
# **
# ***
# ****
# *****
# ******
# ******* 