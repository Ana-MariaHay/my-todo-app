from bonus.parsers14 import parse
from bonus.converters14 import convert

feet_inches_in = input("enter feet and inches:")
parsed = parse(feet_inches_in)

meters_in = convert(parsed['feet'], parsed['inches'])  # access the dictionary items via the key

# print the dictionary items via the key
print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {meters_in} meters.")
if meters_in < 1:
    print("Kid is too small.")
else:
    print("kid can use the slide.")
