import os, configparser

current_file = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_file, "lmconfig.cfg")
main_choices_all = ["Add", "Delete", "List", "Clean", "Sort", "New", "Lists", "Export", "Help", "History", "Reset", "Code", "Mode", "Exit"]
debug_choices_all = ["Add", "Delete", "List", "Clean", "Clear", "Sort", "Export", "Timer", "Performance", "Use", "Reset", "Code", "Help", "Mode", "History", "Exit"]
main_choices_showing = []
debug_choices_showing = []
options = configparser.ConfigParser()

def default_config():
        options = configparser.ConfigParser()
        with open(config_file, "w") as configfile:
            options["ShowCommandsNormalMode"] = {
                "add": "true",
                "delete": "true",
                "list": "true",
                "clean": "true",
                "sort": "true",
                "new": "true",
                "lists": "true",
                "export": "true",
                "help": "true",
                "history": "true",
                "reset": "false",
                "code": "false",
                "mode": "false",
                "exit": "true"
            }
            options["ShowCommandsDebugMode"] = {
                "add": "true",
                "delete": "true",
                "list": "true",
                "clean": "true",
                "clear": "true",
                "sort": "true",
                "export": "true",
                "timer": "true",
                "performance": "true",
                "use": "true",
                "reset": "true",
                "code": "true",
                "help": "true",
                "mode": "true",
                "history": "true",
                "exit": "true"
            }
            options["Startup"] = {
                "banner": "true",
                "funfact": "true"
            }
            options["Visual"] = {
                "gclear": "true",
                "mclear": "true",
                "dclear": "false",
                "cclear": "false"
            }
            options["Settings"] = {
                "using": "0",
                "timer": "0",
                "mode": "0",
                "autosave": "true",
                "configfile": "lmconfig.cfg",
                "datafile": "lmdata.json",
                "reset": "true",
                "export": "true"
            }
            options["EnablesandDisables"] = {
                "resetoptions": "false",
                "usingaffectsnormalmode": "true",
                "usingaffectsdebugmode": "true",
                "startasdebugmode": "false",
                "startasnormalmode": "true",
                "startasconfigmode": "false",
                "users": "false",
                "writehistory": "true",
                "writeerrorlogs": "true",
                "usingoriginalfiles": "true",
                "usingoriginalmodules": "true",
                "usingoriginalbanners": "true",
                "usingoriginalerrors": "true",
                "usingoriginalui": "true",
                "usingoriginalaccounts": "true",
                "usingoriginalconfig": "true",
                "usingoriginaldata": "true",
                "usingoriginalperformanceanalyzer": "true",
                "ignoreerrors": "false",
                "ignoredebugerrors": "false",
                "allowswitchmode": "true"
            }
            options.write(configfile)
    
def load_config():
    global options
    try:
        options.read(config_file)
        if not os.path.exists(config_file):
            raise FileNotFoundError
    except FileNotFoundError:
        with open(config_file, "w") as configfile:
            default_config()
            options.write(configfile)

def setup_showing_commands():
    global main_choices_showing, debug_choices_showing, options
    load_config()
    main_choices_showing = []
    debug_choices_showing = []
    
    for command in main_choices_all:
        if options["ShowCommandsNormalMode"][command] == "true":
            main_choices_showing.append(command)
    
    for command in debug_choices_all:
        if options["ShowCommandsDebugMode"][command] == "true":
            debug_choices_showing.append(command)