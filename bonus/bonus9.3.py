# Dictionaries

password = input(f"Enter a strong password with 8 or more characters, 1 Uppercase and 1 digit: ")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["case"] = uppercase

# if False in result:

print(result)
print(result.values())

if all(result.values()):  # == True is not necessary
    print("password is strong")
else:
    print("password is weak")