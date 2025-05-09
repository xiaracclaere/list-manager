# IMPORTS

import os, pickle, time, keyboard, psutil, random

# VARIABLES AND LISTS

lst = []
counter = 1
global mode
mode = 0
global using
using = 0
global timer
timer = 0
global exited
exited = False

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

# MODE SWITCHING

def switch_mode():
    global mode
    if mode == 0:
        functions.clear()
        mode = 1
    else:
        functions.clear()
        mode = 0

# MAIN MODE

class functions:
    global mode
    def check(real=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if real:
            control = input("Do you really want to do this?(Y/n): ")
            if control == "Y" or control == "y" or control == "":
                do = True
            else:
                do = False
            return do
        else:
            print("Do you really want to do this?(Y/n): ")

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
        if using == 1:
            time.sleep(timer)
        else:
            pass
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
        if using == 1:
            time.sleep(timer)
        else:
            pass
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
        if using == 1:
            time.sleep(timer)
        else:
            pass
        functions.clear()
        main()

    def show_code():
        if using == 1:
            time.sleep(timer)
        else:
            pass
        functions.clear()
        with open(__file__, "r", encoding="utf-8") as file:
            print(file.read())

    def about_version(): 
        if using == 1:
            time.sleep(timer)
        else:
            pass
        functions.clear()
        with open(__file__, "r", encoding="utf-8") as file:
            lns = len(file.readlines())
        print(f"""
Version = 11.2
News:
- FUN FACTS!
Happy News:
The code increased from 946 to {lns} lines!

Enjoy!
            """)

    def exiting():
        global exited
        if using == 1:
            time.sleep(timer)
        else:
            pass
        functions.clear()
        functions.save(f"list{counter}")
        functions.save_counter()
        print("Exiting program... ")
        exit
        exited = True

class actions:
    global mode
    @functions.autosave
    def add(with_input=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_input:
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
        else:
            lst.append("debug_mode_test_item_1")
            lst.append("debug_mode_test_item_2")

    @functions.autosave
    def delete(with_input=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_input:
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
        else:
            lst.remove("debug_mode_test_item_1")

    def show():
        if using == 1:
            time.sleep(timer)
        else:
            pass
        functions.clear()
        if lst:
            for a, i in enumerate(lst, start=1):
                print(f"{a}. {i}")
        else:
            errors.EmptyListError()

    @functions.autosave
    def clean(with_do=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_do:
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
        else:
            lst.clear()
            lst.append("debug_mode_test_item_3")

    def sort(item):
        return item

    @functions.autosave
    def sort_list(with_do=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_do:
            if lst:
                do = functions.check()
                functions.clear()
                if do:
                    lst.sort(key=actions.sort)
                    print("List is sorted successfully!")
                else:
                    pass
            else:
                functions.clear()
                errors.EmptyListError()
        else:
            lst.sort(key=actions.sort)

    @functions.autosave_counter
    def new_list(with_note=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_note:
            global lst, counter
            functions.save(f"list{counter}")
            counter += 1
            lst = []
            functions.clear()
            print(f"Created new list: lst{counter}")
            functions.save(f"list{counter}")
        else:
            counter += 1
            lst = []

    def show_lists(show_truth=True, lists=10):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if show_truth:
            functions.clear()
            if counter > 1:
                for i in range(1, counter):
                    print(f"lst{i}")
            else:
                errors.NoListsError()
        else:
            for i in range(1, lists):
                print(f"list{i}")

    def export(message=functions.exporting, with_note=True):
        if using == 1:
            time.sleep(timer)
        else:
            pass
        if with_note:
            try:
                with open(f"list{counter}.txt", "a") as list_file:
                    list_file.write(f"{message}\n")
                functions.clear()
                print(f"List is exported with name: list{counter}.txt ! ")
            except:
                errors.ExportingError()
        else:
            with open(f"list{counter}.txt", "a") as list_file:
                list_file.write(f"{message}\n")

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
        print("Kod gösterme başarısız oldu! ")
        
    def TooManyErrors():
        print("Too many errors! ")
    
    def CodeError():
        print("Program kodunda bir hata oluştu! ")

    def UnknownError():
        print("An unknown error has occured! ")

def main_mode():
    global mode
    action = input(f"| Add | Delete | List | Clean | Sort | New | Lists | Export | Help | Exit | \n").strip().lower()
    if action == "add":
        actions.add()
    elif action == "delete":
        actions.delete()
    elif action == "list":
        actions.show()
    elif action == "clean":
        actions.clean()
    elif action == "sort":
        actions.sort_list()
    elif action == "new":
        actions.new_list()
    elif action == "version":
        functions.about_version()
    elif action == "lists":
        actions.show_lists()
    elif action == "export":
        actions.export(functions.exporting())
    elif action == "help":
        functions.helping()
    elif action == "reset":
        functions.reset()
    elif action == "code":
        functions.show_code()
    elif action == "mode":
        switch_mode()
    elif action == "exit":
        functions.exiting()
    elif action == "":
        functions.clear()
        errors.EmptyInputError()
    else:
        functions.clear()
        errors.InvalidInputError()

# DEBUG MODE

class debug_functions:
    global mode
    def DebugProgramErrorLog(message):
        time.sleep(timer)
        with open("dm_program_error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def DebugErrorLog(message):
        time.sleep(timer)
        with open("dm_error_logs.txt", "a") as log_file:
            log_file.write(f"{message}\n")

    def clear():
        time.sleep(timer)
        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
        else:
            raise debug_errors.ClearingScreenError

    def exporting():
        for i in lst:
            e = i
            return e

    def check_in_pa():
        if keyboard.is_pressed("d"):
            if detailed:
                detailed = False
            else:
                detailed = True
        elif keyboard.is_pressed("r"):
            while True:
                run_type = input("To run all; 'a', To run in order; 'o': ")
                if run_type == "a":
                    run_all()
                    break
                elif run_type == "o":
                    input("NOTE: You'll get an error in this mode! Press enter to continue... ")
                    run_order()
                    break
                else:
                    raise debug_errors.InvalidInputError
    
    def performance_analyzer():
        time.sleep(timer)
        print("Debug Mode Performance Analyzer Local Version(Beta). \n", "Press 's' to start or stop performance analyzer, press 'e' to exit, press 'r' and 'o' to run all functions in order, press 'r' and 'a' to run all functions in one time. ")
        while True:
            time.sleep(0.1)
            if keyboard.is_pressed("s"):
                debug_functions.clear()
                print("Wait... ")
                detailed = False
                debug_functions.clear()
                time.sleep(1)
                while True:
                    cpu = psutil.cpu_percent(interval=1)
                    ram = psutil.virtual_memory()
                    total_ram = ram.total / (1024 * 1024)
                    using_ram = ram.used / (1024 * 1024)
                    free_ram = ram.available / (1024 * 1024)
                    print(f"CPU usage: {cpu}%")
                    if detailed:
                        print(f"Total RAM: {total_ram} MB")
                        print(f"Free RAM: {free_ram} MB")
                    print(f"Using RAM: {using_ram} MB")
                    if keyboard.is_pressed("s"):
                        break
                    debug_functions.check_in_pa()

    def helping():
        time.sleep(timer)
        print(f"List Manager Debug Mode Help Menu: \n", """
Add: actions.add
Delete: actions.delete
List: actions.show actions.show_list
Clean: actions.clean
Sort: list.sort actions.sort
New: actions.new_list
Export: actions.export
Code: debug_functions.show_code
Help: debug_functions.helping
Exit: debug_functions.exiting
            """)

    def reset():
        time.sleep(timer)
        main()

    def show_code():
        time.sleep(timer)
        with open(__file__, "r", encoding="utf-8") as file: 
            print(file.read())

    def exiting():
        global exited
        time.sleep(timer)
        exited = True
        exit

class debug_actions:
    global menu
    def add(wi=True):
        time.sleep(timer)
        if wi:
            while True:
                item = input("Item: ")
                if item in lst:
                    raise debug_errors.IEILWarning
                elif not item:
                    raise debug_errors.EmptyInputError
                else:
                    lst.append(item)
                    break
            item = ""
        else:
            lst.append("debug_mode_test_item_4")
            lst.append("debug_mode_test_item_5")

    def delete(wi=True):
        time.sleep(timer)
        if wi:
            if lst:
                while True:
                    item = input("Item: ")
                    if item in lst:
                        lst.remove(item)
                        break
                    elif not item:
                        raise debug_errors.EmptyInputError
                    else:
                        raise debug_errors.INILWarning
                item = ""
            else:
                raise debug_errors.EmptyListWarning
        else:
            lst.remove("debug_mode_test_item_4")

    def show():
        time.sleep(timer)
        if lst:
            for item in lst:
                print(item)
        else:
            raise debug_errors.EmptyListWarning

    def clean(wd=True):
        time.sleep(timer)
        if wd:
            if lst:
                lst.clear()
            else:
                raise debug_errors.EmptyListWarning
        else:
            lst.clear()
            lst.append("debug_mode_test_item_6")

    def sort(item):
        return item

    def sort_list():
        time.sleep(timer)
        if lst:
                lst.sort(key=debug_actions.sort)
        else:
            raise debug_errors.EmptyListWarning
        
    def show_lists(st=True, l=10):
        time.sleep(timer)
        if st:
            if counter > 1:
                for i in range(1, counter):
                    print(f"list{i}")
            else:
                raise debug_errors.NoCreatedListsWarning
        else:
            for i in range(1, l):
                    print(f"list{i}")

    def export(message=debug_functions.exporting):
        time.sleep(timer)
        try:
            with open(f"list{counter}.txt", "a") as list_file:
                list_file.write(f"{message}\n")
        except:
            raise debug_errors.ExportingListWarning

class debug_errors:
    class EmptyListWarning(Warning):
        def __init__(self, message="List is empty! "):
            super().__init__(message)

    class IEILWarning(Warning):
        def __init__(self, message="Item is exists in list! "):
            super().__init__(message)

    class EmptyInputError(Exception):
        def __init__(self, message="Input is empty, write something! "):
            super().__init__(message)
    
    class INILWarning(Warning):
        def __init__(self, message="Item is not in list! "):
            super().__init__(message)
    
    class LoadingListError(Exception):
        def __init__(self, message="An error occured while loading list! "):
            super().__init__(message)
    
    class InvalidInputError(Exception):
        def __init__(self, message="Input is invalid, write something valid! "):
            super().__init__(message)
    
    class NoCreatedListsWarning(Warning):
        def __init__(self, message="You don't created and saved lists except current list! "):
            super().__init__(message)
    
    class LoadingCounterError(Exception):
        def __init__(self, message="An error occured while loading counter! "):
            super().__init__(message)

    class ClearingScreenError(Exception):
        def __init__(self, message="Cannot clean your terminal! "):
            super().__init__(message)

    class ExitingProgramError(Exception):
        def __init__(self, message="An error occured while exiting program! "):
            super().__init__(message)

    class SavingListWarning(Warning):
        def __init__(self, message="An error occured while saving list! "):
            super().__init__(message)

    class SavingCounterWarning(Warning):
        def __init__(self, message="An error occured while saving counter! "):
            super().__init__(message)
        
    class AutosavingListWarning(Warning):
        def __init__(self, message="An error occured while autosaving list! "):
            super().__init__(message)

    class AutosavingCounterWarning(Warning):
        def __init__(self, message="An error occured while autosaving counter! "):
            super().__init__(message)
        
    class ExportingListWarning(Warning):
        def __init__(self, message="An error occured while exporting list! "):
            super().__init__(message)
    
    class ResettingProgramError(Exception):
        def __init__(self, message="An error occured while resetting program! "):
            super().__init__(message)

    class ShowingCodeError(Exception):
        def __init__(self, message="An error occured while showing code! "):
            super().__init__(message)
    
    class TooManyErrors(Exception):
        def __init__(self, message="Too many errors occured! "):
            super().__init__(message)

    class ProgramError(Exception):
        def __init__(self, message="A program code error has occured. "):
            super().__init__(message)

    class UnknownError(Exception):
        def __init__(self, message="An unknown error has occured! "):
            super().__init__(message)

def debug_mode():
    global mode
    global using
    global timer
    action = input(f"| Add | Delete | List | Clean | Clear | Sort | Export | Timer | Performance | Use | Code | Help | Mode | Exit | \n").strip().lower()
    if action == "add":
        if using == 0:
            debug_actions.add()
        else:
            actions.add()
    elif action == "delete":
        if using == 0:
            debug_actions.delete()
        else:
            actions.delete()
    elif action == "list":
        if using == 0:
            debug_actions.show()
        else:
            actions.show()
    elif action == "clean":
        if using == 0:
            debug_actions.clean()
        else:
            actions.clean()
    elif action == "clear":
        debug_functions.clear()
    elif action == "sort":
        if using == 0:
            debug_actions.sort_list()
        else:
            actions.sort_list()
    elif action == "export":
        if using == 0:
            debug_actions.export(debug_functions.exporting)
        else:
            actions.export(functions.exporting)
    elif action == "timer":
        timer = float(input("Enter waiting time: "))
    elif action == "performance":
        debug_functions.performance_analyzer()
    elif action == "use":
        if using == 0:
            debug_functions.clear()
            using = 1
        else:
            debug_functions.clear()
            using = 0
    elif action == "code":
        debug_functions.show_code()
    elif action == "help":
        if using == 0:
            debug_functions.helping()
        else:
            functions.helping()
    elif action == "mode":
        switch_mode()
    elif action == "exit":
        if using == 0:
            debug_functions.exiting()
        else:
            functions.exiting()

# RUNNING ALL

def run_all():
    functions.check(False)
    functions.ProgramErrorLog("Error: Not an error! ")
    functions.ErrorLog("Error: Not an error! ")
    functions.save()
    functions.load()
    functions.save_counter()
    functions.clear()
    functions.helping()
    functions.show_code()
    functions.about_version()
    actions.add(False)
    actions.delete(False)
    actions.show()
    actions.clean(False)
    actions.sort_list(False)
    actions.new_list(False)
    actions.show_lists(False, 10)
    actions.export(functions.exporting, False)
    errors.EmptyListError()
    errors.AlreadyExistsError()
    errors.EmptyInputError()
    errors.ItemIsNotOnListError()
    errors.LoadingListError()
    errors.InvalidInputError()
    errors.NoListsError()
    errors.LoadingCounterError()
    errors.ClearError()
    errors.ExitingError()
    errors.SavingListError()
    errors.SavingCounterError()
    errors.AutosavingError()
    errors.AutosavingCounterError()
    errors.ExportingError()
    errors.ResettingError()
    errors.ShowingCodeError()
    errors.TooManyErrors()
    errors.CodeError()
    errors.UnknownError()
    debug_functions.clear()
    debug_functions.helping()
    debug_functions.show_code()
    debug_actions.add(False)
    debug_actions.delete(False)
    debug_actions.show()
    debug_actions.clean(False)
    debug_actions.sort_list()
    debug_actions.show_lists(False, 10)
    debug_actions.export(debug_functions.exporting)
    debug_functions.reset()

def run_order():
    functions.check()
    functions.ProgramErrorLog("Error: Not an error! ")
    functions.ErrorLog("Error: Not an error! ")
    functions.save()
    functions.load()
    functions.save_counter()
    functions.clear()
    functions.helping()
    functions.show_code()
    functions.about_version()
    actions.add()
    actions.delete()
    actions.show()
    actions.clean()
    actions.sort_list()
    actions.new_list()
    actions.show_lists()
    actions.export()
    errors.EmptyListError()
    errors.AlreadyExistsError()
    errors.EmptyInputError()
    errors.ItemIsNotOnListError()
    errors.LoadingListError()
    errors.InvalidInputError()
    errors.NoListsError()
    errors.LoadingCounterError()
    errors.ClearError()
    errors.ExitingError()
    errors.SavingListError()
    errors.SavingCounterError()
    errors.AutosavingError()
    errors.AutosavingCounterError()
    errors.ExportingError()
    errors.ResettingError()
    errors.ShowingCodeError()
    errors.TooManyErrors()
    errors.CodeError()
    errors.UnknownError()
    debug_functions.clear()
    debug_functions.helping()
    debug_functions.show_code()
    debug_actions.add()
    debug_actions.delete()
    debug_actions.show()
    debug_actions.clean()
    debug_actions.sort_list()
    debug_actions.show_lists()
    debug_actions.export()
    debug_functions.reset()

# FUN FACTS

fun_facts= ["The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "Bananas are berries, strawberries aren't.",
            "Honey never spoils, archaeologists found jars full of honey in ancient Egyptian tombs."]

def fun_fact():
    print("Fun Fact:", random.choice(fun_facts),"\n")

# PROGRAM

def main():
    functions.clear()
    functions.load_counter()
    functions.load(f"list{counter}")
    global exited

    print('Welcome to the List Manager! You can write "help" to get help. Version = 11.2 ')
    
    while True:
        if mode == 0:
            main_mode()
            if exited:
                break
        else:
            print("Debug Mode")
            debug_mode()
            if exited:
                break

# RUNNING PROGRAM

if __name__ == "__main__":
    main()

"""
List Manager Version 11.2
COPYRIGHT 2025 © Xiara Cclaere
THE FUNNIEST UPDATE
"""