# Author        : jizhixin
# Date          : 2025-02-02
# Description   : 

import os
from colorama import init, Fore
from py.Tools.parse_code.source_str import source_code


def get_pin_category():
    lines = source_code.split('\n')[1:-1]
    for index, line in enumerate(lines):
        value = line.split('\"')[1]
        end = ((index + 1) % 5 == 0) and '\n' or ' '
        print(Fore.YELLOW + value, end=end)


def main():
    get_pin_category()


if __name__ == '__main__':
    init(autoreset=True)
    main()
