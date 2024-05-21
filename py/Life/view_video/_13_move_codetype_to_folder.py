# Author        : jizhixin
# Date          : 2023-05-20
# Description   : 将指定系列的番号移到一个文件夹下

import os
from colorama import init, Fore
from _00_porn_tool import porn_root_folder, get_all_folder_codetype_path

# 要处理的番号系列
codetype = 'CMC'
# 移到的新文件夹名前缀
prefix = '_0 '
ignore_folders = []
b_only_see_no_modify = 0


# 将同一个番号系列的片子移到一个文件夹下
def move_codetype_to_folder(incodetype):
    all_old_paths = get_all_folder_codetype_path(incodetype)

    old_paths = list()
    for item in all_old_paths:
        b_ignore = False
        for ignore_folder in ignore_folders:
            if ignore_folder in item:
                b_ignore = True
                break
        if not b_ignore:
            old_paths.append(item)

    target_folder = prefix + incodetype
    new_folder = os.path.join(porn_root_folder, target_folder)
    if not os.path.isdir(new_folder):
        if not b_only_see_no_modify:
            os.makedirs(new_folder)

    print(Fore.YELLOW + '番号数量: {0}'.format(len(old_paths)))
    for index, old_path in enumerate(old_paths):
        filename = os.path.split(old_path)[1]
        new_path = os.path.join(new_folder, filename)

        if new_path == old_path:
            continue

        count = index + 1
        print('{}{}'.format(str(count).ljust(5), old_path))
        print(Fore.CYAN + '{}{}'.format('->'.ljust(5), new_path))
        if count % 10 == 0:
            print()

        if not b_only_see_no_modify:
            os.rename(old_path, new_path)


def main():
    move_codetype_to_folder(codetype)


if __name__ == '__main__':
    init(autoreset=True)
    main()
