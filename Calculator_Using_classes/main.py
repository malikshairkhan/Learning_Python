from Calculator import Claculator

choice = int(input("Please Enter your choise.\n1 for Addiiton:\n2 for Subtraction: \n3 for multiplication:\n4 for Division:"))

if choice == 1:
    cal = Claculator()
    val_One = int(input("Please enter ist value."))
    val_two = int(input("Please enter 2nd value."))
    result = cal.Add(val_One, val_two)
    print("Result is :"+str(result))
elif choice == 2:
    cal = Claculator()
    val_One = int(input("Please enter ist value."))
    val_two = int(input("Please enter 2nd value."))
    result = cal.Subtract(val_One, val_two)
    print("Result is :" + str(result))
elif choice == 3:
    cal = Claculator()
    val_One = int(input("Please enter ist value."))
    val_two = int(input("Please enter 2nd value."))
    result = cal.Multiply(val_One, val_two)
    print("Result is :" + str(result))
elif choice == 4:
    cal = Claculator()
    val_One = int(input("Please enter ist value."))
    val_two = int(input("Please enter 2nd value."))
    result = cal.Division(val_One, val_two)
    print("Result is :" + str(result))
else:
    print("your choice is Invalid. Please Chose between 1-4")