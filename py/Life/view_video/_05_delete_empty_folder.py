# Author        : jizhixin
# Date          : 2023-05-07
# Description   : 删除下载后,视频已经移除文件夹的空文件夹

import os
from colorama import init, Fore
from porn_tool import porn_root_folder, get_folder_porn_number
import shutil

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
folder = os.path.join(porn_root_folder, '65')
b_only_see_no_modify = 0
# 小于此大小MB的文件夹才会被删除
max_folder_size = 3

# -------------------- 缓存变量 -----------------------
porn_numbers = list()


# 获取番号中的数字
def get_num_in_code(code: str) -> str:
    return code.split('-')[1]


# 获取文件夹内所有的番号数字
def get_nums_in_folder() -> list[str]:
    nums = list()
    get_folder_porn_number(folder, porn_numbers)
    for index, item in enumerate(porn_numbers):
        num = get_num_in_code(item)
        # print('{0}{1}{2}'.format(str(index).ljust(3), num.ljust(4), item))
        nums.append(num)
    return nums


# 获取文件夹大小MB
def get_folder_size(infolder):
    size = 0
    for parent_folder, sub_folders, files in os.walk(infolder):
        for file in files:
            fullname = os.path.join(parent_folder, file)
            file_size = os.path.getsize(fullname) / 1024 / 1024
            size += file_size
    return size


# 获取所有包含番号数字的文件夹,和移除了视频的文件夹
def get_folders_contain_num():
    nums = get_nums_in_folder()
    sub_folders = list()
    folders_video_out = list()
    for sub_folder in os.listdir(folder):
        index = -1
        if os.path.isdir(os.path.join(folder, sub_folder)):
            index += 1
            video_out = False
            folder_num = '-1'
            for num in nums:
                if num in sub_folder:
                    video_out = True
                    folder_num = num
                    sub_folders.append(sub_folder)
                    break
            color = video_out and Fore.YELLOW or Fore.CYAN
            size = get_folder_size(os.path.join(folder, sub_folder))
            intsize = int(size)
            # print(color + '{0}{1}{2}{3}'.format(
            #     str(index).ljust(3), folder_num.ljust(4), (str(intsize) + 'MB').ljust(7), sub_folder))
            if video_out and size < max_folder_size:
                folders_video_out.append(sub_folder)
    return sub_folders, folders_video_out


# 删除移除视频的文件夹
def del_folders_video_out():
    sub_folders, folders_video_out = get_folders_contain_num()
    for index, sub_folder in enumerate(folders_video_out):
        remove_path = os.path.join(folder, sub_folder)
        print(Fore.YELLOW + '{0}{1}'.format(str(index).ljust(3), remove_path))
        if not b_only_see_no_modify:
            shutil.rmtree(remove_path)


if __name__ == '__main__':
    init(autoreset=True)
    # get_folder_porn_number(folder, porn_numbers)
    # for index, item in enumerate(porn_numbers):
    #     print('{0}{1}'.format(str(index).ljust(3), item))
    # sub_folders, folders_video_out = get_folders_contain_num()
    del_folders_video_out()
