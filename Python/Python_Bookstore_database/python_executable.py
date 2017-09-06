import sys
from cx_Freeze import setup, Executable


setup(  name = "BookstoreFrontend",
        version = "0.1",
        description = "My GUI application!",
        executables = [Executable("BookstoreFrontend.py", base="Win32GUI")])