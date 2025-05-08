# IMPORTS

import os, pickle

# VARIABLES AND LISTS

lst = []

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

def save():
    with open(f"list.pkl", "wb") as file:
        pickle.dump(lst, file)
        
def load():
    global lst
    try:
        with open("list.pkl", "rb") as file:
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

def autosave(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        save()
        return result
    return wrapper

def clear():
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            print("Clearing the terminal screen is not supported on your system or cannot be found by the code. ")
            globals()["clear"] = lambda *args, **kwargs: None

def helping():
    clear()
    print("""
List Manager Help Menu:
Add: Adds the text that is written to the desired section after it is written to the list.
Delete: Deletes the text that is written to the desired section after it is written, if it is in the list.
List: Lists all the item in the list.
Clean: Deletes all the item in the list.
Sort: Sorts all the item in the list.
Help: Shows this menu.
Reset: Resets the program and saves the list.
Code: Shows code of the program. 
Exit: Ends the program and saves the list.
          """)

def reset():
    clear()
    main()

def show_code():
    clear()
    with open(__file__, "r", encoding="utf-8") as file:
        print(file.read())

def exiting():
    clear()
    print("Ending program... ")
    save()

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
            print("Added successfully! ")
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
                print("Deleted successfully! ")
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
            print("Cleaned successfully! ")
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
            print("Sorted successfully!")
        else:
            pass
    else:
        clear()
        EmptyListError()

def empty():
    clear()
    print("Please enter a command! ")

def invalid():
    clear()
    print("Please enter a valid command! ")

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
    print("Can't load list. ")

# PROGRAM

def main():
    clear()
    
    load()

    print('Welcome to the List Manager! You can write "help" to get help. ')

    while True:
        action = input(f"| Add | Delete | List | Clean | Sort | Help | Reset | Code | Exit | \n").strip().lower()
        
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
            empty()
        else:
            invalid()

# RUNNING PROGRAM

if __name__ == "__main__":
    main()

"""
List Manager Version 10 Snapshot 2(Complete)
Copyright 2025 © Xiara Cclaere
"""