#Keep track of registered vehicle numbers using a set. Prevent duplicates.

vehicles = set()

for _ in range(5):
    number = input("Enter vehicle number: ")
    if number in vehicles:
        print("Already registered.")
    else:
        vehicles.add(number)
        print("Vehicle registered.")


# Enter vehicle number: KA02EJ2426
# Vehicle registered.
# Enter vehicle number: KA02EJ2426
# Already registered.
# Enter vehicle number: KA02NM2004
# Vehicle registered.
# Enter vehicle number: KA05PM9346
# Vehicle registered.
# Enter vehicle number: KA02NM2004
# Already registered.