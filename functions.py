FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ open a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_rec = file.readlines()

    todos_local = [i.strip('\n') for i in todos_rec]
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ write the to-do items list in the text file."""
    todos_rec = [f"{i.title()}\n" for i in todos_local]
    with open(filepath, 'w') as file:
        file.writelines(todos_rec)
    return


if __name__ == "__main__":
    print(get_todos())