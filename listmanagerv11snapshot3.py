# IMPORTS

import os, pickle

# VARIABLES AND LISTS

lst = []
counter = 1

# FUNCTIONS

class functions:
    def check():
        control = input("Do you really want to do this?(Y/n): ")
        if control == "Y" or control == "y" or control == "":
            do = True
        else:
            do = False
        return do

    def ProgramErrorLog(message):
        with open("program_error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def ErrorLog(message):
        with open("error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def save(list_name="list"):
        try:
            with open(f"{list_name}.pkl", "wb") as file:
                pickle.dump(lst, file)
        except:
            errors.SavingListError()
            
    def load(list_name="list"):
        global lst
        try:
            with open(f"{list_name}.pkl", "rb") as file:
                lst = pickle.load(file)
        except FileNotFoundError as e:
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            errors.LoadingListError()
            lst = []
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            errors.LoadingListError()
            lst = []
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
            errors.LoadingListError()
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
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            counter = 1
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            counter = 1
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
            errors.LoadingCounterError()
            counter = 1

    def autosave(func):
        try:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                functions.save(f"list{counter}")
                return result
            return wrapper
        except:
            errors.AutosavingError()

    def autosave_counter(func):
        try:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                functions.save_counter()
                return result
            return wrapper
        except:
            errors.AutosavingCounterError()

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
        functions.clear()
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
            """)

    def reset():
        functions.clear()
        main()

    def show_code():
        functions.clear()
        with open(__file__, "r", encoding="utf-8") as file:
            print(file.read())

    def about_version(): 
        with open(__file__, "r", encoding="utf-8") as file:
            lns = len(file.readlines())
        functions.clear()
        print(f"""
Version = 11s3
News:
-
Happy News:
The code increased from 391 to {lns} lines!

Enjoy!
            """)

    def exiting():
        if exit:
            functions.clear()
            print("Exiting program... ")
            functions.save(f"list{counter}")
            functions.save_counter()
        else:
            ExitingError()

# ACTIONS

@functions.autosave
def add():
    while True:
        item = input("Adding item: ")
        functions.clear()
        if item in lst:
            errors.AlreadyExistsError()
            break
        elif not item:
            errors.EmptyInputError()
            continue
        else:
            lst.append(item)
            print("Added item to list successfully! ")
            break
    item = ""

@functions.autosave
def delete():
    if lst:
        while True:
            item = input("Deleting item: ")
            functions.clear()
            if item in lst:
                lst.remove(item)
                print("Deleted item from list successfully! ")
                break
            elif not item:
                errors.EmptyInputError()
                continue
            else:
                errors.ItemIsNotOnListError()
                break
        item = ""
    else:
        functions.clear()
        errors.EmptyListError()

def show():
    functions.clear()
    if lst:
        for a, i in enumerate(lst, start=1):
            print(f"{a}. {i}")
    else:
        errors.EmptyListError()

@functions.autosave
def clean():
    if lst:
        do = functions.check()
        functions.clear()
        if do:
            lst.clear()
            print("List is cleaned successfully! ")
        else:
            pass
    else:
        functions.clear()
        errors.EmptyListError()

def sort(item):
    return item

@functions.autosave
def sort_list():
    if lst:
        do = functions.check()
        functions.clear()
        if do:
            lst.sort(key=sort)
            print("List is sorted successfully!")
        else:
            pass
    else:
        functions.clear()
        errors.EmptyListError()

@functions.autosave_counter
def new_list():
    global lst, counter
    functions.save(f"list{counter}")
    counter += 1
    lst = []
    functions.clear()
    print(f"Created new list: lst{counter}")
    functions.save(f"list{counter}")

def show_lists():
    functions.clear()
    if counter > 1:
        for i in range(1, counter):
            print(f"lst{i}")
    else:
        errors.NoListsError()

def export(message):
    try:
        with open(f"list{counter}.txt", "a") as list_file:
            list_file.write(f"{message}\n")
        functions.clear()
        print(f"List is exported with name: list{counter}.txt ! ")
    except:
        errors.ExportingError()

# ERRORS AND WARNINGS

class errors:
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
        print("An error occured while saving couter! ")

    def AutosavingError():
        print("An error occured while autosaving list! ")
        
    def AutosavingCounterError():
        print("An error occured while autosaving counter! ")

    def ExportingError():
        print("An error occured while exporting list! ")

    def ResettingError():
        print("An error occured while resetting program! ")

    def ShowingCodeError():
        print("An error occured while showing code! ")
        
    def TooManyErrors():
        print("Too many errors! ")
    
    def CodeError():
        print("An error occured in program! ")

    def UnknownError():
        print("An unknown error has occured! ")

# ERROR CONTROL

def error_control(func):
    try:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                functions.ProgramErrorLog(f"Error: {str(e)}")
                errors.UnknownError()
        return wrapper
    except:
        errors.TooManyErrors()

# PROGRAM

@error_control
def main():
    functions.clear()
    functions.load_counter()
    functions.load(f"list{counter}")

    print('Welcome to the List Manager! You can write "help" to get help. Version = 11s3 ')
    
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
            functions.about_version()
        elif action == "lists":
            show_lists()
        elif action == "export":
            export(functions.exporting())
        elif action == "help":
            functions.helping()
        elif action == "reset":
            functions.reset()
        elif action == "code":
            functions.show_code()
        elif action == "mode":
            functions.switch_mode()
        elif action == "exit":
            functions.exiting()
            break
        elif action == "":
            functions.clear()
            errors.EmptyInputError()
        else:
            functions.clear()
            errors.InvalidInputError()

# RUNNING PROGRAM

if __name__ == "__main__":
    main()

"""
List Manager Version 11 Snapshot 3(Complete)
COPYRIGHT 2025 © Xiara Cclaere
"""