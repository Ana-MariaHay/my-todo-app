import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4)")

now = time.strftime("%b %d, %Y %H:%M:%S")
clock = sg.Text(key="clock")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button(image_size=(80, 80), tooltip="Enter a todo",
                       image_source="add.png", mouseover_colors="LightBlue2", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_size=(80, 80), tooltip="Complete a todo",
                            image_source="complete.png", mouseover_colors="LightBlue2", key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My to-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break

    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Exit":
            break
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except (IndexError, ValueError):
                sg.popup("Please select a todo item prior first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except (IndexError, ValueError):
                sg.popup("Please select a todo item prior first", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])

window.close()
