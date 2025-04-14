import os
lst = []
action = "a"
screencanbecleared = True
def clr():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            globals()["clr"] = lambda *args, **kwargs: None
def add():
        addingitem = input("Adding item: ")
        clr()
        if addingitem in lst:
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            print("Added successfully! ")
def dlt():
    deletingitem = input("Deleting item: ")
    clr()
    if deletingitem in lst:
        lst.remove(deletingitem)
        print("Deleted successfully! ")
    else:
        print("Item is not in list! ")
def shw():
    a = 1
    clr()
    if len(lst) > 0:
        for i in lst:
            print(a,".",i)
            a += 1
    else:
        print("List is empty! ")
def cln():
    clr()
    if len(lst) > 0:
        lst.clear()
        print("Cleaned successfully! ")
    else:
        print("List is empty! ")
def ext():
    clr()
    print("Ending program... ")
def emp():
    clr()
    print("Please enter a command! ")
def inv():
    clr()
    print("Please enter a valid command! ")
while action != "e":
    action = input(f"| Add | Delete | List | Clean | Exit | \n").strip().lower()
    if action == "a" or action == "add":
        add()
    elif action == "d" or action == "delete":
        dlt()
    elif action == "l" or action == "list":
        shw()
    elif action == "c" or action == "clean":
        cln()
    elif action == "e" or action == "exit":
        ext()
        break
    elif action == "":
        emp()
    else:
        inv()

"""
List Manager Version 5.2
-1
"""