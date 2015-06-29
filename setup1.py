import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script=r"C:\Users\shubham singh\Desktop\AppDevelopment\My Notepad.py",
    base="Win32GUI",
    )

setup(
    name = "My Notepad",
    version = "0.1",
    options = {"build_exe":{"include_files":["find.ico","Notepad++.ico","help.gif","help.ico"]}},
    description = "My First Application",
    executables = [exe]
    )
