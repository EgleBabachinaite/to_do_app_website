FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# this function is like a procedure, it doesn't return anything
# it modifies the text file, so we do not need a value
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
