import sys
import statistics
import common

def quit(db):
    db.close
    sys.exit(0)

def help():
    print('''q - quit
h - help ( show all available commands )
a - add measure
m - show all measures
s - statistics
e - export data to json''')

def add_measure(db):
    temp = input('type in the temperature: ')
    down = input('type in the downfall: ')
    db.insert(temp, down)
    print('the temperature and downfall was added to the database')


def show_all_measures(db):
    print()
    print('date                            temperature      downfall')
    print()
    records = db.get_all()
    for i in records:
        # print('date                            temperature      downfall')
        print('%s         %s               %s' % (i[1], i[2], i[3]))
    print()

def export_json(db):
    u = input('enter file path: ')
    sdata = common.jsonify(db.get_all())
    file = open(u, "w")
    file.write(sdata)
    file.close()
    print('data exported succesfully')

def stats(db):
    records = db.get_all()
    min = statistics.min(records)
    max = statistics.max(records)
    avg = statistics.average(records)
    print()
    print('                temperature         downfall')
    print()
    print('minimum         % 2.2f              % 3.2f' % (min[0], min[1]))
    print('maximum         % 2.2f              % 3.2f' % (max[0], max[1]))
    print('average         % 2.2f              % 3.2f' % (avg[0], avg[1]))
    print()
     


def run(db):
    c = input('command:')
    if c == 'q':
        quit(db)

    elif c == 'h':
        help()

    elif c == 'a':
        add_measure(db)

    elif c == 'm':
        show_all_measures(db)

    elif c == 'e':
        export_json(db)
    
    elif c == 's':
        stats(db)

    else:
        print('Please type "h" to see all the avaliable commands :)')

if __name__ == '__main__':
    run()