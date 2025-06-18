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

try:
    import os
except ImportError as e:
    print(f"Error importing os module: {e}")

try:
    import psutil
except ImportError as e:
    print(f"Error importing psutil module: {e}")

try:
    import subprocess
except ImportError as e:
    print(f"Error importing subprocess module: {e}")

try:
    import requests
except ImportError as e:
    print(f"Error importing requests module: {e}")

try:
    import re
except ImportError as e:
    print(f"Error importing re module: {e}")

try:
    from normal_errors import *
except ImportError as e:
    print(f"Error importing normal errors: {e}")

try:
    from debug_errors import *
except ImportError as e:
    print(f"Error importing debug errors: {e}")

try:
    from lmcontrol_errors import *
except ImportError as e:
    print(f"Error importing lmcontrol errors: {e}")

try:
    from banners import *
except ImportError as e:
    print(f"Error importing banners: {e}")

try:
    from lmuiprovider import *
except ImportError as e:
    print(f"Error importing list manager ui provider: {e}")

try:
    from lmconfigurator import *
except ImportError as e:
    print(f"Error importing list manager configurator: {e}")

try:
    import performanceanalyzerv1 as performanceanalyzer
except ImportError as e:
    print(f"Error importing performanceanalyzer: {e}")

#----------------------------------------------

# GLOBAL VARIABLES AND LISTS

#----------------------------------------------

current_file = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_file, "config.json")
data_file = os.path.join(current_file, "lmdata.json")
lm_folder = os.path.dirname(os.path.abspath(__file__))
manifest_file = "https://raw.githubusercontent.com/xiaracclaere/list-manager/main/MANIFEST.json"

current_lm_version = ""

choices = ["Check", "History", "Update", "Fix", "Install", "Remove", "Reset", "Reinstall", "Remove Control", "Clean Installation", "Exit"]

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

def find_version():
    global current_lm_version

    files = os.listdir(current_file)

    candidates = [f for f in files if f.startswith("listmanagerv") and f.endswith(".py")]

    if not candidates:
        current_lm_version = None
        return None

    file = candidates[0]

    match = re.search(r'v[\d\w]+', file)
    if match:
        current_lm_version = match.group(0)
        return current_lm_version
    else:
        current_lm_version = None
        return None

def normalize_version(name: str) -> str:
    if name.startswith("listmanager"):
        return name[len("listmanager"):]
    return name

def check_updates_with_return():
    global manifest_file, current_lm_version
    clear()
    try:
        print("Checking for updates...")
        r = requests.get(manifest_file)
        manifest = r.json()

        lm_versions = [normalize_version(k) for k in manifest]
        latest = lm_versions[-1] if lm_versions else None
    except Exception as e:
        print("Failed to check updates:", e)
        return None
    
    return latest

def check_updates():
    global manifest_file, current_lm_version
    clear()
    try:
        print("Checking for updates...")
        r = requests.get(manifest_file)
        manifest = r.json()

        lm_versions = [normalize_version(k) for k in manifest]
        latest = lm_versions[-1] if lm_versions else None

        if not latest:
            print("No versions found in manifest. ")
            return

        print(f"Latest version found: {latest}")
        print(f"Your current version: {current_lm_version or 'Unknown'}")

        if current_lm_version and current_lm_version == latest:
            print("You are using the latest version. ")
        else:
            print("Update available! ")
            print("Use 'update' option to upgrade. ")
    except Exception as e:
        print("Failed to check updates:", e)

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

def show_history():
    if not history:
        print("History is empty.")
    else:
        print("History: ")
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item}")

def update():
    global current_lm_version
    clear()
    print("Checking for updates...")
    
    latest = check_updates_with_return()

    if not latest:
        print("No version info found.")
        return

    print(f"Latest version found: {latest}")
    print(f"Your current version: {current_lm_version or 'Unknown'}")

    if current_lm_version and current_lm_version == latest:
        print("You are already using the latest version.")
        return

    if "snapshot" in latest.lower():
        print("Snapshot version detected. Keeping current version and installing snapshot separately...")
        install(latest)
    else:
        print("Stable version detected. Replacing current version...")
        current_file_path = os.path.join(lm_folder, f"listmanager{current_lm_version}.py")
        if os.path.exists(current_file_path):
            os.remove(current_file_path)
            print(f"Removed old version: {current_lm_version}")
        install(latest)

    print("Update completed.")

def fix():
    pass # will be created

def install_file(url, path):
    try:
        r = requests.get(url)
        r.raise_for_status()

        with open(path, "wb") as f:
            f.write(r.content)

        print(f"Downloaded and saved to: {path}")

    except Exception as e:
        print(f"Error installing file from {url}: {e}")

def install(target=None):
    global manifest_file
    clear()
    try:
        print("Fetching manifest...")
        r = requests.get(manifest_file)
        r.raise_for_status()
        manifest = r.json()

        print("\nAvailable files in manifest:")
        for key in manifest:
            print(f"  - {key}")

        if not target:
            target = input("\nEnter the file name to install: ").strip()
            clear()

        if target not in manifest:
            print(f"'{target}' not found in manifest.")
            return

        url = manifest[target]["url"]

        filename = f"listmanager{target}.py" if target.startswith("v") else f"{target}.py"
        filepath = os.path.join(current_file, filename)

        print(f"Installing '{target}' from: {url}")
        install_file(url, filepath)

    except Exception as e:
        print(f"Failed to install file: {e}")

def remove(force=False):
    pass # will be created

def clean_installation():
    choice = input("Are you sure you want to perform a clean installation? (y/n): ").strip().lower()
    clear()
    try:
        if choice == "y" or choice == "":
            if os.path.exists(config_file):
                os.remove(config_file)
            if os.path.exists(data_file):
                os.remove(data_file)
            if os.path.exists(os.path.join(current_file, "lmconfigurator.py")):
                os.remove(os.path.join(current_file, "lmconfigurator.py"))
            if os.path.exists(os.path.join(current_file, "lmuiprovider.py")):
                os.remove(os.path.join(current_file, "lmuiprovider.py"))
            if os.path.exists(os.path.join(current_file, "lmcontrol.py")):
                os.remove(os.path.join(current_file, "lmcontrol.py"))
            if os.path.exists(os.path.join(current_file, "lmcontrol_errors.py")):
                os.remove(os.path.join(current_file, "lmcontrol_errors.py"))
            if os.path.exists(os.path.join(current_file, "normal_errors.py")):
                os.remove(os.path.join(current_file, "normal_errors.py"))
            if os.path.exists(os.path.join(current_file, "debug_errors.py")):
                os.remove(os.path.join(current_file, "debug_errors.py"))
            if os.path.exists(os.path.join(current_file, "banners.py")):
                os.remove(os.path.join(current_file, "banners.py"))
            if os.path.exists(os.path.join(current_file, "performanceanalyzerv1.py")):
                os.remove(os.path.join(current_file, "performanceanalyzerv1.py"))
            if os.path.exists(os.path.join(current_file, "listmanager" + current_lm_version + ".py")):
                os.remove(os.path.join(current_file, "listmanager" + current_lm_version + ".py"))
            install("lmconfigurator")
            install("lmuiprovider")
            install("lmcontrol")
            install("lmcontrol_errors")
            install("normal_errors")
            install("debug_errors")
            install("banners")
            install("performanceanalyzerv1")
            print("Clean installation completed. ")
        else:
            print("Clean installation cancelled. ")
    except Exception as e:
        print(f"An error occurred during clean installation: {e}")
        
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
        elif choice == "clean installation":
            clean_installation()
        elif choice == "exit":
            exiting()
        else:
            InvalidInputError()

#----------------------------------------------

# RUNNING THE PROGRAM

#----------------------------------------------

if __name__ == "__main__":
    main()