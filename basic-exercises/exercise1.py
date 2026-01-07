import math


try:
    print("Insert the radius: ", end="")
    r = int(input())
    if (r < 0) :
        print("Error: the input isn't greather than zero")
    else:
        area = math.pi * (r ** 2)
        print(f"The area is: {area:.2f}")
except:
    print("Error: the input isn't an integer!")

