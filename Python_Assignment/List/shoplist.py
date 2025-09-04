#Create a program to merge two shopping lists without duplicates.

list1 = ["milk", "bread", "eggs"]
list2 = ["eggs", "butter", "jam"]

merged = list(set(list1 + list2))
print("Merged list:", merged)


# Merged list: ['milk', 'bread', 'butter', 'eggs', 'jam']