# Author        : jizhixin
# Date          : 2022-11-06
# Description   : 统计各种porn

import os
from colorama import init, Fore
from _00_porn_tool import av_actress_names, change_names, porn_root_folder


# 遍历文件夹中所有文件,每行打印5个文件名,并按照是否有女优名字区分颜色
def print_folder_has_actress(infolder):
    for i, item in enumerate(os.listdir(infolder)):
        filename = os.path.splitext(item)[0]
        strs = filename.split(' ')
        name_redirects = change_names.keys()

        # 文件名中是否已经有女忧名字
        if len(strs) >= 2:
            strs = strs[1:]
            b_has_actress_name = False
            for temp_str in strs:
                if temp_str in av_actress_names or temp_str in name_redirects:
                    b_has_actress_name = True
                    break

            end = ((i + 1) % 5 == 0) and '\n' or ',\t'
            color = b_has_actress_name and Fore.WHITE or Fore.MAGENTA
            print(color + ' '.join(strs), end=end)


# 打印重复的女优名字
def print_duplicate_names():
    # 不重复的名字
    names = list()
    # 重复的名字
    duplicate_names = list()

    for i, name in enumerate(av_actress_names):
        if name in names:
            duplicate_names.append(name)
        else:
            names.append(name)

    # 检查改名的女优
    diff_names = change_names.values()
    for name in diff_names:
        if name not in names:
            print(Fore.RED + '改名的女优需要放入av_actress_names: ' + name)

    print('重复的女优名字: ' + ' '.join(duplicate_names))


# 获取一个文件夹下的所有porn文件名(无后缀)数组
def get_porn_names_in_folder(infolder, bprint):
    file_names = list()
    if os.path.isdir(infolder):
        if bprint:
            print(Fore.YELLOW + '{0} {1}'.format(infolder, '-' * 30))
        for i, fullname in enumerate(os.listdir(infolder)):
            file_name = os.path.splitext(fullname)[0]
            file_names.append(file_name)
            if bprint:
                print('{} {}'.format(str(i + 1).ljust(3), file_name))
    return file_names


# 获取所有日本文件夹下的porn文件名,包括数字编号的文件夹和SM文件夹
def get_all_japanese_porns(bprint):
    file_names = list()

    big_num = 300

    # 从编号1开始的普通文件夹
    for i in range(1, big_num):
        sub_folder = os.path.join(porn_root_folder, str(i))
        if os.path.isdir(sub_folder):
            folder_names = get_porn_names_in_folder(sub_folder, False)
            file_names.extend(folder_names)

    # SM文件夹
    for i in range(1, big_num):
        sub_folder = os.path.join(porn_root_folder, 'SM')
        if i < 10:
            sub_folder += '0' + str(i)
        else:
            sub_folder += str(i)
        if os.path.isdir(sub_folder):
            folder_names = get_porn_names_in_folder(sub_folder, False)
            file_names.extend(folder_names)

    if bprint:
        for i, item in enumerate(file_names):
            print('{} {}'.format(str(i).ljust(5), item))

    return file_names


# 统计女优名字数量,也可以统计名字中的单个汉字
def stat_names(b_stat_names=True, b_stat_chars=False):
    print(Fore.YELLOW + 'av女优数量: {0}'.format(len(av_actress_names)))

    if b_stat_names:
        name_dict = dict()
        file_names = get_all_japanese_porns(False)
        for file_name_index, file_name in enumerate(file_names):
            for actress_name_index, actress_name in enumerate(av_actress_names):
                if actress_name in file_name:
                    if actress_name in name_dict.keys():
                        name_dict[actress_name] += 1
                    else:
                        name_dict[actress_name] = 1

        sorted_dict = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)

        index = -1
        for name, count in sorted_dict:
            index += 1
            end = (index + 1) % 10 == 0 and '\n' or '\t'
            # 打印名字出现次数
            print('{0} : {1}'.format(name, count).ljust(12), end=end)
            # if count >= 5:
            #     print('\'{0}\', '.format(name), end=end)

    if b_stat_chars:
        char_dict = dict()
        for name in av_actress_names:
            for char in name:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] += 1

        sorted_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

        for char, count in sorted_dict:
            # 打印汉字出现次数
            print('{0} : {1}'.format(char, count), end=', ')
            pass


# 打印有女优旧名字的文件名
def print_old_names():
    file_names = get_all_japanese_porns(False)
    old_name_filenames = list()
    for file_name_index, file_name in enumerate(file_names):
        for old_name_index, old_name in enumerate(change_names.keys()):
            if old_name in file_name:
                old_name_filenames.append(old_name)
    for item in old_name_filenames:
        print(item)


if __name__ == '__main__':
    init(autoreset=True)
    # for i in range(11, 29):
    #     sub_folder = os.path.join(porn_root_folder, str(i))
    #     if os.path.isdir(sub_folder):
    #         print(str(i) + '-' * 50)
    #         print_folder_has_actress(sub_folder)
    #         print()

    # print_duplicate_names()
    stat_names()
    # get_all_japanese_porns(True)
    # print_old_names()
