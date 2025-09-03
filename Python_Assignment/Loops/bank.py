#Banking system: show balance every month for 12 months after adding 5% interest.

balance = float(input("Enter initial balance: "))
for month in range(1, 13):
    balance += balance * 0.05
    print(f"Month {month}: ₹{balance:.2f}")

# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Loops$ python3 bank.py
# Enter initial balance: 1000
# Month 1: ₹1050.00
# Month 2: ₹1102.50
# Month 3: ₹1157.62
# Month 4: ₹1215.51
# Month 5: ₹1276.28
# Month 6: ₹1340.10
# Month 7: ₹1407.10
# Month 8: ₹1477.46
# Month 9: ₹1551.33
# Month 10: ₹1628.89
# Month 11: ₹1710.34
# Month 12: ₹1795.86