#Grocery store: store 10 items in a list and allow the user to search if an item exists.

items = ["rice", "milk", "bread", "eggs", "oil", "sugar", "salt", "tea", "coffee", "butter"]
search = input("Enter item to search: ")

if search in items:
    print(f"{search} is available.")
else:
    print(f"{search} is not in stock.")

# Enter item to search: icecream
# icecream is not in stock.

# Enter item to search: milk
# milk is available.