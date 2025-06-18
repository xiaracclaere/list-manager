import os
lst = []
action = "a"
def add():
        addingitem = input("Adding item: ")
        if addingitem in lst:  
            os.system("cls")
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            os.system("cls")
            print("Added successfully! ")
def delete():
    deletingitem = input("Deleting item: ")
    if deletingitem in lst:
        lst.remove(deletingitem)
        os.system("cls")
        print("Deleted successfully! ")
    else:
        os.system("cls")
        print("Item is not on list! ")
def list():
    os.system("cls")
    a = 1
    if len(lst) > 0:
        for i in lst:
            print(a,".",i)
            a += 1
    else:
        print("List is empty! ")
def clean():
    os.system("cls")
    if len(lst) > 0:
        lst.clear()
        print("Cleaned successfully! ")
    else:
        print("List is empty! ")
def exit():
    os.system("cls")
    print("Ending program... ")
def empty():
    os.system("cls")
    print("Please enter a command! ")
def invalid():
    os.system("cls")
    print("Please enter a valid command! ")
while action != "e":
    action = input(f"| Add | Delete | List | Clean | Exit | \n")
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
    elif action == "":
        empty()
    else:
        invalid()

"""
List Manager Version 4
Functional
"""