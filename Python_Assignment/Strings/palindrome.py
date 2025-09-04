#Check if a given sentence is a palindrome (ignoring spaces & case).

sentence = input("Enter a sentence: ")
cleaned = ''.join(sentence.lower().split())

if cleaned == cleaned[::-1]:
    print("It's a palindrome! ")
else:
    print("Not a palindrome.")



# Enter a sentence: madam
# It's a palindrome! 

# Enter a sentence: sir
# Not a palindrome.

