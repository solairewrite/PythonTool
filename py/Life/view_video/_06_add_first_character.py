# Author        : jizhixin
# Date          : 2023-09-27
# Description   : 女优文件夹名添加首字母

import os
from colorama import init, Fore
from xpinyin import Pinyin
from _00_porn_tool import porn_root_folder

b_only_see_no_modify = 0


def str_add_first_char(instr):
    p = Pinyin()
    pinyin = p.get_pinyin(instr, '')
    first_char = pinyin[0]
    first_char = str.upper(first_char)
    newstr = '_{0} {1}'.format(first_char, instr)
    print(newstr)
    return newstr


def all_folder_add_first_char(root_folder):
    sub_folders = os.listdir(root_folder)
    for i, sub_folder in enumerate(sub_folders):
        if not sub_folder.isdigit() \
                and not sub_folder.startswith('Anim') \
                and not sub_folder.startswith('USA') \
                and not sub_folder.startswith('SM'):
            new_folder = str_add_first_char(sub_folder)
            old_path = os.path.join(root_folder, sub_folder)
            new_path = os.path.join(root_folder, new_folder)
            print('{0} -> {1}'.format(old_path, new_path))
            if not b_only_see_no_modify:
                os.rename(old_path, new_path)


def str_format_old_name(instr):
    big_char = str.upper(instr[1])
    name = instr[2:]
    newstr = '_{0} {1}'.format(big_char, name)
    # print(newstr)
    return newstr


def all_folder_format_old_name(root_folder):
    sub_folders = os.listdir(root_folder)
    for i, sub_folder in enumerate(sub_folders):
        if sub_folder.startswith('_'):
            new_folder = str_format_old_name(sub_folder)
            old_path = os.path.join(root_folder, sub_folder)
            new_path = os.path.join(root_folder, new_folder)
            print('{0} -> {1}'.format(old_path, new_path))
            if not b_only_see_no_modify:
                os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    # all_folder_add_first_char(porn_root_folder)
    all_folder_format_old_name(porn_root_folder)
    # str_add_first_char('吉高宁宁')
    # str_format_old_name('_a爱弓凉')
