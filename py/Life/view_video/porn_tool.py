# Author        : jizhixin
# Date          : 2022-11-05
# Description   : 使用的porn工具

import os
from colorama import init, Fore
import re

test_folder = 'E:\\Porn\\2'
test_name = 'ABP-989 小女人'

video_types = ['.mp4', '.mkv', '.avi', '.MP4', '.mpg', '.wmv']
not_video_types = ['.torrent']

# 番号正则表达式
# porn_pattern = r'^[a-zA-z]{2,5}-[0-9]{3,4}(-[0-9])?' # 匹配最后表示上下集的-1
porn_pattern = r'^[a-zA-z]{2,5}-[0-9]{3,4}'


# 判断文件全名是否是视频
def is_video_fullname(fullname):
    file_type = '.' + fullname.split('.')[-1]
    if file_type in video_types:
        return True
    return False


# 判断文件全名是否是视频
def is_video_fullpath(fullpath):
    if os.path.isfile(fullpath):
        fullname = os.path.split(fullpath)[1]
        file_type = '.' + fullname.split('.')[-1]
        if file_type in video_types:
            return True
    return False


# 从文件名中(不包含文件类型后缀)获取AV番号
def get_porn_number(file_name):
    match_result = re.search(porn_pattern, file_name)
    if match_result:
        # 转大写
        porn_number = match_result[0].upper()
        return porn_number
    else:
        return None


# 获取文件夹内所有的番号
def get_folder_porn_number(path, inlist):
    for fullname in os.listdir(path):
        if is_video_fullname(fullname):
            file_name = os.path.splitext(fullname)[0]
            porn_number = get_porn_number(file_name)
            if porn_number:
                if porn_number not in inlist:
                    inlist.append(porn_number)
                    # print(Fore.YELLOW + '{} -> {}'.format(porn_number.ljust(10), file_name))
                else:
                    print(Fore.MAGENTA + '重复番号: {0}, 文件夹: {1}'.format(porn_number, path))
            else:
                print(Fore.RED + file_name)


# 获取porn文件夹下所有日本文件夹下的番号
def get_all_folder_porn_number():
    root_folder = 'E:\\Porn'
    all_porn_numbers = list()
    for i in range(1, 100):
        sub_folder = os.path.join(root_folder, str(i))
        if os.path.isdir(sub_folder):
            # print(str(i).ljust(3) + '-' * 30)
            get_folder_porn_number(sub_folder, all_porn_numbers)
    all_porn_numbers.sort()
    print(Fore.YELLOW + '番号数量: {0}'.format(len(all_porn_numbers)))
    return all_porn_numbers
    # for i, item in enumerate(all_porn_numbers):
    #     count = i + 1
    #     print('{} {}'.format(str(count).ljust(5), item))
    #     if count % 10 == 0:
    #         print()


if __name__ == '__main__':
    init(autoreset=True)
    get_all_folder_porn_number()
