# IMPORTS

import os, pickle

# VARIABLES AND LISTS

lst = []
counter = 1

# FUNCTIONS

def WantCheck():
    control = input("Do you really want to do this?(Y/n): ")
    if control == "Y" or control == "y" or control == "":
        do = True
    else:
        do = False
    return do

def ErrorLog(message):
    with open("error_logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")

def save(list_name="list"):
    try:
        with open(f"{list_name}.pkl", "wb") as file:
            pickle.dump(lst, file)
    except:
        SavingListError()
        
def load(list_name="list"):
    global lst
    try:
        with open(f"{list_name}.pkl", "rb") as file:
            lst = pickle.load(file)
    except FileNotFoundError as e:
        ErrorLog(f"FileNotFoundError: {str(e)}")
        LoadingListError()
        lst = []
    except EOFError as e:
        ErrorLog(f"EOFError: {str(e)}")
        LoadingListError()
        lst = []
    except Exception as e:
        ErrorLog(f"Unknown error: {str(e)}")
        LoadingListError()
        lst = []

def save_counter():
    with open("counter.pkl", "wb") as file:
        pickle.dump(counter, file)

def load_counter():
    global counter
    try:
        with open("counter.pkl", "rb") as file:
            counter = pickle.load(file)
    except FileNotFoundError as e:
        ErrorLog(f"FileNotFoundError: {str(e)}")
        counter = 1
    except EOFError as e:
        ErrorLog(f"EOFError: {str(e)}")
        counter = 1
    except Exception as e:
        ErrorLog(f"Unknown error: {str(e)}")
        LoadingCounterError()
        counter = 1

def autosave(func):
    try:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            save(f"list{counter}")
            return result
        return wrapper
    except:
        AutosavingError()

def autosave_counter(func):
    try:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            save_counter()
            return result
        return wrapper
    except:
        AutosavingCounterError()

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        print("Clearing the terminal screen is not supported on your system or cannot be found by the program. ")
        globals()["clear"] = lambda *args, **kwargs: None

def exporting():
    for i in lst:
        e = i
        return e

def helping():
    clear()
    print(f"List Manager Help Menu: \n", """
Add: Adds the text that is written to the desired section after it is written to the list.
Delete: Deletes the text that is written to the desired section after it is written, if it is in the list.
List: Lists all the item in the list.
Clean: Deletes all the item in the list.
Sort: Sorts all the item in the list.
New: Creates a new list.
Version: Gives information about current version of program. 
Lists: Lists created lists. 
Export: Exports list to a .txt file. 
Help: Shows this menu.
Exit: Ends the program and saves the list.
A small note: You cannot load lists that were saved in older versions older than 10.0. Because in the old saving system, it was saved as follows: list.pkl. In the new saving system, it is saved as follows: list1.pkl, list2.pkl, list3.pkl... etc.
          """)

def reset():
    clear()
    main()

def show_code():
    clear()
    with open(__file__, "r", encoding="utf-8") as file:
        print(file.read())

def about_version(): 
    with open(__file__, "r", encoding="utf-8") as file:
        lns = len(file.readlines())
    clear()
    print(f"""
Version = 10.1
News:
- Added new error messages.
- Made some error messages and notifications more understandable. 
Happy News:
The code increased from 280 to {lns} lines!

İyi Kullanımlar!
          """)

def exiting():
    if exit:
        clear()
        print("Ending program... ")
        save(f"lst{counter}")
        save_counter()
    else:
        ExitingError()

# ACTIONS

@autosave
def add():
    while True:
        item = input("Adding item: ")
        clear()
        if item in lst:
            AlreadyExistsError()
            break
        elif not item:
            EmptyInputError()
            continue
        else:
            lst.append(item)
            print("Added item to list successfully! ")
            break
    item = ""

@autosave
def delete():
    if lst:
        while True:
            item = input("Deleting item: ")
            clear()
            if item in lst:
                lst.remove(item)
                print("Deleted item from list successfully! ")
                break
            elif not item:
                EmptyInputError()
                continue
            else:
                ItemIsNotOnListError()
                break
        item = ""
    else:
        clear()
        EmptyListError()

def show():
    clear()
    if lst:
        for a, i in enumerate(lst, start=1):
            print(f"{a}. {i}")
    else:
        EmptyListError()

@autosave
def clean():
    if lst:
        do = WantCheck()
        clear()
        if do:
            lst.clear()
            print("List is cleaned successfully! ")
        else:
            pass
    else:
        clear()
        EmptyListError()

def sort(item):
    return item

@autosave
def sort_list():
    if lst:
        do = WantCheck()
        clear()
        if do:
            lst.sort(key=sort)
            print("List is sorted successfully!")
        else:
            pass
    else:
        clear()
        EmptyListError()

@autosave_counter
def new_list():
    global lst, counter
    save(f"lst{counter}")
    counter += 1
    lst = []
    clear()
    print(f"Created new list: lst{counter}")
    save(f"lst{counter}")

def show_lists():
    clear()
    if counter > 1:
        for i in range(1, counter):
            print(f"lst{i}")
    else:
        NoListsError()

def export(message):
    try:
        with open(f"lst{counter}.txt", "a") as list_file:
            list_file.write(f"{message}\n")
        clear()
        print(f"List is exported with name: lst{counter}.txt ! ")
    except:
        ExportingError()

# ERRORS AND WARNINGS

def EmptyListError():
    print("List is empty! ")

def AlreadyExistsError():
    print("Item is already exists in list! ")

def EmptyInputError():
    print("Please enter something! ")

def ItemIsNotOnListError():
    print("Item is not in list! ")

def LoadingListError():
    print("An error occured while loading list! ")

def InvalidInputError():
    clear()
    print("Please enter a valid command! ")

def NoListsError():
    print("No created lists! ")

def LoadingCounterError():
    print("An error occured while loading counter! ")

def ClearError():
    print("Clearing the terminal screen is not supported on your system or cannot be found by the program. ")

def ExitingError():
    print("An error occured while exiting program! ")

def SavingListError():
    print("An error occured while saving list! ")
    
def SavingCounterError():
    print("An error occured while saving counter! ")

def AutosavingError():
    print("An error occured while autosaving list! ")
    
def AutosavingCounterError():
    print("An error occured while autosaving counter! ")

def ExportingError():
    print("An error occured while exporting list! ")

# PROGRAM

def main():
    clear()
    
    load_counter()
    
    load(f"lst{counter}")

    print('Welcome to the List Manager! You can write "help" to get help. Version = 10.1 ')
    
    while True:
        action = input(f"| Add | Delete | List | Clean | Sort | New | Lists | Export | Help | Exit | \n").strip().lower()
        
        if action == "add":
            add()
        elif action == "delete":
            delete()
        elif action == "list":
            show()
        elif action == "clean":
            clean()
        elif action == "sort":
            sort_list()
        elif action == "new":
            new_list()
        elif action == "version":
            about_version()
        elif action == "lists":
            show_lists()
        elif action == "export":
            export(exporting())
        elif action == "help":
            helping()
        elif action == "reset":
            reset()
        elif action == "code":
            show_code()
        elif action == "exit":
            exiting()
            break
        elif action == "":
            EmptyInputError()
        else:
            InvalidInputError()

# RUNNING PROGRAM

if __name__ == "__main__":
    main()

"""
List Manager Version 10.1
Copyright 2025 © Xiara Cclaere
JUST MORE ERRORS
"""