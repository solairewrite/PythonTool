# Author        : jizhixin
# Date          : 2022-07-29
# Description   : 将一个文件夹下的,所有子文件夹内的porn移动到根目录,忽略迅雷正在下载的视频

import os
from colorama import init, Fore
from porn_tool import is_video_fullpath, not_video_types

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
folder = 'E:\\porn\\35'
b_only_see_no_modify = 0
b_delete_none_video = 0

# -------------------- 缓存变量 -----------------------
# 根目录下的所有文件
files = list()
# 所有文件类型,[类型:文件数量]
file_types = dict()


def read_folder(infolder):
    if os.path.isfile(infolder):
        files.append(infolder)
    elif os.path.isdir(infolder):
        for item in os.listdir(infolder):
            sub_path = os.path.join(infolder, item)
            read_folder(sub_path)


def move_porn_to_root_folder():
    for fullpath in files:
        b_video = is_video_fullpath(fullpath)
        color = Fore.YELLOW if b_video else ''
        print(color + fullpath, end='')

        if b_video:
            filename = os.path.split(fullpath)[1]
            new_path = os.path.join(folder, filename)
            print()
            print(Fore.CYAN + new_path)
            if not b_only_see_no_modify:
                os.rename(fullpath, new_path)
        print()


def delete_none_video():
    for fullpath in files:
        file_folder, filename = os.path.split(fullpath)
        if file_folder == folder:
            for end in not_video_types:
                if filename.endswith(end):
                    print(Fore.RED + '删除: {}'.format(fullpath))
                    os.remove(fullpath)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
    move_porn_to_root_folder()
    if b_delete_none_video:
        delete_none_video()
