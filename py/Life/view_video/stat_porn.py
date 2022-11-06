# Author        : jizhixin
# Date          : 2022-11-06
# Description   : 统计各种porn

import os
from colorama import init, Fore
from porn_tool import av_actress_names, change_names

folder = 'E:\\Porn'


def read_folder(infolder):
    for i, item in enumerate(os.listdir(infolder)):
        filename = os.path.splitext(item)[0]
        strs = filename.split(' ')
        name_redirects = change_names.keys()

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


def unique_names():
    names = list()
    duplicate_names = list()

    for i, name in enumerate(av_actress_names):
        if name in names:
            duplicate_names.append(name)
        else:
            names.append(name)

    diff_names = change_names.values()
    for name in diff_names:
        if name not in names:
            print(Fore.RED + name)

    print(' '.join(duplicate_names))


# 获取一个文件夹下的所有porn文件名
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


# 获取所有日本文件夹下的porn文件名
def get_all_japanese_porns():
    file_names = list()

    # 从编号1开始的普通文件夹
    for i in range(1, 100):
        sub_folder = os.path.join('E:\\porn', str(i))
        folder_names = get_porn_names_in_folder(sub_folder, False)
        file_names.extend(folder_names)

    # SM文件夹
    for i in range(1, 30):
        sub_folder = 'E:\\porn\\SM '
        if i < 10:
            sub_folder += '0' + str(i)
        else:
            sub_folder += str(i)
        folder_names = get_porn_names_in_folder(sub_folder, False)
        file_names.extend(folder_names)

    # for i, item in enumerate(file_names):
    #     print('{} {}'.format(str(i).ljust(5), item))

    return file_names


# 统计女优名字数量
def stat_names(b_stat_names=True, b_stat_chars=False):
    print(Fore.YELLOW + 'av女优数量: {0}'.format(len(av_actress_names)))

    if b_stat_names:
        name_dict = dict()
        file_names = get_all_japanese_porns()
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


if __name__ == '__main__':
    init(autoreset=True)
    # for i in range(11, 29):
    #     sub_folder = os.path.join(folder, str(i))
    #     print(str(i) + '-' * 50)
    #     read_folder(sub_folder)
    #     print()

    # unique_names()
    stat_names()
    # get_all_japanese_porns()
