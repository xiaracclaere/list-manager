import os
lst = []
action = "a"
while action != "e":
    action = input(f"| Add | Delete | List | Clean | Exit | \n")
    if action == "a" or action == "add":
        addingitem = input("Adding item: ")
        if addingitem in lst:  
            os.system("cls")
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            os.system("cls")
            print("Added successfully! ")
    elif action == "d" or action == "delete":
        deletingitem = input("Deleting item: ")
        if deletingitem in lst:
            lst.remove(deletingitem)
            os.system("cls")
            print("Deleted successfully! ")
        else:
            os.system("cls")
            print("Item is not in list! ")
    elif action == "l" or action == "list":
        os.system("cls")
        a = 1
        if len(lst) > 0:
            for i in lst:
                print(a,".",i)
                a += 1
        else:
            print("List is empty! ")
    elif action == "c" or action == "clean":
        os.system("cls")
        if len(lst) > 0:
            lst.clear()
            print("Cleaned successfully! ")
        else:
            print("List is empty! ")
    elif action == "e" or action == "exit":
        os.system("cls")
        print("Ending program... ")
        break
    elif action == "":
        os.system("cls")
        print("Please enter a command! ")
    else:
        os.system("cls")
        print("Please enter a valid command! ")
        
"""
List Manager Version 3
Looks Better
"""