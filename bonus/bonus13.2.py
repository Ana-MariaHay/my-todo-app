def parse(feet_inches):
    calc_list = feet_inches.split(" ")
    feet = float(calc_list[0])
    inches = float(calc_list[1])
    return {"feet": feet, "inches": inches}  # dictionary, can be accessed via the key


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet_inches_in = input("enter feet and inches:")
parsed = parse(feet_inches_in)

meters_in = convert(parsed['feet'], parsed['inches'])  # access the dictionary items via the key

# print the dictionary items via the key
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {meters_in} meters.")
if meters_in < 1:
    print("Kid is too small.")
else:
    print("kid can use the slide.")
