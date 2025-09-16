"""cell06"""
def greeting_for_all(name):
    """"ex03"""
    if name.isnumeric():
        print("Error! It was not a name.")
    elif name == "":
        print("Hello, noble stranger.")
    else:
        print(f"Hello, {name}.")
greeting_for_all(input())
