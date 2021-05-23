import utils
import sys

def init(db_path):
     if (not utils.is_database_exists(db_path)):
         print('Database was not found. Do you want to create a new one?')
         a = input ('Yes/no: ')
         if (a == 'no' or a == 'n'):
             sys.exit(1)
         else:
             print('Your database was created succesfuly!')
         

