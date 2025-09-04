#A library wants to track how many books a user borrows. Write a program to ask the user for their name and number of books borrowed, and print a formatted receipt.

name=input("what is your name: ")
books=int(input("how many number of books did you borrow: "))
print(f"{name} has borrowed {books} Books from library.")

# what is your name: Manoj
# how many number of books did you borrow: 5
# Manoj has borrowed 5 Books from library.