import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(
    name = "Autofocus",
    version = "0.1",
    description = "App of Autofocus System by Mark Forster",
    executables = [Executable("autofocus.py", base=base)]
)
