#A shopkeeper wants to generate a bill: items (key) → price (value). Display total cost.

items = {
    "milk": 40,
    "bread": 25,
    "eggs": 60
}

total = 0
for item in items:
    print(f"{item}: ₹{items[item]}")
    total += items[item]

print(f"Total bill: ₹{total}")


# milk: ₹40
# bread: ₹25
# eggs: ₹60
# Total bill: ₹125