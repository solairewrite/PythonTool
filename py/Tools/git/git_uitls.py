# Author        : jizhixin
# Date          : 2025-06-06
# Description   : git工具函数

import os
from colorama import init, Fore
from git import Repo

test_folder = 'G:\\UnrealEngine\\UE5.5\\UnrealEngine'


# 获取已暂存 & 没提交的文件
def get_staged_files(folder: str) -> list[str]:
    staged_files: list[str] = list()

    repo = Repo(folder)
    # repo.index: 暂存区
    # diff('HEAD'): 比较暂存区和当前最新提交(HEAD)之间的差异
    diffs = repo.index.diff('HEAD')
    for diff in diffs:
        staged_file = diff.a_path
        staged_files.append(staged_file)

    return staged_files


def main():
    staged_files = get_staged_files(test_folder)
    for index, file in enumerate(staged_files):
        print(Fore.CYAN + '{0} {1}'.format(str(index).ljust(3), file))


if __name__ == '__main__':
    init(autoreset=True)
    main()
