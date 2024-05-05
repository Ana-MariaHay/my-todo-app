password = input(f"Enter a strong password with 8 or more characters, 1 Uppercase and 1 digit: ")
pass_msg = "You have entered a weak password"

flag = 0

if len(password) >= 8:
    for i, letter in enumerate(password):
        if letter == letter.capitalize():
            flag += 1
        if letter in "1234567890":
            flag += 1


if flag >= 2:
    pass_msg = "You have entered a strong password"

print(pass_msg)


