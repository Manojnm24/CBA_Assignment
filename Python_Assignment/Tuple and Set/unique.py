#Write a program to count unique words in a paragraph using a set.

text = input("Enter a paragraph: ")
words = set(text.lower().split())
print(f"Unique words ({len(words)}):", words)

# Enter a paragraph: hello i m manoj,i m in seventh sem and going to next sem in few months.
# Unique words (13): {'months.', 'manoj,i', 'm', 'in', 'next', 'hello', 'going', 'seventh', 'i', 'to', 'sem', 'and', 'few'}