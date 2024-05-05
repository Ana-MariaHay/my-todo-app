FILEPATH = "../todos.txt"


def get_todos(filepath=FILEPATH):
    """ open the file name todos.txt and return
    the list of todo items
    """
    with open(filepath, 'r') as file:
        todos_rec = file.readlines()

    # remove '/n' and null at end of list
    todos_local = [i.strip('\n') for i in todos_rec]
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ write the file name todos.txt and update
    the list of todo items
    """
    # add '/n' to item before write of file
    todos_rec = [f"{i.title()}\n" for i in todos_local]

    with open(filepath, 'w') as file:
        file.writelines(todos_rec)
    return


if __name__ == "__main__":
    print(get_todos())