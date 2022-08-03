# Author        : Zhixin.Ji
# Date          : 2020-07-04
# Description   : 读取文件夹内的所有文件
# TODO: 处理不是视频的文件类型,忽略的文件夹排序
import os
from colorama import init, Fore
import random
from video_types import video_types

# -------------------- 运行前设置的变量 -----------------------
# 要读取的根目录
path = 'E:\\porn'
# 一个文件夹下最多有多少个文件
max_num = 30
# 忽略的文件夹
ignore_folders = ['marc dorcel 01', 'marc dorcel 02', 'SM 01', 'anim 01']

# -------------------- 全局变量 -----------------------
# 根目录下的所有文件
files = list()
# 所有文件类型,[类型:文件数量]
file_types = dict()
# [子文件夹:文件数量]
subs = dict()
# 重名文件[文件名:文件路径数组]
same_names = dict()


# 读取所有文件
def read_folder(inpath, inlist):
    if os.path.isfile(inpath):
        inlist.append(inpath)
    elif os.path.isdir(inpath):
        folder_name = os.path.split(inpath)[1]
        for ignore in ignore_folders:
            if folder_name == ignore:
                # print(Fore.MAGENTA + folder_name)
                return inlist

        for item in os.listdir(inpath):
            sub_path = os.path.join(inpath, item)
            read_folder(sub_path, inlist)
    return inlist


# 统计各种类型的文件数量
def stat_file_types():
    for item in files:
        filename = os.path.split(item)[1]
        end = os.path.splitext(filename)[1]
        if end not in file_types.keys():
            file_types[end] = 1
        else:
            file_types[end] += 1


# 统计子文件夹下的文件数量
def stat_sub_folder():
    for item in files:
        folder_path = os.path.split(item)[0]
        folder_name = os.path.split(folder_path)[1]
        if folder_name not in subs.keys():
            subs[folder_name] = 1
        else:
            subs[folder_name] += 1


# 打印重名文件
def print_same_name():
    if len(same_names.keys()) <= 0:
        return
    print(Fore.RED + '同名文件')
    for name in same_names.keys():
        for item in same_names[name]:
            print(item)
        print()


# 统计同名文件
def stat_same_name():
    # [文件名:文件路径]
    names = dict()
    # 记录同名文件
    for item in files:
        name = os.path.split(item)[1]
        if name not in names.keys():
            names[name] = item
        else:
            # 发现同名文件
            if name not in same_names.keys():
                same_names[name] = [names[name], item]
            else:
                same_names[name].append(item)
    # print_same_name()


# 将重名文件改名
def change_same_name():
    # print_same_name()
    if len(same_names.keys()) <= 0:
        print(Fore.YELLOW + '没有同名文件')
        return
    print(Fore.YELLOW + '更改同名文件')
    for name in same_names.keys():
        index = 0
        for item in same_names[name]:
            old = item
            folder = os.path.split(item)[0]
            filename = os.path.split(item)[1]
            start = os.path.splitext(filename)[0]
            end = os.path.splitext(filename)[1]
            new_name = '{}_{}{}'.format(start, index, end)
            new = os.path.join(folder, new_name)
            index += 1
            print('   ' + old)
            print('-> ' + new)
            # os.rename(old, new)
        print()


# 打印文件总数,文件类型,子文件夹
def print_files():
    # for item in files:
    #     print(item)
    print(Fore.YELLOW + '文件总数: {}'.format(len(files)))

    print(Fore.YELLOW + '统计文件类型')
    for item in file_types.keys():
        print(Fore.MAGENTA + '{} : {}'.format(item.ljust(5), file_types[item]))

    print(Fore.YELLOW + '统计子文件夹')
    print('  '.join(subs.keys()))
    # for item in subs.keys():
    #     print(Fore.MAGENTA + '{} : {}'.format(item.ljust(5), subs[item]))


# 将文件顺序打乱,随机放到文件夹中
def random_folder():
    print(Fore.YELLOW + '随机打乱文件路径,均匀分配到子文件夹中')
    folder_index = 0
    while len(files) > 0:
        folder_index += 1
        # print('-' * 20)
        for _ in range(max_num):
            # 随机[a,b]的整数
            rand = random.randint(0, len(files) - 1)
            old = files[rand]
            # 删除数组元素
            del files[rand]
            filename = os.path.split(old)[1]
            new_folder = os.path.join(path, str(folder_index))
            if not os.path.isdir(new_folder):
                os.makedirs(new_folder)
            new = os.path.join(new_folder, filename)
            # print('   ' + old)
            # print('-> ' + new)
            # print()
            os.rename(old, new)

            if len(files) <= 0:
                return


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(path, files)
    stat_file_types()
    stat_sub_folder()
    print_files()
    stat_same_name()
    print_same_name()
    # change_same_name()
    if len(same_names.keys()) <= 0:
        pass
        random_folder()
    print(Fore.YELLOW + '程序结束')
