while True:
    try:
        length = float(input("Enter length: "))
    except ValueError:
        print("not a float")
        continue

    try:
        width = float(input("Enter width: "))
    except ValueError:
        print("not a float")
        continue

    perimeter = (length + width) * 2
    area = length * width

    print("Perimeter is", perimeter)
    print("Area is", area)

    if perimeter < 14 and area < 8:
        print("OK")
    else:
        print("NOT OK")

    cont = input("Continue Y/N: ")
    if cont.upper() != "Y":
        break
