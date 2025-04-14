lst = []
action = "a"
while action != "e":
    action = input("Add(a)  Delete(d)  List(l)  Exit(e) ")
    if action == "a":
        addingitem = input("Adding item: ")
        if addingitem in lst:  
            print("Item is already exists in list! ")
        else:
            lst.append(addingitem)
            print("Added successfully! ")
    elif action == "d":
        deletingitem = input("Deleting item: ")
        if deletingitem in lst:
            lst.remove(deletingitem)
            print("Deleted successfully! ")
        else:
            print("Item is not in list. ")
    elif action == "l":
        a = 1
        for i in lst:
            print(a,".",i)
            a += 1
    elif action == "e":
        print("Ending program... ")
        break
    else:
        print("Please enter a valid command! ")

"""
List Manager Version 1
Classic
"""