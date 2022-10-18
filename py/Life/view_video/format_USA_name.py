# Author        : jizhixin
# Date          : 2022-10-01
# Description   : 将欧美porn从文件夹移至根目录,对于文件夹内命名Scene 01的,命名为文件夹名+01

import os
from colorama import init, Fore
from video_types import video_types

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
folder = 'E:\\porn\\USA 08'
b_only_print_no_change = 0

delete_strs = [
    'Marc Dorcel -', 'Luxure -',
    '[Dorcel]', '[Marc Dorcel 2021]', '(2011).', '2010.', '(2010).', 'Luxure',
    '(Marc Dorcel)', 'WEB-DL', 'NEW 2021', '(Split Scenes)', '.480p', 'luxure-',
    '[Marc Dorcel]', 'lovexxx-', '(1080p)', 'Luxure -'
]


# inname是文件名,不包含文件类型
def format_usa_porn_name(inname):
    for del_str in delete_strs:
        inname = inname.replace(del_str, '')
        inname = inname.strip()
    inname = ' '.join(inname.split())
    return inname


def change_porn_path(oldpath, newpath):
    print(oldpath)
    print(Fore.CYAN + newpath)
    print()
    if not b_only_print_no_change:
        os.rename(oldpath, newpath)


# 只读取一级子文件夹
def read_folder(infolder):
    for sub1_name in os.listdir(infolder):
        sub1_path = os.path.join(infolder, sub1_name)
        if os.path.isdir(sub1_path):
            for sub2_name in os.listdir(sub1_path):
                sub2_left, sub2_type = os.path.splitext(sub2_name)
                # 一级子目录下的视频文件
                if sub2_type in video_types:
                    sub2_path = os.path.join(sub1_path, sub2_name)
                    new_left = sub2_left
                    if 'Split Scenes' in sub1_name or 'SPLIT SCENES' in sub1_name:
                        new_left = '{} {}'.format(sub1_name, sub2_left)
                    elif sub2_name.startswith('Scene'):
                        num_str = sub2_left.replace('Scene', '').strip()
                        new_left = '{} {}'.format(sub1_name, num_str)
                    new_left = format_usa_porn_name(new_left)
                    new_path = '{}\\{}{}'.format(infolder, new_left, sub2_type)
                    change_porn_path(sub2_path, new_path)

        elif os.path.isfile(sub1_path):
            sub1_left, sub1_type = os.path.splitext(sub1_name)
            new_left = format_usa_porn_name(sub1_left)
            if new_left != sub1_left:
                new_path = '{}\\{}{}'.format(infolder, new_left, sub1_type)
                change_porn_path(sub1_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
