import csv
import os

FILE_NAME = "students.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["roll", "name", "age", "course"])  # header row

# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, age, course])

    print("\n✅ Student added successfully!\n")

# Display all students
def display_students():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No student records found.\n")
            return
        print("\n📋 Student Records:")
        print("-" * 50)
        for row in rows:
            print(f"Roll: {row['roll']} | Name: {row['name']} | Age: {row['age']} | Course: {row['course']}")
        print("-" * 50)

# Search student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['roll'] == roll:
                print(f"\n🔎 Found: Roll: {row['roll']}, Name: {row['name']}, Age: {row['age']}, Course: {row['course']}\n")
                return
    print("\n❌ Student not found.\n")

# Update student
def update_student():
    roll = input("Enter Roll Number to Update: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['roll'] == roll:
                print("\nEnter new details (leave blank to keep unchanged):")
                new_name = input("New Name: ") or row['name']
                new_age = input("New Age: ") or row['age']
                new_course = input("New Course: ") or row['course']
                row = {"roll": roll, "name": new_name, "age": new_age, "course": new_course}
                updated = True
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["roll", "name", "age", "course"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Student updated successfully!\n")
    else:
        print("\n❌ Student not found.\n")

# Delete student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['roll'] == roll:
                deleted = True
            else:
                rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["roll", "name", "age", "course"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Student deleted successfully!\n")
    else:
        print("\n❌ Student not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("\n====== Student Management System (CSV) ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in students.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()