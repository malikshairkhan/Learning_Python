num1 = int(input("Please enter ist number:"))
num2 = int(input("Please enter the second number:"))
oper = input("Enter your choice 1 for addition 2 for subtraction and 3 for multiplication: ")
result = 0
match oper:
    case "1":
        result = num1+num2
    case "2":
        result = num1-num2
    case "3":
        result = num1*num2
    case _:
        print("invalid operation")
print(num1,num2,":",result)