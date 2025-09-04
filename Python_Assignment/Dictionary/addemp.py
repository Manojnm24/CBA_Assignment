#Update a dictionary of employees by adding new employee details.

employees = {
    "E101": "Manoj",
    "E102": "Bhoomi"
}

new_id = input("Enter new employee ID: ")
new_name = input("Enter employee name: ")

employees[new_id] = new_name
print("Updated employee list:", employees)

# Enter new employee ID: E103
# Enter employee name: Rakshitha
# Updated employee list: {'E101': 'Manoj', 'E102': 'Bhoomi', 'E103': 'Rakshitha'}