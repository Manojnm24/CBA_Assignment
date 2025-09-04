#Define a function to take a list and return the second-largest number.

def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print("Second Largest:", second_largest([10, 20, 30, 40, 30]))

#Second Largest: 30
