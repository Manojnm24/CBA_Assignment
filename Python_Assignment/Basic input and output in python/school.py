#A school needs a grading system. Ask for marks of 5 subjects and calculate percentage + grade.

sub1 = int(input("enter the sub1 marks "))
sub2 = int(input("enter the sub2 marks "))
sub3 = int(input("enter the sub3 marks "))
sub4 = int(input("enter the sub4 marks "))
sub5 = int(input("enter the sub5 marks "))
total = ((sub1+sub2+sub3+sub4+sub5)/500)*100
if 80<total and total<=100:
    x="A"
elif 50<total and total<=80:
    x="B"
elif 35<total and total<=50:
    x="C"
else:
    x="Fail"
print(f"Total : {total}% and grade is {x}")
