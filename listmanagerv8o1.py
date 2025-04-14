import os
import pickle
lst = []
action = "a"
screencanbecleared = True
def save():
    with open("list.pkl", "wb") as file:
        pickle.dump(lst, file)
def load():
    global lst
    try:
        with open("list.pkl", "rb") as file:
            lst = pickle.load(file)
    except (FileNotFoundError, EOFError):
        print("Can't load list. ")
        lst = []
def clear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            print("Clearing the terminal screen is not supported on your system or cannot be found by the code. ")
            globals()["clr"] = lambda *args, **kwargs: None
def EmptyError():
    clear()
    print("List is empty! ")
def add():
    while True:
        addingitem = input("Adding item: ")
        if addingitem in lst:
            clear()
            print("Item is already exists in list! ")
            break
        elif not addingitem:
            clear()
            print("Enter something! ")
            continue
        else:
            clear()
            lst.append(addingitem)
            print("Added successfully! ")
            break
    save()
def delete():
    deletingitem = input("Deleting item: ")
    clear()
    while True:
        if deletingitem in lst:
            clear()
            lst.remove(deletingitem)
            print("Deleted successfully! ")
            break
        elif not deletingitem:
            clear()
            print("Enter something! ")
            continue
        else:
            clear()
            print("Item is not in list! ")
            break
    save()
def show():
    clear()
    if lst:
        for a, i in enumerate(lst, start=1):
            print(f"{a}. {i}")
    else:
        EmptyError()
    save()
def clean():
    clear()
    if lst:
        lst.clear()
        print("Cleaned successfully! ")
    else:
        EmptyError()
    save()
def sort():
    clear()
    if lst:
        lst.sort()
        print("Sorted successfully! ")
    else:
        EmptyError()
    save()
def exiting():
    clear()
    print("Ending program... ")
    save()
def empty():
    clear()
    print("Please enter a command! ")
def invalid():
    clear()
    print("Please enter a valid command! ")
load()
while True:
    action = input(f"| Add | Delete | List | Clean | Sort | Exit | \n").strip().lower()
    if action == "add":
        add()
    elif action == "delete":
        delete()
    elif action == "list":
        show()
    elif action == "clean":
        clean()
    elif action == "sort":
        sort()
    elif action == "exit":
        exiting()
        break
    elif action == "":
        empty()
    else:
        invalid()

"""
List Manager Version 8.1
More Errors?
"""