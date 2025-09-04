# Write a function to check if a number is Armstrong or not.

def is_armstrong(num):
    power = len(str(num))
    total = sum(int(digit) ** power for digit in str(num))
    return total == num

print("Armstrong:", is_armstrong(152))

#Armstrong: True (153)
#Armstrong: False (152)


