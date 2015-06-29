import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "include_files":["find.ico", "Notepad++.ico"], "excludes": ["tkinter"]}
executables = [Executable("My Notepad.py")]
# GUI applications require a different base on Windows (the default is for a
# console application).
setup(  name = "My Notepad",
        description = "My first application!",
        options = {"build_exe": build_exe_options},
        executables = executables)
