#Mask email IDs: "john.doe@gmail.com" → "j***@gmail.com".

email = input("Enter your email: ")
username, domain = email.split("@")
masked = username[0] + "***"
print(f"Masked Email: {masked}@{domain}")

# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Strings$ python3 email.py
# Enter your email: manoj@gmail.com
# Masked Email: m***@gmail.com