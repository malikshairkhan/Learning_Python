marks = int(input("Enter your marks: "))
if marks >= 80:
    print("your grade is A!")
elif marks <= 80:
    print("your grade is B!")
elif marks <= 60:
    print("your grade is C!")
elif marks <= 50:
    print("your grade is D!")
elif marks <= 45:
    print("your grade is E!")
elif marks < 25:
    print("your grade is F!")
else:
    print("your are fail, please study!")