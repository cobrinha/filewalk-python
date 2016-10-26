# setup.py
from distutils.core import setup
import py2exe

target_abc = {
    "script": main.py",
    "icon_resources": [(1, "icon.ico")],
}