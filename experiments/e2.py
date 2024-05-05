prompt = "Enter a todo or null to exit:"

todos = []

test = True
while test is True:
    todo = input(prompt)
    todos.append(todo.capitalize())
    print(todos)
    if not(todo):
        test = False