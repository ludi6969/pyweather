import sys
from os import path
import datetime

def get_main_module_path():
    return path.dirname(sys.modules['__main__'].__file__)

def is_database_exists(db_path):
    path.isfile(db_path)

def get_current_datetime():
    t = datetime.datetime.utcnow()
    return '%s-%s-%s %s:%s:%s UTC' % (t.year, t.month, t.day, t.hour, t.minute, t.second)