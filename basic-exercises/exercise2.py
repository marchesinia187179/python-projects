try:
    first = int(input("Insert the first input: "))
    second = int(input("Insert the second input: "))
    third = int(input("Insert the third input: "))

    if (not first is second and \
        not first is third and \
        not second is third):
        print(f"The the result of {first} + {second} + {third} is: {first + second + third}")
        exit

    if (first is second and \
        first is third and \
        second is third):
        print(f"The result of ({first} + {second})^{third} is: {(first + second) ** third}")
        exit
    
    if (first == 0 or second == 0 or third == 0):
        print("Error: if two numbers are equal, the other one can't be zero!")
        raise Exception

    if (first is second and not first is third):
        print(f"The result of ({first} + {second}) / {third} is: {(first + second) / third}")
        exit

    if (first is third and not first is second):
        print(f"The result of ({first} + {third}) / {second} is: {(first + third) / second}")
        exit

    if (second is third and not second is first):
        print(f"The result of ({second} + {third}) / {first} is: {(second + third) / first}")
        exit
except:
    print("Error: insert valid inputs")
