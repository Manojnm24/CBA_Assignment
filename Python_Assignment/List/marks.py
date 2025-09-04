#Marks management: accept 5 marks and display highest, lowest, and average.

marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")
print(f"Average: {sum(marks)/len(marks):.2f}")


# Enter mark 1: 95
# Enter mark 2: 88
# Enter mark 3: 90
# Enter mark 4: 82
# Enter mark 5: 80
# Highest: 95.0
# Lowest: 80.0
# Average: 87.00