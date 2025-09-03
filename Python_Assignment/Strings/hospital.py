#A hospital system stores patient IDs as strings — validate that an ID always starts with "HOSP".

patient_id = input("Enter patient ID: ")

if patient_id.startswith("HOSP"):
    print("Valid Patient ID ")
else:
    print("Invalid Patient ID ")


# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Strings$ python3 hospital.py 
# Enter patient ID: abc1234
# Invalid Patient ID 
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Strings$ python3 hospital.py 
# Enter patient ID: HOSP4321
# Valid Patient ID 
# manoj@dell-vostro:~/Desktop/CBA-tr/Assignment/Python_Assignment/Strings$ 
