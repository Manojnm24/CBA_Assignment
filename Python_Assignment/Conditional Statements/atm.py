#ATM machine: ask PIN. If correct, allow withdrawal, else block after 3 wrong attempts.

correct_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        print("Access granted. You may withdraw.")
        break
    else:
        attempts += 1
        print("Incorrect PIN.")

if attempts == 3:
    print("Card blocked due to 3 wrong attempts.")
    
    
# Enter PIN: 4321
# Incorrect PIN.
# Enter PIN: 7896
# Incorrect PIN.
# Enter PIN: 8745
# Incorrect PIN.
# Card blocked due to 3 wrong attempts.

# Enter PIN: 1234             
# Access granted. You may withdraw.
