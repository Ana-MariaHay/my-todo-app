def greet(message):  # parameter
    new_msg = message.title()
    return new_msg


my_greeting = input("Enter the greeting you would like to see: ")
greeting = greet(message=my_greeting)  # argument = value of the argument
print(greeting)

