num1 = int(input("Please enter ist number:"))
num2 = int(input("Please enter the second number:"))
oper = input("Enter your choice 1 for addition 2 for subtraction and 3 for multiplication: ")
result = 0
if oper == "1":
    result = num1 + num2
elif oper == "2":
    result = num1 - num2
elif oper == "3":
    result = num1 * num2
else:
    print("invalid number")
print(num1, num2, ":", result)