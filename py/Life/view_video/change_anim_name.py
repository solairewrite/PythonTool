# Author        : jizhixin
# Date          : 2022-08-09
# Description   : 修改动画文件夹内porn的文件名

import os
from colorama import init, Fore
from video_types import video_types

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
folder = 'E:\\porn\\anim 01'
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
