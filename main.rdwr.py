user_action = ""
with open('todos.txt', 'r') as file:
    todos_rec = file.readlines()

# remove '/n' and null at end of list
todos = [i.strip('\n') for i in todos_rec]

print(todos)

while True:
    user_action = input("Type 'a'dd, 's'how, 'd'isplay, 'e'dit, 'c'omplete or e'x'it: ")
    user_action = user_action.strip()

    match user_action:
        case 'a':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 's' | 'd':
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index+1}{') '}{item}"
                print(row)
        case 'e':
            number = int(input("Enter the number of the todo item: "))
            number = number - 1
            existing_item = todos[number]
            todo = input(f"Previous todo is '{existing_item}', Enter a new todo: ")
            todos[number] = todo
            print(todos)
        case 'c':
            number = int(input("Enter the number that you want to complete: "))
            index = number - 1
            existing_item = todos[index]
            todos.remove(todos[index])
            print(f"Completed to do '{existing_item}', was removed from the list.")
            # another way to complete
            # todos.pop(index)

        case 'x':
            break
        case _:
            print("You have entered an invalid choice.")

# add '/n' to item before write of file
print(todos)
todos_rec = [f"{i.title()}\n" for i in todos]

print(todos_rec)
with open('todos.txt', 'w') as file:
    file.writelines(todos_rec)

print("Bye")
