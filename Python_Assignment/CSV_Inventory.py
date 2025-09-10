import csv
import os

FILE_NAME = "inventory.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ItemID", "ItemName", "Quantity", "Price", "Supplier"])  # header row

# Add new item to inventory
def add_item():
    itemid = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    quantity = input("Enter Quantity: ")
    price = input("Enter Price: ")
    supplier = input("Enter Supplier: ")
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([itemid, name, quantity, price, supplier])
    print("\n✅ Item added to inventory!\n")

# Display stock report
def display_stock():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No inventory records found.\n")
            return
        print("\n📦 Inventory Stock Report:")
        print("-" * 70)
        for row in rows:
            print(f"ItemID: {row['ItemID']} | Name: {row['ItemName']} | Qty: {row['Quantity']} | Price: {row['Price']} | Supplier: {row['Supplier']}")
        print("-" * 70)

# Search item by name
def search_item():
    keyword = input("Enter Item Name to Search: ").lower()
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if keyword in row['ItemName'].lower():
                print(f"\n🔎 Found: ItemID: {row['ItemID']}, Name: {row['ItemName']}, Qty: {row['Quantity']}, Price: {row['Price']}, Supplier: {row['Supplier']}")
                found = True
    if not found:
        print("\n❌ No item found with that name.\n")

# Update quantity/price of an item
def update_item():
    itemid = input("Enter Item ID to Update: ")
    updated = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ItemID'] == itemid:
                print(f"Current Qty: {row['Quantity']}, Price: {row['Price']}")
                new_qty = input("New Quantity (leave blank to keep unchanged): ") or row['Quantity']
                new_price = input("New Price (leave blank to keep unchanged): ") or row['Price']
                row['Quantity'] = new_qty
                row['Price'] = new_price
                updated = True
            rows.append(row)
    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ItemID", "ItemName", "Quantity", "Price", "Supplier"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Item details updated!\n")
    else:
        print("\n❌ Item not found.\n")

# Delete item from inventory
def delete_item():
    itemid = input("Enter Item ID to Delete: ")
    deleted = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ItemID'] == itemid:
                deleted = True
            else:
                rows.append(row)
    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ItemID", "ItemName", "Quantity", "Price", "Supplier"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Item deleted from inventory!\n")
    else:
        print("\n❌ Item not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("\n====== Inventory Management System (CSV) ======")
        print("1. Add New Item")
        print("2. Display Stock Report")
        print("3. Search Item by Name")
        print("4. Update Quantity/Price")
        print("5. Delete Item")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_item()
        elif choice == '2':
            display_stock()
        elif choice == '3':
            search_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in inventory.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()
