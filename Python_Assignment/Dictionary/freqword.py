#Write a program to count the frequency of characters in a word.

word = input("Enter a word: ")
freq = {}

for char in word:
    freq[char] = freq.get(char, 0) + 1

print("Character frequencies:", freq)

# Enter a word: hello
# Character frequencies: {'h': 1, 'e': 1, 'l': 2, 'o': 1}