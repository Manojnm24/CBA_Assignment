#A tuple stores (name, age). Write a program to filter all people above 18.

people = [("Manu", 20), ("Bhoomi", 19), ("Ravi", 25), ("Rakshitha", 16), ("Harshith",17)]

for name, age in people:
    if age > 18:
        print(f"{name} is above 18")


# Manu is above 18
# Bhoomi is above 18
# Ravi is above 18