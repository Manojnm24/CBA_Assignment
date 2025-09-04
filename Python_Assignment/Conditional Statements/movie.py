#Movie ticket booking: if time < 17 hrs → matinee discount 30%, else full price.

time = int(input("Enter show time (24-hour format): "))
price = 200 

if time < 17:
    price *= 0.70  

print(f"Ticket price: ₹{price}")



# Enter show time (24-hour format): 15
# Ticket price: ₹140.0

# Enter show time (24-hour format): 22
# Ticket price: ₹200
 