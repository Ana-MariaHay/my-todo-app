def strength(password):
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
    if all(result.values()):  # == True is not necessary
        message = "Strong Password"
    else:
        message = "Weak password"

    return message


pass_word = input(f"Enter a strong password with 8 or more characters, 1 Uppercase and 1 digit: ")
new_msg = strength(pass_word)

print(new_msg)