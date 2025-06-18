# IMPORTS

import os, pickle

# VARIABLES AND LISTS

lst = []
action = "a"
screencanbecleared = True
code = 0
current_version = None

# CLEAR

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        globals()["clear"] = lambda *args, **kwargs: None

# VERSION FUNCTIONS

def v1():
    global lst, action, code, current_version, ui, switch
    current_version = v1
    while action != "e":
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                print("Please enter a valid command! ")
        elif code == 1:
            ui()

def v2():
    global lst, action, code, current_version, ui, switch
    current_version = v2
    while action != "e":
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                os.system("cls")
                print("Please enter a valid command! ")
        elif code == 1:
            ui()

def v3():
    global lst, action, code, current_version, ui, switch
    current_version = v3
    while action != "e":
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                os.system("cls")
                print("Please enter a valid command! ")
        elif code == 1:
            ui()

def v4():
    global lst, action, code, current_version, ui, switch
    current_version = v4
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v5():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v5
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v5o1():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v5o1
    def clr():
            if os.name == "nt":
                os.system("cls")
            elif os.name == "posix":
                os.system("clear")
            else:
                globals()["fonk"] = lambda *args, **kwargs: None # Code has an error, nevermind. 
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
        if code == 0:
            action = input(f"| Add | Delete | List | Clean | Exit | \n")
            action = action.lower()
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
            elif action == "switch":
                switch()
            else:
                inv()
        elif code == 1:
            ui()

def v5o2():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v5o2
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                inv()
        elif code == 1:
            ui()

def v6():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v6
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
            print("List is empty! ")
    def clean():
        clear()
        if len(lst) > 0:
            lst.clear()
            print("Cleaned successfully! ")
        else:
            print("List is empty! ")
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
        if code == 0:
            action = input(f"| Add | Delete | List | Clean | Exit | \n").strip().lower()
            if action == "a" or action == "add":
                add()
            elif action == "d" or action == "delete":
                delete()
            elif action == "l" or action == "list":
                show()
            elif action == "c" or action == "clean":
                clean()
            elif action == "e" or action == "exit":
                exiting()
                break
            elif action == "":
                empty()
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v7():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v7
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v8():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v8
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v8o1():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v8o1
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

def v8o2():
    global lst, action, screencanbecleared, code, current_version, ui, switch
    current_version = v8o2
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
        
    def EmptyListError():
        clear()
        print("List is empty! ")
    def AlreadyExistsError():
        print("Item is already exists in list! ")
    def EmptyInputError():
        print("Please enter something! ")
    def ItemIsNotOnListError():
        print("Item is not in list! ")
    def add():
        while True:
            addingitem = input("Adding item: ")
            clear()
            if addingitem in lst:
                AlreadyExistsError()
                break
            elif not addingitem:
                EmptyInputError()
                continue
            else:
                lst.append(addingitem)
                print("Added successfully! ")
                break
        save()
    def delete():
        deletingitem = input("Deleting item: ")
        clear()
        while True:
            if deletingitem in lst:
                lst.remove(deletingitem)
                print("Deleted successfully! ")
                break
            elif not deletingitem:
                EmptyInputError()
                continue
            else:
                ItemIsNotOnListError()
                break
        save()
    def show():
        clear()
        if lst:
            for a, i in enumerate(lst, start=1):
                print(f"{a}. {i}")
        else:
            EmptyListError()
    def clean():
        clear()
        if lst:
            lst.clear()
            print("Cleaned successfully! ")
        else:
            EmptyListError()
        save()
    def sort():
        clear()
        if lst:
            lst.sort()
            print("Sorted successfully! ")
        else:
            EmptyListError()
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
        if code == 0:
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
            elif action == "switch":
                switch()
            else:
                invalid()
        elif code == 1:
            ui()

# SWITCH MODE

def save():
    with open("list.pkl", "wb") as file:
        pickle.dump(lst, file)
            
def load():
    global lst
    print("Founding a list file... ")
    try:
        with open("list.pkl", "rb") as file:
            lst = pickle.load(file)
            print("Successfully loaded! ")
    except FileNotFoundError:
        answer = input("Can't found a list file. Do you wanna enter it's name manually? (y/n)").strip().lower()
        if answer == "y":
            filename = input("Enter the file name: ")
            try:
                with open(filename, "rb") as file:
                    lst = pickle.load(file)
            except FileNotFoundError:
                print("Can't found your list file, sorry. ")
                lst = []
        else:
            pass

def reset():
    clear()
    main()
        
def switch():
    clear()
    global code
    if code == 1:
        code = 0
    elif code == 0:
        code = 1
        
def ui():
    global current_version
    print("Old Manager Switch Menu \n")
    command = input("| Save | Load | Reset | Change | Back | Exit | \n").strip().lower()
    if command == "save":
        clear()
        save()
    elif command == "load":
        clear()
        load()
    elif command == "reset":
        clear()
        reset()
    elif command == "change":
        clear()
        change()
    elif command == "back":
        clear()
        current_version()
    elif command == "exit":
        clear()
        print("Exiting... ")
        exit(0)
    else:
        clear()
        print("Please enter a valid command! ")
        
# VERSION CHANGER

def change():
    print("Please choose a version: \n")
    while True:
        version = input("| v1 | v2 | v3 | v4 | v5 | v5.1 |v5.2 | v6 | v7 | v8 | v8.1 | v8.2 | Exit |\n").lower().strip()
        if version == "v1":
            clear()
            v1()
        elif version == "v2":
            clear()
            v2()
        elif version == "v3":
            clear()
            v3()
        elif version == "v4":
            clear()
            v4()
        elif version == "v5":
            clear()
            v5()
        elif version == "v5.1":
            clear()
            v5o1()
        elif version == "v5.2":
            clear()
            v5o2()
        elif version == "v6":
            clear()
            v6()
        elif version == "v7":
            clear()
            v7()
        elif version == "v8":
            clear()
            v8()
        elif version == "v8.1":
            clear()
            v8o1()
        elif version == "v8.2":
            clear()
            v8o2()
        elif version == "exit":
            clear()
            print("Exiting... ")
            exit(0)
        else:
            clear()
            print("Please enter a valid version or command! ")
# MAIN

def main():
    clear()
    print("Welcome to the Old Manager! You can find all old versions of the List Maanger here. \n")
    change()
    
# RUNNING

if __name__ == "__main__":
    main()

print(f"""
Old Manager
COPYRIGHT 2025 © Xiara Cclaere
Some Nostalgia
""")