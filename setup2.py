import sys
from cx_Freeze import setup, Executable
exe = Executable(
    script=r"C:\Users\shubham singh\Desktop\AppDevelopment\Apple and Snake.py",
    base="Win32GUI",
    )

setup(
    name = "Apple and Snake",
    version = "0.1",
    options = {"build_exe":{"include_files":["head.png","apple.png","logo.png","match20.wav","medal1.jpg","medal2.jpg","medal3.jpg"]}},
    description = "My First Game",
    executables = [exe]
    )
