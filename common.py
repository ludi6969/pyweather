import utils
import sys
import json

def init(db_path):
     if (not utils.is_database_exists(db_path)):
         print('Database was not found. Do you want to create a new one?')
         a = input ('Yes/no: ')
         if (a == 'no'):
             sys.exit(1)
         else:
             print('Your database was created succesfuly!')
         

def jsonify(data):
    l = []
    for i in data:
        tmp = {
            'date': i[0],
            'temperature': i[1],
            'downfall': i[2]
        }
        l.append(tmp)
    return json.dumps(l)
        