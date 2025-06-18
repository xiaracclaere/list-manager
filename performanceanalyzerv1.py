import psutil, keyboard, time, os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("Unsupported OS")
        globals()['clear_screen'] = lambda: None

def splash():
    clear_screen()
    print(
"""Performance Analyzer v1. 
    
Press 's' to start performance analyzer, press 't' to stop performance analyzer, press 'd' to toggle detailed mode, press 'e' to exit. """)

def main():
    splash()
    while True:
        if keyboard.is_pressed("s"):
            clear_screen()
            print("Wait... ")
            detailed = False
            time.sleep(1)
            clear_screen()
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
                if keyboard.is_pressed("d"):
                    if detailed:
                        detailed = False
                    else:
                        detailed = True
                if keyboard.is_pressed("t"):
                    clear_screen()
                    input("Performance analyzer stopped. Press enter to continue... ")
                    splash()
                    break
                if keyboard.is_pressed("e"): 
                    clear_screen()
                    print("Exiting...")
                    break
        if keyboard.is_pressed("e"): 
                clear_screen()
                print("Exiting...")
                break