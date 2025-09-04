#Store student names with their marks in a dictionary. Print topper’s name.

students = {
    "Manoj": 85,
    "Bhoomi": 92,
    "Rakshitha": 90,
    "Harshith": 88
}

topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")

#Topper: Bhoomi with 92 marks