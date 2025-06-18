import os
lst = []
action = "a"
screencanbecleared = True
def clear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            globals()["fonk"] = lambda *args, **kwargs: None # Code has an error, nevermind. 
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
def list():
    a = 1
    clear()
    if len(lst) > 0:
        for i in lst:
            print(a,".",i)
            a += 1
    else:
        print("List is empty! ")
def clean():
    clear()
    if len(lst) > 0:
        lst.clear()
        print("Cleaned successfully! ")
    else:
        print("List is empty! ")
def exit():
    clear()
    print("Ending program... ")
def empty():
    clear()
    print("Please enter a command! ")
def invalid():
    clear()
    print("Please enter a valid command! ")
while action != "e":
    action = input(f"| Add | Delete | List | Clean | Exit | \n")
    action = action.lower()
    if action == "a" or action == "add":
        add()
    elif action == "d" or action == "delete":
        delete()
    elif action == "l" or action == "list":
        list()
    elif action == "c" or action == "clean":
        clean()
    elif action == "e" or action == "exit":
        exit()
        break
    elif action == "":
        empty()
    else:
        invalid()

"""
List Manager Version 5
Clear
"""