#Railway reservation: if age < 5 → free, 5–60 → full ticket, >60 → half ticket.

age = int(input("Enter age: "))

if age < 5:
    print("Ticket: Free")
elif age <= 60:
    print("Ticket: Full fare")
else:
    print("Ticket: Half fare")
    
 
# Enter age: 4
# Ticket: Free
 
# Enter age: 55
# Ticket: Full fare
 
# Enter age: 85
# Ticket: Half fare