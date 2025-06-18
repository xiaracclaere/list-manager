# IMPORTS

import os, pickle, time, random # All of them are using.
from normal_errors import * # Needs a file named "normal_errors_1" and has all errors. 
from debug_errors import * # Needs a file named "debug_errors_1" and has all errors.
import performanceanalyzerv1 as performanceanalyzer # Needs original Performance Analyzer. 

# VARIABLES AND LISTS

global lst
lst = [] # This is our list. 
global counter
counter = 1 # This is our list counter. 
global mode
mode = 0 # This will make program from current mode to other mode. 
global using
using = 0 # This is decides to which functions will be used in debug mode. 
global timer
timer = 0 # This is the waiting time before running functions in debug mode. 
global exited
exited = False # This will control exiting program. 
global v
v = "12snapshot4" # This is lower name of current version. 
global V
V = "12 Snapshot 4" # This is upper name of current version. 
global sv
sv = "12s4" # This is short name of current verison. 

# ERROR CONTROL

def error_control(func): # Controls errors. (Not completed. )
    try:
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                functions.ProgramErrorLog(f"Error: {str(e)}")
        return wrapper
    except:
        TooManyErrors()

# MODE SWITCHING

def switch_mode(): # Changes mode. 
    global mode
    if mode == 0:
        functions.clear()
        print('Welcome to the List Manager Debug Mode! Write "help" to get help. \n')
        mode = 1
    else:
        functions.clear()
        print('Welcome to the List Manager! Write "help" to get help. \n')
        fun_fact()
        mode = 0

# MAIN MODE

class functions: # Functions of main mode. 
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
            print("Do you really want to do this?(Y/n): Y")

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
            SavingListError()
            
    def load(list_name="list"):
        global lst
        try:
            with open(f"{list_name}.pkl", "rb") as file:
                lst = pickle.load(file)
        except FileNotFoundError as e:
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            LoadingListError()
            lst = []
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            LoadingListError()
            lst = []
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
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
            functions.ProgramErrorLog(f"FileNotFoundError: {str(e)}")
            counter = 1
        except EOFError as e:
            functions.ProgramErrorLog(f"EOFError: {str(e)}")
            counter = 1
        except Exception as e:
            functions.ProgramErrorLog(f"Unknown error: {str(e)}")
            LoadingCounterError()
            counter = 1

    def autosave(func):
        try:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                functions.save(f"list{counter}")
                return result
            return wrapper
        except:
            AutosavingError()

    def autosave_counter(func):
        try:
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                functions.save_counter()
                return result
            return wrapper
        except:
            AutosavingCounterError()

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
Version = {sv}
News:
- 
Happy News:
The code increased from 808 to {lns} lines!

Hope you enjoy!
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

class actions: # Actions of main mode. 
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
                        EmptyInputError()
                        continue
                    else:
                        ItemIsNotOnListError()
                        break
                item = ""
            else:
                functions.clear()
                EmptyListError()
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
            EmptyListError()

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
                EmptyListError()
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
                EmptyListError()
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
                NoListsError()
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
                ExportingError()
        else:
            with open(f"list{counter}.txt", "a") as list_file:
                list_file.write(f"{message}\n")

def main_mode(): # Interface, checker and runner of main mode. 
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
        EmptyInputError()
    else:
        functions.clear()
        InvalidInputError()

# DEBUG MODE

class debug_functions: # Functions of debug mode. 
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

class debug_actions: # Actions of debug mode. 
    global menu
    def add(wi=True):
        time.sleep(timer)
        if wi:
            while True:
                item = input("Item: ")
                if item in lst:
                    raise IEILW
                elif not item:
                    raise EIE
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
                        raise EIE
                    else:
                        raise INILW
                item = ""
            else:
                raise EmLW
        else:
            lst.remove("debug_mode_test_item_4")

    def show():
        time.sleep(timer)
        if lst:
            for item in lst:
                print(item)
        else:
            raise EmLW

    def clean(wd=True):
        time.sleep(timer)
        if wd:
            if lst:
                lst.clear()
            else:
                raise EmLW
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
            raise ExLW
        
    def show_lists(st=True, l=10):
        time.sleep(timer)
        if st:
            if counter > 1:
                for i in range(1, counter):
                    print(f"list{i}")
            else:
                raise NCLW
        else:
            for i in range(1, l):
                    print(f"list{i}")

    def export(message=debug_functions.exporting):
        time.sleep(timer)
        try:
            with open(f"list{counter}.txt", "a") as list_file:
                list_file.write(f"{message}\n")
        except:
            raise ExLW

def debug_mode(): # Interface, checker and runner of debug mode. 
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
        performanceanalyzer.main()
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

def run_all(): # Runs all functions without input or message. 
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
    EmptyListError()
    AlreadyExistsError()
    EmptyInputError()
    ItemIsNotOnListError()
    LoadingListError()
    InvalidInputError()
    NoListsError()
    LoadingCounterError()
    ClearError()
    ExitingError()
    SavingListError()
    SavingCounterError()
    AutosavingError()
    AutosavingCounterError()
    ExportingError()
    ResettingError()
    ShowingCodeError()
    TooManyErrors()
    CodeError()
    UnknownError()
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

def run_order(): # Runs all functions with input and messages. 
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
    EmptyListError()
    AlreadyExistsError()
    EmptyInputError()
    ItemIsNotOnListError()
    LoadingListError()
    InvalidInputError()
    NoListsError()
    LoadingCounterError()
    ClearError()
    ExitingError()
    SavingListError()
    SavingCounterError()
    AutosavingError()
    AutosavingCounterError()
    ExportingError()
    ResettingError()
    ShowingCodeError()
    TooManyErrors()
    CodeError()
    UnknownError()
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

fun_facts   = ["The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "Bananas are berries, strawberries aren't.",
            "Honey never spoils, archaeologists found jars full of honey in ancient Egyptian tombs.",
            "Ducks' quacks don't echo, nobody knows why.",
            "Sea water is salty because there is the sea in it.",
            "The average person eats 8 spiders a year is a complete fabrication, but you can still sleep soundly. >:)",
            "When choosing the color of toothbrushes, it is actually difficult to decide among all the colors in the universe.",
            "A penguin is likely to be having fun while walking on land.",
            "Watermelons are the only fruit chosen by aliens, or maybe not.",
            "If a song repeats itself over and over, your brain memorizes it and you end up paying royalties to the song owner without even realizing it.",
            "If people actually lived 7.5 minutes longer, they would not be doing anything for the last 7.5 minutes.",
            "If a zombie stays in a room with you for 5 minutes, you don't forget to say 'Hi' to it.",
            "Actually, ostriches can fly but they are afraid.",
            "Watermelons just retain more water, but they're fun.",
            "If there is no world, you still exist, but perhaps on another planet. (Mysterious!)",
            "If you can read this, you are not blind.",
            "If you are reading this, you are not dead.",
            "If you are reading this, you are not a robot.",
            "If you are reading this, you are not a cat.",
            "If you are reading this, you are not a dog.",
            "If you are reading this, you are not a fish.",
            "You are you, me are me. ",
            "If you are reading this, you are not a tree.",
            "If you are reading this, you are not a rock.",
            "You can see this text in only List Manager, not in any other program.",
            "If you are reading this, you are not a human. >:)",
            "If you are reading this, you are not a computer.(can you?)",
            "If you are reading this, you are not a virus.",
            "You can't see this text in lower versions of List Manager.",
            "If you are reading this, you are not a bug."
            ] # Fun facts that will appear in starting program. 

def fun_fact(): # Gives fun fact. 
    print("Fun Fact:", random.choice(fun_facts),"\n")

# PROGRAM

def main(): # Main function of program. 
    functions.clear()
    functions.load_counter()
    functions.load(f"list{counter}")
    global exited

    print(f'Welcome to the List Manager! You can write "help" to get help. Version = {V} \n')
    
    fun_fact()
    
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

if __name__ == "__main__": # Runs main function. 
    main()

f"""
List Manager Version {V}(Complete)
COPYRIGHT 2025 © Xiara Cclaere
"""