import os
lst = []
action = "a"
while action != "e":
    action = input(f"Add(a)  Delete(d)  List(l)  Clean(c)  Exit(e) \n")
    if action == "a":
        addingitem = input("Adding item: ")
        if addingitem in lst:  
            os.system("cls")
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            os.system("cls")
            print("Added successfully! ")
    elif action == "d":
        deletingitem = input("Deleting item: ")
        if deletingitem in lst:
            lst.remove(deletingitem)
            os.system("cls")
            print("Deleted successfully! ")
        else:
            os.system("cls")
            print("Item is not in list. ")
    elif action == "l":
        os.system("cls")
        a = 1
        if len(lst) > 0:
            for i in lst:
                print(a,".",i)
                a += 1
        else:
            print("List is empty! ")
    elif action == "c":
        os.system("cls")
        if len(lst) > 0:
            lst.clear()
            print("Cleaned successfully! ")
        else:
            print("List is empty! ")
    elif action == "e":
        os.system("cls")
        print("Ending program... ")
        break
    elif action == "" or action == " ":
        os.system("cls")
        print("Please enter a command! ")
    else:
        os.system("cls")
        print("Please enter a valid command! ")

"""
List Manager Version 2
Better
"""