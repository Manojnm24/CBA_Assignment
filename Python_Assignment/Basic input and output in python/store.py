#An online store applies discounts: if purchase > 5000, give 20% off, else 10%. Write code for it.

itemcost = float(input("enter the cost: "))
if itemcost>5000:
    print(f"cost {itemcost} after 20% discount total amout is {itemcost-(itemcost*0.20)} ")
else:
    print(f"cost {itemcost} after 10% discount total amout is {itemcost-(itemcost*0.10)}")
    
    
# enter the cost: 2000
# cost 2000.0 after 10% discount total amout is 1800.0

# enter the cost: 10000
# cost 10000.0 after 20% discount total amout is 8000.0 