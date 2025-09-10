import csv
import os

FILE_NAME = "employees.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["EmpID", "Name", "Department", "Salary", "Contact"])  # header row

# Add employee
def add_employee():
    empid = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = input("Enter Salary: ")
    contact = input("Enter Contact: ")
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([empid, name, dept, salary, contact])
    print("\n✅ Employee added successfully!\n")

# Display all employees
def display_employees():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No employee records found.\n")
            return
        print("\n📋 Employee Records:")
        print("-" * 65)
        for row in rows:
            print(f"EmpID: {row['EmpID']} | Name: {row['Name']} | Department: {row['Department']} | Salary: {row['Salary']} | Contact: {row['Contact']}")
        print("-" * 65)

# Search employees by Department
def search_department():
    dept = input("Enter Department to Search: ")
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Department'].lower() == dept.lower():
                print(f"\n🔎 Found: EmpID: {row['EmpID']}, Name: {row['Name']}, Salary: {row['Salary']}, Contact: {row['Contact']}")
                found = True
    if not found:
        print("\n❌ No employee found in that department.\n")

# Update salary of an employee
def update_salary():
    empid = input("Enter Employee ID to Update Salary: ")
    updated = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['EmpID'] == empid:
                print(f"Current Salary: {row['Salary']}")
                new_salary = input("Enter New Salary: ") or row['Salary']
                row['Salary'] = new_salary
                updated = True
            rows.append(row)
    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["EmpID", "Name", "Department", "Salary", "Contact"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Employee salary updated successfully!\n")
    else:
        print("\n❌ Employee not found.\n")

# Delete an employee
def delete_employee():
    empid = input("Enter Employee ID to Delete: ")
    deleted = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['EmpID'] == empid:
                deleted = True
            else:
                rows.append(row)
    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["EmpID", "Name", "Department", "Salary", "Contact"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Employee deleted successfully!\n")
    else:
        print("\n❌ Employee not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("\n====== Employee Directory System (CSV) ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employees by Department")
        print("4. Update Employee Salary")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_department()
        elif choice == '4':
            update_salary()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in employees.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()
