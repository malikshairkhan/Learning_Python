light = input("Please enter the color of traffic light: ")
if light.lower() == "green":
    print("car is allowed to go.")
elif light.lower() == "red":
    print("car has to stop.")
elif light.lower() == "yellow":
    print("car has to wait.")
else:
    print("unrecognized signal")
