#Count how many vowels are in a sentence.

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print(f"Number of vowels: {count}")



# Enter a sentence: hello cba
# Number of vowels: 3

# Enter a sentence: earth is where we live
# Number of vowels: 8