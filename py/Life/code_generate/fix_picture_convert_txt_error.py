# Author        : jizhixin
# Date          : 2025-06-02
# Description   : 修复图片转txt的错误

import os
import chardet
from colorama import init, Fore

b_write_file = 1

txt_path = 'C:\\Users\\jizhixin\\Desktop\\temp2.txt'

redirects = {
    '	': '    ',  # tab to space

    '（': '(',
    '）': ')',
    '，': ',',
    '；': ';',
    '：': ':',
    '？': '?',
    '∥': '// ',

    'for(': 'for (',
    'if(': 'if (',
    'switch(': 'switch (',

    'lndex': 'Index',
    'ldx': 'Idx',
}

lines: list[str] = list()


def fix_error():
    with open(txt_path, 'rb') as tfile:
        encoding = chardet.detect(tfile.read())['encoding']

    with open(txt_path, 'r', encoding=encoding, errors='ignore') as file:
        for line_index, line in enumerate(file):
            old_line = line

            b_change = False
            for key_index, key in enumerate(redirects.keys()):
                value = redirects[key]
                if key in line:
                    line = line.replace(key, value)
                    if key != '	':
                        b_change = True

            lines.append(line)

            print(old_line, end='')
            if b_change:
                print(Fore.YELLOW + line, end='')

    if b_write_file:
        with open(txt_path, 'w+', encoding='utf-8') as file:
            for line in lines:
                file.write(line)


def main():
    fix_error()


if __name__ == '__main__':
    init(autoreset=True)
    main()
