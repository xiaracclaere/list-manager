# List Manager Update Notes

**You can find new features, bug fixes etc. of versions in this file.**

# Old Versions

## List Manager v1

I think you don't need it.

## List Manager v2

**_Features:_**

- Clean

    - Deletes all items in the list.

- Clear

    - Clears your terminal screen almost in every action for a better look.

**_Errors:_**

- Empty List Error (New)

    - Notifies you about the list is empty.

    - Usage(s): 
        
        - Action is "l"
        - Action is "c"

- Empty Input Error (New)

    - Notifies you about you didn’t enter anything into the input.

    - Usage(s): 
        
        - Action is "" or " "

## List Manager v3

**_UI:_**

- Renewed UI

    - Old UI: Add(a)  Delete(d)  List(l)  Clean(c)  Exit(e)

    - New UI: | Add | Delete | List | Clean | Exit |

**_Compatibility:_**

- Words are Letters

    - You can now type either the first letter or the full word of a command.

    - Affects to:

        - "a" with "add"
        - "d" with "delete"
        - "l" with "list"
        - "c" with "clean"
        - "e" with "exit"

**_Errors:_**

- Empty Input Error (Edited)

    - Notifies you about you didn’t enter anything into the input.

    - Usage(s): 
        
        - Action is ""

## List Manager v4

**_Performance and Compatibility:_**

- Functions

    - Now all operations are defined in advance by function instead of being processed in a loop.

    - Usage(s):

        - While loop
    
    - Affects to:

        - Code of 'Action is "a" or "add"' with function "add"
        - Code of 'Action is "d" or "delete"' with function "delete"
        - Code of 'Action is "l" or "list"' with function "list"
        - Code of 'Action is "c" or "clean"' with function "clean"
        - Code of 'Action is "e" or "exit"' with function "exit"
        - Error "Empty Input Error" with function "empty"
        - Error "Invalid Input Error" with function "invalid"

## List Manager v5

**_Performance:_**

- Variables

    - New unusual variable "screencanbecleared"

- Functions

    - Exit
 
      - Added an unusual "break" for loop at down of exit().

**_Compatibility:_**

- Input

  - Now all letters of the command you enter will be lowercase.

- Functions

    - Clear

        - Now clearing terminal screen is compatible with these operating systems:

            - nt (Windows)
            - posix (Linux)
        
        - If operating system is not compatible, screen clearing function is disables itself. 

## List Manager v5.1

**_Performance:_**

- Functions

  - Function names are shortened to 3 characters.
 
    - Affects to:
   
      - Function "clear" with "clr"
      - Function "delete" with "dlt"
      - Function "list" with "shw"
      - Function "clean" with "cln"
      - Function "exit" with "ext"
      - Function "empty" with "emp"
      - Function "invalid" with "inv"

## List Manager v5.2

**_Bug Fixes:_**

- Function

  - Clear
 
    - Disabling itself is has an error before:
   
      globals()["fonk"] = lambda *args, **kwargs: None

     - It's fixed:
   
      globals()["clr"] = lambda *args, **kwargs: None

**_Performance and Compatibility:_**

- Input

  - It now converts the text you enter to lowercase letters instead of converting it to lowercase letters later. This also applies to the new strip feature.

## List Manager v6

**Features:_**

- Save

  - Saves the list to a file with module "pickle" of Python.
 
- Load

  - Loads a list file to list with module "pickle" of Python.

**Performance:_**

- Functions

  - Function names are resetted with some changes. 
 
    - Affects to:
   
      - Function "clr" with "clear"
      - Function "dlt" with "delete"
      - Function "shw" with "show"
      - Function "cln" with "clean"
      - Function "ext" with "exiting"
      - Function "emp" with "empty"
      - Function "inv" with "invalid"

- Loop

  - New Loop Control System
 
    - Old Loop: while action != "e"
   
    - New Loop: while True

**_Modifications:_**

- Functions

  - Exit
 
    - Saves list before exiting. 

## List Manager v7

**_Features and Errors:_**

- Functions

  - EmptyError
 
    - This function is callable version of Empty List Error.

  - Sort
 
    - Sorts the list.

**_Compatibility:_**

- Words Are Not Letters

  - Now you can only type full name of action you want to do.
 
    - Affects to:
   
      - "a" and "add" with "add"
      - "d" and "delete" with "delete"
      - "l" and "list" with "list"
      - "c" and "clean" with "clean"
      - "e" and "exit" with "exit"

      **Note:** Sort is came in this version with only "sort".

## List Manager v8

Nothing's changed.

## List Manager v8.1

**_Errors:_**

- Loading List Error (New)

  - Notifies you about List Manager got a error while loading the list file.
 
  - Usage(s)
 
    - Load

Clearing Screen Error (New)

  - Notifies you about your terminal doesn't supports clear terminal or List Manager is not knowing your terminal clearing command.

  - Usage(s)

    - Clear

**_Modifications and Performance:_**

- Functions

  - Add
 
    - Added a loop that obliges you to enter something to input.
    - Saves list after adding.

  - Delete
 
    - Added a loop that obliges you to enter something to input.
    - Saves list after deleting.

  - Show
 
    - It's not checking list's length now, It's checking "Is list have a item?".
    - Now shows list with enumerate() function of Python.
    - Saves list after showing.

  - Clean
 
    - It's not checking list's length now, It's checking "Is list have a item?".
    - Saves list after cleaning.

  - Sort
 
    - It's not checking list's length now, It's checking "Is list have a item?".
    - Saves list after sorting.
   
  - Exit
 
    - Saves list before exiting notification.

## List Manager v8.2

**_Features and Errors:_**

- Already Exists Error (New)

  - Notifies you about text given to input is already exists in the list.
 
  - Usage(s):
 
    - Add

- Empty Input Error (New) (**Note:** Older Empty Input Error is function "empty", but this new one is "EmptyInputError" and their usages are different)

  - Notifies you about text given to input of a command is empty.
 
  - Usage(s):
 
    - Add
    - Delete

- Item Is Not On List Error (New)

  - Notifies you about text given to input is not in list.
 
  - Usage(s):
 
    - Delete

- Functions

  - EmptyError (Edited)
 
    - New name of this function is "EmptyListError".

**_Maintainability:_**

- Code

  - Now the code has spaces between functions, variables, etc. for easy reading.

**_Bug Fixes:_**

- Save

  - It's saving list before showing it, removed it.

# New Versions

## List Manager v9

**_Maintainability:_**

- Code

  - Now the codes are grouped by their type. Also spaces are stayed.

**_Features:_**

- Check Wanting

  - It asks you if you are sure you want to do the action you are trying to do.
 
- Error Log

  - It writes errors to a file.
 
- Sort

  - Name is changed as "sort_list"("Sort" so).

- Autosave

  - Saves list automatically in specified functions.
 
  - Affects to:
 
    - Add
    - Delete
    - Clean
    - Sort

**_Errors:_**

- Functions

  - LoadingListError
 
    - Callable version of Loading List Error.
   
    - Usage(s):

      - Load
     
## List Manager v9.1

**_Modifications:_**

- Functions

  - Delete
 
    - First checks "Is list have a item?" now.

## List Manager v10

### Snapshot 1

**_Maintainability:_**

- Code Groups

    - Now code group names are upper.
 
        - Affects to:
     
            - "imported" with "IMPORTS"
            - "functions" with "FUNCTIONS"

    - New code groups:
 
        - ACTIONS
        - PROGRAM
        - RUNNING PROGRAM

    - Changed code group names:
 
        - "variables" with "VARIABLES AND LISTS"
        - "errors" with "ERRORS AND WARNINGS"

**_Bug Fixes:_**

- Functions

    - Clear
 
        - Before, it's tries to deleting a function named "clr" that doesn't exists when cannot clear the terminal screen. Now it's deleting the function "clear". (Itself.)

**_Features:_**

- Functions

    - Main
 
        - Finally the main "while True" loop is running inside of the "main" function.

    - Reset
 
        - Clears screen and reruns main function.

    - Help
 
        - Shows information about commands.

### Snapshot 2

**_Performance:_**

- Functions

    - Save
 
        - Added a unusual 'f' prefix before "list.pkl".

**_Features:_**

- Functions

    - Show Code
 
        - Prints the code of program. (It may can't print all of file.)

### Snapshot 3

**_Features:_**

- Variables

    - counter
 
        - It's using in save lists more than 1.

- Functions
    
    - Save Counter
 
        - Saves the "counter" variable to a file for load the latest list.

    - Load Counter
 
        - Loads the file that variable "counter" is saved to it.

    - Autosave Counter
 
        - Saves the "counter" variable automatically.
     
    - New List
 
        - Saves current list and creates a new list.

**_Modifications:_**

- Functions

    - Save
 
        - Now has a parameter named "list_name" to save file as that name. Default is "list".

    - Load
 
        - Now has a parameter named "list_name" to load file as that name. Default is "list".

    - empty
 
        - Deleted this function. Now it's using "EmptyInputError".
     
    - invalid
 
        - Deleted this function. Now it's using "InvalidInputError".

### Snapshot 4

**_Features:_**

- Functions

    - Export
 
        - Writes the contents of the list in the same order to a ".txt" file.
     
## List Manager v10.1

**_Features:_**

- Functions

    - About Version
 
        - Gives information about current version.

**_Errors:_**

- Loading List Error (Edited)
 
    - Message is changed from "Can't load list." to "An error occured while loading list!".

- No Lists Error (New)

    - Message is "No created lists!".
 
- Loading Counter Error (New)

    - Message is "An error occured while loading counter!".

- Clear Error (New/Moved)

    - Maked as function from function "clear".
 
    - Message is "Clearing the terminal screen is not supported on your system or cannot be found by the program.".

- Exiting Error (New)

    - Message is "An error occured while exiting program!".

- Saving List Error (New)

    - Message is "An error occured while saving list!".

- Saving Counter Error (New)

    - Message is ""An error occured while saving counter!".

- Autosaving Error (New)

    - Message is "An error occured while autosaving list!".

- Autosaving Counter Error (New)

    - Message is "An error occured while autosaving counter!".

- Exporting Error (New)

    - Message is "An error occured while exporting list!".

## List Manager v11

### Snapshot 1

**_Modifications:_**

- Functions

    - WantCheck
 
        - Renamed as "check"

**_Features:_**

- Functions

    - ProgramErrorLog
 
        - Logs program errors.

    - Error Control
 
        - Does error control and gives a error.
     
**_Errors:_**

- Resetting Error (New)

    - Message is "An error occured while resetting program!".

- Too Many Errors (New)

    - Message is "Too many errors!".
 
- Unknown Error (New)

    - Message is "An unknown error has occured!".

### Snapshot 2

**_Modifications:_**

- Class System

    - Now every function are in a class
 
        - Affects to:
     
            - functions
         
                - check
                - ProgramErrorLog
                - ErrorLog
                - save
                - load
                - save_counter
                - load_counter
                - autosave
                - autosave_counter

            - errors
         
                - EmptyListError
                - AlreadyExistsError
                - EmptyInputError
                - ItemIsNotOnListError
                - LoadingListError
                - InvalidInputError
                - NoListsError
                - LoadingCounterError
                - ClearError
                - ExitingError
                - SavingListError
                - SavingCounterError
                - AutosavingError
                - ExportingError
                - ResettingError
                - ShowingCodeError
                - TooManyErrors
                - CodeError
                - UnknownError

**_Maintainability:_**

- Functions

    - Main
 
        - First clearing and loading codes are sticked.

### Snapshot 3

- **_Modifications:_**

- Functions

    - Main
 
        - Added an undefined function when written "mode".

### Snapshot 4

**General**

**_Features:_**

- Variables

    - Added 2 variables named "mode" and "exited".

**_Modes:_**

- Debug Mode

    - This is the new and second mode of List Manager! This mode is not have some debug tools yet, but they will be added!
 
