import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"


includes      = []
include_files = [r"C:\Users\floyd\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll", \
                 r"C:\Users\floyd\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll"]

setup(
    name = "Autofocus",
    version = "0.3",
    description = "App of Autofocus System. The system is designed by Mark Forster",
    options = {"build_exe": {"includes": includes, "include_files": include_files}},
    executables = [Executable("autofocus.py", base=base)]
)
