import csv
import os

FILE_NAME = "library_books.csv"

# Ensure CSV file exists with headers
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["BookID", "Title", "Author", "Year", "Status"])  # header row

# Add a new book
def add_book():
    bookid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    year = input("Enter Year: ")
    status = "Available"
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([bookid, title, author, year, status])
    print("\n✅ Book added successfully!\n")

# View all books
def display_books():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n⚠️ No book records found.\n")
            return
        print("\n📚 Library Book Records:")
        print("-" * 70)
        for row in rows:
            print(f"BookID: {row['BookID']} | Title: {row['Title']} | Author: {row['Author']} | Year: {row['Year']} | Status: {row['Status']}")
        print("-" * 70)

# Search books by Author or Title
def search_books():
    keyword = input("Enter Author or Title to Search: ").lower()
    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if keyword in row['Author'].lower() or keyword in row['Title'].lower():
                print(f"\n🔎 Found: BookID: {row['BookID']}, Title: {row['Title']}, Author: {row['Author']}, Year: {row['Year']}, Status: {row['Status']}")
                found = True
    if not found:
        print("\n❌ No book found with that author or title.\n")

# Update book status (Borrow/Return)
def update_status():
    bookid = input("Enter Book ID to Update Status: ")
    updated = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BookID'] == bookid:
                print(f"Current Status: {row['Status']}")
                if row['Status'] == "Available":
                    new_status = "Borrowed"
                else:
                    new_status = "Available"
                row['Status'] = new_status
                updated = True
            rows.append(row)
    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["BookID", "Title", "Author", "Year", "Status"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n✅ Book status updated successfully!\n")
    else:
        print("\n❌ Book not found.\n")

# Delete a book entry
def delete_book():
    bookid = input("Enter Book ID to Delete: ")
    deleted = False
    rows = []
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['BookID'] == bookid:
                deleted = True
            else:
                rows.append(row)
    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["BookID", "Title", "Author", "Year", "Status"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n🗑️ Book deleted successfully!\n")
    else:
        print("\n❌ Book not found.\n")

# Menu-driven program
def menu():
    init_file()
    while True:
        print("\n====== Library Book Records Management (CSV) ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books by Author/Title")
        print("4. Update Book Status (Borrow/Return)")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            update_status()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("\n👋 Exiting... Data saved in library_books.csv\n")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.\n")

# Run the project
if __name__ == "__main__":
    menu()
