#Electricity bill calculator: units ≤100 → ₹5/unit, 101–300 → ₹7/unit, >300 → ₹10/unit.

units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

print(f"Total bill: ₹{bill}")

# Enter units consumed: 200
# Total bill: ₹1400

# Enter units consumed: 350
# Total bill: ₹3500

# Enter units consumed: 50
# Total bill: ₹250