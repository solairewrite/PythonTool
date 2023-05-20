# Author        : jizhixin
# Date          : 2023-05-20
# Description   : 将同一个女优的片子移到一个文件夹下

import os
from colorama import init, Fore
from porn_tool import porn_root_folder, get_all_folder_actress_path

# 女优名字
actress_name = '凉森铃梦'
# 移动到哪个文件夹
target_folder = '66'
b_only_see_no_modify = 0


# 将同一个女优的片子移到一个文件夹下
def move_actress_to_folder():
    old_paths = get_all_folder_actress_path(actress_name)

    new_folder = os.path.join(porn_root_folder, target_folder)
    if not os.path.isdir(new_folder):
        os.makedirs(new_folder)

    print(Fore.YELLOW + '番号数量: {0}'.format(len(old_paths)))
    for index, old_path in enumerate(old_paths):
        filename = os.path.split(old_path)[1]
        new_path = os.path.join(new_folder, filename)

        count = index + 1
        print('{}{}'.format(str(count).ljust(5), old_path))
        print(Fore.CYAN + '{}{}'.format('->'.ljust(5), new_path))
        if count % 10 == 0:
            print()

        if not b_only_see_no_modify:
            os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    move_actress_to_folder()
