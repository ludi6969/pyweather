import common
import utils
from interpreter import run

if __name__ == '__main__':
    common.init(utils.get_main_module_path())
    while True: 
        run()