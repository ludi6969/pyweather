import sys


def quit():
    sys.quit(0)

def help():
    print('''q - quit
h - help ( show all available commands )
a - add measure
m - show all measures
m [x] - show last [x] measures
s - statistics''')

def add_measure():
    print('add measure')

def show_all_measures():
    print('show all measures')

def show_measures(x):
    print('show x measures')

def statistics():
    print('statistics')

def run():
    c = input('command:')
    if c == 'q':
        quit()

    elif c == 'h':
        help()

    elif c == 'a':
        add_measure()

    elif c == 'm':
        show_all_measures()

    else:
        print('Please type "h" to see all the avaliable commands :)')

if __name__ == '__main__':
    run()