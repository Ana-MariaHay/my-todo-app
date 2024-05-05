def parse(feet_inches):
    calc_list = feet_inches.split(" ")
    feet = float(calc_list[0])
    inches = float(calc_list[1])
    return [feet, inches]


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches_in = input("enter feet and inches:")
feet_inches_in = parse(feet_inches_in)
feet_in = feet_inches_in[0]
inches_in = feet_inches_in[1]
meters_in = convert(feet_in, inches_in)
print(f"{feet_in} feet and {inches_in} inches is equal to {meters_in} meters.")
if meters_in < 1:
    print("Kid is too small.")
else:
    print("kid can use the slide.")
