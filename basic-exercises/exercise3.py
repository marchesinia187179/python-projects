try:
    first = int(input("Insert the first integer: "))
    second = int(input("Insert the second integer: "))

    if ((first is second) == 5 or \
        (first + second) == 5 or \
        (first - second) == 5):
        print("True")
    else:
        print("False")

except:
    print("Error: the inputs must be integers!")