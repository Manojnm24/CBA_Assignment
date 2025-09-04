#Create a function to calculate compound interest.

def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount

print("Compound Interest:", compound_interest(1000, 5, 2))

#Compound Interest: 1102.5
