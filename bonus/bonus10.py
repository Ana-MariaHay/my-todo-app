while True:
    try:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        if width == length:
            exit("That looks like a square")  # prints red

    except ValueError:
        print("not a float")
        continue

    perimeter = (length + width) * 2
    area = length * width

    print("Perimeter is", perimeter)
    print("Area is", area)

    cont = input("Continue Y/N: ")
    if cont.upper() != "Y":
        break
