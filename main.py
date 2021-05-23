import common
import utils
from interpreter import run
from database import Db
from os import path

database_file_name = 'database.db'

if __name__ == '__main__':
    database_path = path.join(utils.get_main_module_path(), database_file_name)
    common.init(database_path)
    db = Db(database_path)
    while True: 
        run(db)