def __init__():
    pass

class EmLW(Warning):
    def __init__(self, message="List is empty! "):
        super().__init__(message)

class IEILW(Warning):
    def __init__(self, message="Item is exists in list! "):
        super().__init__(message)

class EIE(Exception):
    def __init__(self, message="Input is empty, write something! "):
        super().__init__(message)

class INILW(Warning):
    def __init__(self, message="Item is not in list! "):
        super().__init__(message)

class IIE(Exception):
    def __init__(self, message="Input is invalid, write something valid! "):
        super().__init__(message)

class NCLW(Warning):
    def __init__(self, message="You don't created and saved lists except current list! "):
        super().__init__(message)

class CSE(Exception):
    def __init__(self, message="Cannot clear your terminal! "):
        super().__init__(message)

class EPE(Exception):
    def __init__(self, message="An error occured while exiting program! "):
        super().__init__(message)

class ExLW(Warning):
    def __init__(self, message="An error occured while exporting list! "):
        super().__init__(message)

class RPE(Exception):
    def __init__(self, message="An error occured while resetting program! "):
        super().__init__(message)

class SCE(Exception):
    def __init__(self, message="An error occured while showing code! "):
        super().__init__(message)

class TME(Exception):
    def __init__(self, message="Too many errors occured! "):
        super().__init__(message)

class PE(Exception):
    def __init__(self, message="A program code error has occured. "):
        super().__init__(message)

class UE(Exception):
    def __init__(self, message="An unknown error has occured! "):
        super().__init__(message)