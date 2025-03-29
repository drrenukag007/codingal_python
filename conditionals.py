working_days = int(input("enter your total amount of working days "))
absentees = int(input("enter your total amount of absentees "))

percentage = working_days / absentees * 100
print(percentage)

if percentage < 75:
    print("you are not eligible to sit in the exam")

else:
    print("you are eligible to sit in the exam")
