# Author        : jizhixin
# Date          : 2025-06-06
# Description   : 一些备份代码,已经没用了,一般是one time thing,删了可惜

import os
from colorama import init, Fore
from py.Tools.git.git_uitls import get_staged_files


# 从git仓库中读取当前禁止优化的.build.cs文件列表
def get_disable_optimize_list_from_git_repo() -> list[str]:
    disable_optimize_list: list[str] = list()

    git_folder = 'G:\\UnrealEngine\\UE5.5\\UnrealEngine'
    staged_files = get_staged_files(git_folder)
    for index, file in enumerate(staged_files):
        if file.endswith('.Build.cs'):
            file_name_type = file.split('/')[-1]
            file_name = file_name_type.split('.')[0]
            # disable_optimize_list.append(file_name)
            disable_optimize_list.append(file)
            # print(Fore.CYAN + '{0} {1}'.format(str(index).ljust(3), file))
            # print(Fore.YELLOW + file_name)

    return disable_optimize_list


def main():
    disable_optimize_list = get_disable_optimize_list_from_git_repo()
    for index, file in enumerate(disable_optimize_list):
        print(Fore.CYAN + "'{}',".format(file))


if __name__ == '__main__':
    init(autoreset=True)
    main()
