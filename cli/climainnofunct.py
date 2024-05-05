user_action = ""
with open('../todos.txt', 'r') as file:
    todos_rec = file.readlines()

# remove '/n' and null at end of list
todos = [i.strip('\n') for i in todos_rec]

# print(todos)

while True:
    choice = input(f"\nType 'a'dd followed by the todo,\n"
                   f"Type 'e'dit followed by the number to edit,\n"
                   f"Type 's'how or 'd'isplay,\n"
                   f"Type 'c'omplete followed by the number to complete,\n"
                   f"Type 'e'x'it to abandon the todos program\n"
                   f": ")

    user_action = choice[0]
    todo = choice[2:]

    if user_action[0] == 'a':
        todos.append(todo)

    if user_action == 's' or user_action == 'd':
        for index, item in enumerate(todos):
            item = item.title()
            row = f"{index+1}{') '}{item}"
            print(row)

    elif user_action[0] == 'e':
        try:
            number = int(todo) - 1
            existing_item = todos[number]
            todo = input(f"Previous todo is '{existing_item}', Enter a new todo: ")
            todos[number] = todo
            print(todos)

        except (IndexError, ValueError):
            print("There is no item with that number")
            continue

    elif user_action[0] == 'c':
        try:
            index = int(todo) - 1
            existing_item = todos[index]
            todos.remove(todos[index])
            print(f"The completed to do '{existing_item}', was removed from the list.")

            # another way to complete
            # todos.pop(index)
        except (IndexError, ValueError):
            print("There is no item with that number")
            continue

    elif user_action[0] == 'x':
        break
    else:
        print("You have entered an invalid choice.")

# add '/n' to item before write of file
print(todos)
todos_rec = [f"{i.title()}\n" for i in todos]

print(todos_rec)
with open('../todos.txt', 'w') as file:
    file.writelines(todos_rec)

print("Bye")
