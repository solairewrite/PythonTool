# Author        : Zhixin.Ji
# Date          : 2020-05-11
# Description   : 修改目录下所有文件的编码
import os
from colorama import init, Fore
import chardet
from py.Tools.PrintPercent import PrintPercent

# ----------------------运行前需要设置的变量---------------------
# 文件夹
folder = 'E:\\Learn\\GASDoc'
# 要修改编码的文件类型
file_types = ['.cpp', '.h', '.c', '.cs', '.txt', '.md']
# file_types = ['.txt']
# 忽略文件夹
ignore_folders = ['.git', '.vs', 'x64', 'Debug']
# 是否仅显示文件编码,不进行转换
bOnlyShow = False
# 新的编码
new_encoding = 'utf-8'

# ----------------------全局(临时)变量---------------------------
# 所有文件列表
filelist = list()
# 所有文件后缀
all_file_types = list()


def get_files_in_folder(path):
    """获取文件夹及子文件夹下所有的文件"""
    for item in ignore_folders:
        if path.endswith(item):
            return
    if os.path.isfile(path):
        filelist.append(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            sub_path = os.path.join(path, item)
            get_files_in_folder(sub_path)


def get_all_files():
    """获取所有需要修改编码的文件"""
    if not os.path.exists(folder):
        raise NameError('文件夹不存在: {}'.format(folder))
    get_files_in_folder(folder)

    # 获取所有文件类型
    for item in filelist:
        filename = os.path.split(item)[1]
        file_type = os.path.splitext(filename)[1]
        if file_type not in all_file_types:
            all_file_types.append(file_type)


def show_encoding():
    i = 0
    for item in filelist:
        i += 1
        if i % 5 == 0:
            print()
        with open(item, 'rb') as file:
            encoding = chardet.detect(file.read())['encoding']
            print(Fore.WHITE + os.path.split(item)[1].ljust(40), end='')
            if encoding is None:
                encoding = 'None'
            print(Fore.CYAN + encoding)
    print(Fore.YELLOW + '所有文件类型:')
    print(Fore.YELLOW + ' '.join(all_file_types))
    print(Fore.CYAN + '文件数量: {}'.format(len(filelist)))


def change_encoding(filepath):
    with open(filepath, 'rb') as file:
        # 注意,file.read()只能进行一次,第二次是null
        data = file.read()
        old_encoding = chardet.detect(data)['encoding']
        if old_encoding == new_encoding:
            return

    if old_encoding is None:
        old_encoding = 'utf-8'
    decode_data = data.decode(old_encoding, errors='ignore')
    encode_data = decode_data.encode(new_encoding)

    temp_file = filepath + '_new'
    with open(temp_file, 'wb+') as file:
        file.write(encode_data)

    os.remove(filepath)
    os.rename(temp_file, filepath)


def change_all_encodings():
    items_to_change = list()
    for item in filelist:
        for file_type in file_types:
            if item.endswith(file_type):
                items_to_change.append(item)
                break

    print(Fore.YELLOW + '需要修改的文件数量: {}'.format(len(items_to_change)))
    i = 0
    for item in items_to_change:
        i += 1
        PrintPercent.print(i * 1.0 / len(items_to_change))
        change_encoding(item)
    print('修改编码完成')


if __name__ == '__main__':
    init()
    get_all_files()
    if bOnlyShow:
        show_encoding()
    else:
        change_all_encodings()
