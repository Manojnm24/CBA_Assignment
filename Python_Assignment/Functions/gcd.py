#Create a function to find the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD:", gcd(36, 60))

#GCD: 12

