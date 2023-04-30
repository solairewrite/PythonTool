# Author        : jizhixin
# Date          : 2022-11-02
# Description   : 从包含番号和av女忧名字的txt中,根据番号抓取av女忧的名字,并更新porn文件名

import os
from colorama import init, Fore
import chardet
import re
from zhconv import convert
from porn_tool import porn_pattern, porn_root_folder

# -------------------- 运行前设置的变量 -----------------------
path = folder = os.path.join(porn_root_folder, '51')
filepath_with_actress = 'C:\\Users\\jizhixin\\Desktop\\AV.txt'
only_see_no_modify = 0

# -------------------- 缓存变量 -----------------------
files = list()
actress_names = list()
change_num = 0


# 读取所有文件
def read_folder():
    global files
    for item in os.listdir(path):
        sub_path = os.path.join(path, item)
        if os.path.isfile(sub_path):
            files.append(sub_path)


# 读取包含av女忧名字的文件
def read_file_with_actress():
    with open(filepath_with_actress, 'rb') as tfile:
        tencoding = chardet.detect(tfile.read())['encoding']
    with open(filepath_with_actress, 'r', encoding=tencoding, errors='ignore') as tfile:
        line_index = -1
        for line in tfile:
            line_index += 1
            line = line.strip().strip('=').strip('-').strip('!')
            # if re.match(porn_pattern, line):
            #     if line_index < 15:
            #         line += ' {}'.format('纱纱原百合')
            #     else:
            #         line += ' {}'.format('麻里梨夏')
            # print(Fore.CYAN + '{0} {1}'.format(str(line_index).ljust(3), line))
            actress_names.append(line)


def get_name_with_av_actress(old_name):
    for actress in actress_names:
        old_name = old_name.upper()
        actress = actress.upper()
        if old_name in actress:
            her_name = actress.replace(old_name, '')
            # 繁体转简体
            her_name = convert(her_name, 'zh-cn')
            her_name = her_name.strip()
            return old_name + ' ' + her_name
    return old_name


def change_porn_names():
    for i, fullpath in enumerate(files):
        filename = os.path.split(fullpath)[1]
        # old_name: ABP-747, file_type: .mp4
        old_name, file_type = os.path.splitext(filename)
        new_name = get_name_with_av_actress(old_name)
        old_path = os.path.join(path, old_name) + file_type
        new_path = os.path.join(path, new_name) + file_type

        color = ''
        if old_name != new_name:
            global change_num
            change_num += 1
            color = Fore.YELLOW

        if only_see_no_modify:
            print('{}{}'.format(str(i).ljust(3), old_name))
            print(color + '-> {}'.format(new_name))
            print()
        else:
            print(color + '{} {} -> {}'.format(str(i).ljust(3), old_name.ljust(20), new_name))
            os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder()
    read_file_with_actress()
    change_porn_names()
    if not only_see_no_modify:
        print(Fore.YELLOW + '修改了 {} 个文件'.format(change_num))
