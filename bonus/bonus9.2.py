# using List
#
password = input(f"Enter a strong password with 8 or more characters, 1 Uppercase and 1 digit: ")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

# if False in result:

if all(result):  # == True is not necessary
    print("password is strong")
else:
    print("password is weak")