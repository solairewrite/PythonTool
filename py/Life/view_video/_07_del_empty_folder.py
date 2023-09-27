# Author        : jizhixin
# Date          : 2023-07-23
# Description   : 

import os
from colorama import init, Fore
from _00_porn_tool import porn_root_folder


def del_empty_folder():
    for i in range(100):
        num = i + 1
        folder = os.path.join(porn_root_folder, str(num))
        if os.path.isdir(folder):
            porn_num = len(os.listdir(folder))
            bempty = porn_num <= 0
            color = bempty and Fore.MAGENTA or ''
            print(color + folder + ' ' + str(porn_num))
            if bempty:
                os.removedirs(folder)


def rename_numeric_folder():
    new_num = 0
    for i in range(100):
        num = i + 1
        folder = os.path.join(porn_root_folder, str(num))
        if os.path.isdir(folder):
            new_num += 1
            new_folder = os.path.join(porn_root_folder, str(new_num))
            print('{} -> {}'.format(folder, new_folder))
            os.rename(folder, new_folder)


if __name__ == '__main__':
    init(autoreset=True)
    del_empty_folder()
    # rename_numeric_folder()
