import sys
from cx_Freeze import setup, Executable

# Execute this file to create an .exe for the project

build_exe_options = {"packages": ["os", "tkinter"],
                     "include_files":[
                         ("quotes", "quotes"),    # include the entire "quote" directory and its contents
                         ("resources", "resources"),    # include the entire "resources" directory and its contents
                         ("images", "images")
                     ],
                       "excludes": [],
                       
                       }
base= None

if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    "main.py",
    base= base,
    icon= "images/icon/cat.ico"
)

setup(
    name="Cat Pet App",
    version="2.0",
    options={"build_exe": build_exe_options},
    executables=[exe]
)