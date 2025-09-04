#Create a dictionary of products and prices. Ask user for product name → show price.

products = {
    "milk": 40,
    "bread": 25,
    "eggs": 60,
    "butter": 80
}

item = input("Enter product name: ").lower()

if item in products:
    print(f"Price of {item}: ₹{products[item]}")
else:
    print("Product not found.")


# Enter product name: milk
# Price of milk: ₹40