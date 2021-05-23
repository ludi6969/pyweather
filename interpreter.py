import sys

def quit(db):
    db.close
    sys.exit(0)

def help():
    print('''q - quit
h - help ( show all available commands )
a - add measure
m - show all measures
m [x] - show last [x] measures
s - statistics''')

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

def show_measures(x):
    print('show x measures')

def statistics(db):
    print('statistics')

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

    else:
        print('Please type "h" to see all the avaliable commands :)')

if __name__ == '__main__':
    run()