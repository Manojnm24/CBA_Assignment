# Remove all negative numbers from a given list of integers.

numbers = [10, -5, 3, -2, 8, -7, 0]
positive_numbers = [num for num in numbers if num >= 0]
print("Without negatives:", positive_numbers)

#Without negatives: [10, 3, 8, 0]