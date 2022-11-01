# Author        : jizhixin
# Date          : 2022-07-29
# Description   : 格式化文件夹内porn的文件名

import os
from colorama import init, Fore
from enum import Enum

# -------------------- 运行前设置的变量 -----------------------
path = 'E:\\porn\\28'
only_see_no_modify = 0
delete_starts = [
    'HD-', 'zzpp08.com@', 'avmans.com-', 'kpkp3.com_', 'kpkp56.com-',
    '8899xx.xyz_', '@蜂鳥@FENGNIAO-151.VIP-', 'avmans.com_', 'HD_',
    'hhd800.com@', 'zzpp01.com@', 'kckc-11.com@', 'freedl.org@',
    'kckc11.com@', 'rh2048.com@', 'kckc13.com@', 'kpkp69.com-',
    '[zzpp03.com]-', '@扶摇小飞鼠_', 'Woxav.Com@', 'zzpp06.com@',
    '[Xav-1.Xyz]', '[44x.me]', 'jav20s8.com@', '(無修正-流出) ',
    'bbsxv.xyz-', 'kckc14.com@', 'kpkp69.com_', 'javsubs91@',
    'kckc12.com@', 'kpkp3.com-', 'zzpp01.com_', '[Xavs1.Xyz]', 'JAVZIP.NET-',
    '[Xav-3.Xyz]', 'PP168.CC-', 'kckc16.com@', 'PP168.cc-', 'kckc17.com@',
]
delete_ends = [
    '_60fps_CH_HD', '_CH_HD', '_FHD_CH', '_CH_SD', '_C', '_Uncen', '_2K', '_ch',
    '-HD', '_', '.', '_HD_CH', '-FHD', '-C', 'c', '~nyap2p.com', 'ch',
    '_CH-nyap2p.com', '.SD', '(Uncensored Leaked)', '-uncensored-nyap2p.com',
    '-uncensored'
]

# -------------------- 缓存变量 -----------------------
files = list()
change_num = 0


class CharType(Enum):
    Null = 'None'
    Alpha = '字母'
    Digit = '数字'
    Line = '-'


# 读取所有文件
def read_folder():
    global files
    for item in os.listdir(path):
        sub_path = os.path.join(path, item)
        if os.path.isfile(sub_path):
            files.append(sub_path)


def delete_start_str(instr):
    for delstr in delete_starts:
        if instr.startswith(delstr):
            instr = instr.lstrip(delstr)
    return instr


def delete_end_str(instr):
    for delstr in delete_ends:
        if instr.endswith(delstr):
            instr = instr.rstrip(delstr)
    return instr


def get_formatted_name(old_name):
    # print(oldname)

    # 删除开头和末尾的字符
    old_name = delete_start_str(old_name)
    old_name = delete_end_str(old_name)

    chars = list(old_name)

    # 英文字母和数字之间加"-"
    last_type = CharType.Null
    for i in range(len(chars)):
        char = chars[i]

        if char == '-':
            break

        current_type = CharType.Null
        # print(i, char, end=' ')
        if char.isalpha():
            current_type = CharType.Alpha
        elif char.isdigit():
            current_type = CharType.Digit

        if current_type == CharType.Digit and last_type == CharType.Alpha:
            # print('need change', end=' ')
            chars.insert(i, '-')
            i += 1

        last_type = current_type
        # print(current_type.value)

    # 删除末尾的C
    num = len(chars)
    if num >= 2 and chars[num - 1] == 'C' and chars[num - 2].isdigit():
        del chars[num - 1]

    new_name = ''.join(chars)
    return new_name


def change_porn_names():
    for i, fullpath in enumerate(files):
        # if i != 1:
        #     continue
        if i <= -20:
            continue
        filename = os.path.split(fullpath)[1]
        # real_name: ABP-747, file_type: .mp4
        old_name, file_type = os.path.splitext(filename)
        new_name = get_formatted_name(old_name)
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
    change_porn_names()
    if not only_see_no_modify:
        print(Fore.YELLOW + '修改了 {} 个文件'.format(change_num))
