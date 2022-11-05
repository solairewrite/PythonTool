# Author        : jizhixin
# Date          : 2022-08-09
# Description   : 将动画的名字重命名为它所在的文件夹的名字
# E:\Porn\anim 01\HAC2145 虚假的寝取 02\HAC2145.MP4
# E:\Porn\anim 01\HAC2145 虚假的寝取 02.MP4

import os
from colorama import init, Fore
from porn_tool import video_types

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
folder = 'E:\\porn\\20'
b_only_print_no_change = 0


# 只读取一级子文件夹
def read_folder(infolder):
    for sub1_name in os.listdir(infolder):
        sub1_path = os.path.join(infolder, sub1_name)
        if os.path.isdir(sub1_path):
            for sub2_name in os.listdir(sub1_path):
                sub2_type = os.path.splitext(sub2_name)[1]
                if sub2_type in video_types:
                    sub2_path = os.path.join(sub1_path, sub2_name)
                    print(sub2_path)
                    new_path = sub1_path + sub2_type
                    print(Fore.CYAN + new_path)
                    if not b_only_print_no_change:
                        os.rename(sub2_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
