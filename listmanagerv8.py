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
        lst = []
def clear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            globals()["clr"] = lambda *args, **kwargs: None
def EmptyError():
    clear()
    print("List is empty! ")
def add():
        addingitem = input("Adding item: ")
        clear()
        if addingitem in lst:
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            print("Added successfully! ")
def delete():
    deletingitem = input("Deleting item: ")
    clear()
    if deletingitem in lst:
        lst.remove(deletingitem)
        print("Deleted successfully! ")
    else:
        print("Item is not in list! ")
def show():
    a = 1
    clear()
    if len(lst) > 0:
        for i in lst:
            print(a,".",i)
            a += 1
    else:
        EmptyError()
def clean():
    clear()
    if len(lst) > 0:
        lst.clear()
        print("Cleaned successfully! ")
    else:
        EmptyError()
def sort():
    clear()
    if len(lst) > 0:
        lst.sort()
        print("Sorted successfully! ")
    else:
        EmptyError()
def exiting():
    clear()
    save()
    print("Ending program... ")
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
List Manager Version 8
Same 2
"""