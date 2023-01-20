myfunc = lambda valueOne,ValueTwo : valueOne+ValueTwo

ist_value = int(input("Please Enter ist value:"))
second_value = int(input("Please Enter the second value:"))
sum = myfunc(ist_value,second_value)
print("Sum of two value is: "+str(sum))

'''def Number(ist,second,third):
    if ist>second and ist>third:
        return ist
    elif second>ist and second>third:
        return second
    else:
        return third


ist = int(input("enter ist nmber:"))
second = int(input("enter 2nd nmber:"))
third = int(input("enter 3rd nmber:"))
print("Greatest number is : "+str(Number(ist,second,third)))'''