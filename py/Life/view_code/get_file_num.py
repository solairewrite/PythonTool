# Author        : Zhixin.Ji
# Date          : 2020-10-24
# Description   : 获取文件夹下有多少个文件
import os

# folder = 'F:\\Learn\\UE4Shop\\ActionRPG'
folder = 'F:\\Learn\\ActionRPG'
# folder = 'D:\\Game Design Learning\\UE4Shop\\ActionRPG'
# folder = 'E:\\Learn\\ActionRPG'
sub_folders = [
    'Config',
    'Content',
    'Source',
]
all_num = 0
tfile_num = 0


def get_file_num(path):
    if os.path.isfile(path):
        global tfile_num
        tfile_num += 1
    elif os.path.isdir(path):
        for item in os.listdir(path):
            sub_path = os.path.join(path, item)
            get_file_num(sub_path)


def main():
    for item in sub_folders:
        path = os.path.join(folder, item)
        global tfile_num
        tfile_num = 0
        get_file_num(path)
        print('{}: {}'.format(item.ljust(8), tfile_num))
        global all_num
        all_num += tfile_num
    print('总计: {}'.format(all_num))


main()
