def convert(feet_inches):
    calc_list = feet_inches.split(" ")
    feet = float(calc_list[0])
    inches = float(calc_list[1])

    meters = feet * 0.3048 + inches * 0.0254
    #  return f"{feet} feet and {inches} inches is equal to {meters} meters."
    return meters


feet_inches_in = input("enter feet and inches:")
meters_in = convert(feet_inches_in)
if meters_in < 1:
    print("Kid is too small")
else:
    print("kid can ride")