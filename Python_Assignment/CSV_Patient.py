import csv
import os

FILE_NAME = "patients.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["PatientID", "Name", "Age", "Disease", "DoctorAssigned"])  # header row

# Add a new patient record
def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Assigned: ")
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pid, name, age, disease, doctor])
    print("\n✅ Patient record added successfully!\n")

# View all patients
def display_patients():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No patient records found.\n")
            return
        print("\n🩺 Patient Records:")
        print("-" * 70)
        for row in rows:
            print(f"PatientID: {row['PatientID']} | Name: {row['Name']} | Age: {row['Age']} | Disease: {row['Disease']} | DoctorAssigned: {row['DoctorAssigned']}")
        print("-" * 70)

# Search patient by DoctorAssigned
def search_patient_by_doctor():
    doctor = input("Enter Doctor Assigned to Search: ").lower()
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if doctor in row['DoctorAssigned'].lower():
                print(f"\n🔎 Found: PatientID: {row['PatientID']}, Name: {row['Name']}, Age: {row['Age']}, Disease: {row['Disease']}")
                found = True
    if not found:
        print("\n❌ No patients found for the given doctor.\n")

# Update patient details
def update_patient():
    pid = input("Enter Patient ID to Update: ")
    updated = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['PatientID'] == pid:
                print("Enter new details (leave blank to keep unchanged):")
                new_name = input("New Name: ") or row['Name']
                new_age = input("New Age: ") or row['Age']
                new_disease = input("New Disease: ") or row['Disease']
                new_doctor = input("New Doctor Assigned: ") or row['DoctorAssigned']
                row = {
                    "PatientID": pid,
                    "Name": new_name,
                    "Age": new_age,
                    "Disease": new_disease,
                    "DoctorAssigned": new_doctor
                }
                updated = True
            rows.append(row)
    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["PatientID", "Name", "Age", "Disease", "DoctorAssigned"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Patient details updated!\n")
    else:
        print("\n❌ Patient not found.\n")

# Delete patient record
def delete_patient():
    pid = input("Enter Patient ID to Delete: ")
    deleted = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['PatientID'] == pid:
                deleted = True
            else:
                rows.append(row)
    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["PatientID", "Name", "Age", "Disease", "DoctorAssigned"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Patient record deleted!\n")
    else:
        print("\n❌ Patient not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("\n====== Patient Record System (CSV) ======")
        print("1. Add Patient Record")
        print("2. View All Patients")
        print("3. Search Patient by DoctorAssigned")
        print("4. Update Patient Details")
        print("5. Delete Patient Record")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_patient()
        elif choice == '2':
            display_patients()
        elif choice == '3':
            search_patient_by_doctor()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in patients.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()
