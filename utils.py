import sys
from os import path

def get_main_module_path():
    return path.abspath(sys.modules['__main__'].__file__)

def is_database_exists(db_path):
    path.isfile(db_path)