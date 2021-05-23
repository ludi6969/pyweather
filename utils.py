import sys
from os import path
import datetime

def get_main_module_path():
    return path.dirname(sys.modules['__main__'].__file__)

def is_database_exists(db_path):
    return path.isfile(db_path)

def get_current_datetime():
    t = datetime.datetime.utcnow()
    return '%04d-%02d-%02d %02d:%02d:%02d UTC' % (t.year, t.month, t.day, t.hour, t.minute, t.second)

print(is_database_exists('./db.db'))