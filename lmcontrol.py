#----------------------------------------------

# WELCOME TO THE LIST MANAGER CONTROL!
# Happy to see you here!
# You can use this program for control your List Manager program.
# As Xiara Cclaere, I'm thankful to you for using this program.
# Here's the official repository of the List Manager Control: https://www.github.com/xiaracclaere/list-manager/
# For one file: https://raw.githubusercontent.com/xiaracclaere/list-manager/
# :)

#----------------------------------------------

#|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|
#||||||||||||||||||||||||||||||||||||||||||||||
#|\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|

#----------------------------------------------

# IMPORTS

#----------------------------------------------

import os, psutil, subprocess
from normal_errors import *
from debug_errors import *
from lmcontrol_errors import *
from banners import *
from lmuiprovider import *
from lmconfigurator import *
import performanceanalyzerv1 as performanceanalyzer

#----------------------------------------------

# GLOBAL VARIABLES AND LISTS

#----------------------------------------------

current_file = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_file, "config.json")
data_file = os.path.join(current_file, "lmdata.json")

choices = ["Check", "History", "Update", "Fix", "Install", "Remove", "Reset", "Reinstall", "Remove Control", "Exit"]

check_choices = ["Updates", "Files", "Data", "Performance"]
performance_choices = ["Performance Analyzer", "Momentary"]

history = []

#----------------------------------------------

# FUNCTIONS

#----------------------------------------------

def exiting():
    clear()
    print("Exiting List Manager Control... ")
    exit(0)

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        ClearError()

def check_updates():
    pass # will be created

def check_files():
    pass # will be created

def check_data():
    pass # will be created

def check_performance():
    clear()
    print(cui(style2, performance_choices))
    choice = input().strip().lower()
    if choice == "performance analyzer":
        performanceanalyzer.main()
    elif choice == "momentary":
        clear()
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        total_ram = ram.total / (1024 * 1024)
        using_ram = ram.used / (1024 * 1024)
        free_ram = ram.available / (1024 * 1024)
        print(f"""
CPU usage: {cpu}%
Total RAM: {total_ram} MB
Using RAM: {using_ram} MB
Free RAM: {free_ram} MB
""")

def check():
    clear()
    print(cui(style2, check_choices))
    checking = input().strip().lower()
    if checking == "updates":
        check_updates()
    elif checking == "files":
        check_files()
    elif checking == "data":
        check_data()
    elif checking == "performance":
        check_performance()
    else:
        CheckingError()

def history():
    if not history:
        print("History is empty.")
    else:
        print("History: ")
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item}")

def update():
    pass # will be created

def fix():
    pass # will be created

def install():
    pass # will be created

def remove(force=False):
    pass # will be created

def reset():
    choice = input("Are you sure you want to reset the List Manager? (y/n): ").strip().lower()
    clear()
    if choice == "y" or choice == "":
        if os.path.exists(config_file):
            os.remove(config_file)
        if os.path.exists(data_file):
            os.remove(data_file)
        print("List Manager has been reset.")
    else:
        print("Reset cancelled.")

def reinstall():
    choice = input("Are you sure you want to reinstall the List Manager? (y/n): ").strip().lower()
    clear()
    if choice == "y" or choice == "":
        remove(force=True)
        print("List Manager is removed now. Installing new one... ")
        install()
        print("List Manager has been reinstalled. ")
    else:
        print("Reinstall cancelled.")

def remove_control():
    choice = input("Are you sure you want to remove the List Manager Control? (y/n): ").strip().lower()
    clear()
    if choice == "y" or choice == "":
        if os.name == "nt":
            subprocess.run(f"del /f /q {current_file} & echo 'List Manager Control has been removed.'", shell=True)
        else:
            subprocess.run(f"rm -rf {current_file} && echo 'List Manager Control has been removed.'", shell=True)
    else:
        print("Remove cancelled.")

def create_menu():
    return cui(style2, choices)

#----------------------------------------------

# MAIN FUNCTION

#----------------------------------------------

def main():
    clear()

    print("Welcome to the List Manager Control! This program helps you to control your List Manager program! \n")
    
    while True:
        print(create_menu())
        choice = input().strip().lower()
        if choice == "check":
            check()
        elif choice == "history":
            history()
        elif choice == "update":
            update()
        elif choice == "fix":
            fix()
        elif choice == "install":
            install()
        elif choice == "remove":
            remove()
        elif choice == "reset":
            reset()
        elif choice == "reinstall":
            reinstall()
        elif choice == "remove control":
            remove_control()
        elif choice == "exit":
            exiting()
        else:
            InvalidInputError()

#----------------------------------------------

# RUNNING THE PROGRAM

#----------------------------------------------

if __name__ == "__main__":
    main()