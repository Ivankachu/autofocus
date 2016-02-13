import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(
    name = "Autofocus",
    version = "0.2",
    description = "App of Autofocus System. The system is designed by Mark Forster",
    executables = [Executable("autofocus.py", base=base)]
)
