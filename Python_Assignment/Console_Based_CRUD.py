students = []  # list to store student records

# Function to add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    print("\n✅ Student added successfully!\n")

# Function to display all students
def display_students():
    if not students:
        print("\n⚠️ No student records found.\n")
        return
    print("\n📋 Student Records:")
    print("-" * 40)
    for s in students:
        print(f"Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")
    print("-" * 40)

# Function to search student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"\n🔎 Found Student: Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}\n")
            return
    print("\n❌ Student not found.\n")

# Function to update student
def update_student():
    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s['roll'] == roll:
            print("\nEnter new details (leave blank to keep unchanged):")
            new_name = input("New Name: ")
            new_age = input("New Age: ")
            new_course = input("New Course: ")

            if new_name:
                s['name'] = new_name
            if new_age:
                s['age'] = new_age
            if new_course:
                s['course'] = new_course

            print("\n✅ Student updated successfully!\n")
            return
    print("\n❌ Student not found.\n")

# Function to delete student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("\n🗑️ Student deleted successfully!\n")
            return
    print("\n❌ Student not found.\n")

# Menu-driven program
def menu():
    while True:
        print("\n====== Student Management System ======")
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
            print("\n👋 Exiting... Thank you!\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()
