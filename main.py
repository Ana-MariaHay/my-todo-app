# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    choice = input(f"\nType 'a'dd followed by the todo,\n"
                   f"Type 'e'dit followed by the number to edit,\n"
                   f"Type 'c'omplete followed by the number to complete,\n"
                   f"Type 's'how or 'd'isplay,\n"
                   f"Type 'e'x'it to abandon the todos program\n"
                   f": ")

    user_action = choice[0]
    todo = choice[2:]

    if user_action[0] == 'a' and todo != "":
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    if user_action == 's' or user_action == 'd':
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.title()
            row = f"{index+1}{') '}{item}"
            print(row)

    elif user_action[0] == 'e':
        try:
            number = int(todo) - 1
            todos = functions.get_todos()
            existing_item = todos[number]
            todo = input(f"Previous todo is '{existing_item}', Enter a new todo: ")
            todos[number] = todo
            functions.write_todos(todos)

        except (IndexError, ValueError):
            print("You have entered an invalid choice.")
            continue

    elif user_action[0] == 'c':
        try:
            index = int(todo) - 1
            todos = functions.get_todos()
            existing_item = todos[index]
            todos.remove(todos[index])
            print(f"The completed to do '{existing_item}', was removed from the list.")
            # another way to complete
            # todos.pop(index)
            functions.write_todos(todos)

        except (IndexError, ValueError):
            print("You have entered an invalid choice.")
            continue

    elif user_action[0] == 'x':
        break
    else:
        print("You have entered an invalid choice.")

print("Bye")