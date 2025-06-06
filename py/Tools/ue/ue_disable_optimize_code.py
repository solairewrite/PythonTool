# Author        : jizhixin
# Date          : 2025-06-06
# Description   : 修改引擎指定模块的.build.cs文件,禁止变量优化

import os
from colorama import init, Fore
from ue_config import disable_optimize_module_list
import chardet

# 是否修改引擎源码
b_modify = 1
engine_folder = 'G:\\UnrealEngine\\UE5.6\\UnrealEngine'


def disable_optimize_code(filepath: str):
    if not os.path.isfile(filepath) or not filepath.endswith('.Build.cs'):
        return

    print()
    print(Fore.CYAN + filepath)
    module_name = os.path.split(filepath)[1][:-len('.Build.cs')]
    # print(Fore.YELLOW + module_name)

    # 构造函数缩进层级
    tab = 1

    encoding = 'utf-8'
    with open(filepath, 'rb') as file:
        encoding = chardet.detect(file.read())['encoding']

    lines: list[str] = list()
    # 构造函数所在的行
    construct_line = -1
    # 已经有的优化代码行索引
    optimize_code_line = -1
    with open(filepath, 'r', encoding=encoding, errors='ignore') as file:
        for index, line in enumerate(file):
            # print('{0} {1}'.format(str(index).ljust(3), line), end='')
            lines.append(line)

            if optimize_code_line < 0 and 'OptimizeCode' in line:
                optimize_code_line = index

            if construct_line <= 0:
                if line.strip() == 'public {}(ReadOnlyTargetRules Target) : base(Target)'.format(module_name):
                    tabs = line.split('public')[0]
                    for tab_count in range(1, 10):
                        if tabs == '\t' * tab_count:
                            tab = tab_count
                            break
                    construct_line = index
                    # print(Fore.YELLOW + '{0} {1}'.format(str(index).ljust(3), line), end='')

    if construct_line <= 0:
        print(Fore.RED + '没找到构造函数')
        return

    # 添加禁止优化代码
    b_should_insert = optimize_code_line < 0 and construct_line > 0
    insert_line = -1
    if b_should_insert:
        insert_line = construct_line + 2
        lines[insert_line: insert_line] = [
            '{}OptimizeCode = CodeOptimization.InShippingBuildsOnly;\n'.format('\t' * (tab + 1)),
            '\n'
        ]

    for index, line in enumerate(lines):
        anchor_line = max(0, optimize_code_line, insert_line)
        if index > anchor_line + 2:
            break
        elif index < anchor_line - 4:
            continue

        color = ''
        if optimize_code_line < 0:
            if index == construct_line + 2:
                color = Fore.YELLOW
        else:
            if index == optimize_code_line:
                color = Fore.GREEN
        print(color + '{0} {1}'.format(str(index).ljust(3), line), end='')

    # 写入文件
    if b_should_insert and b_modify:
        with open(filepath, 'w+', encoding='utf-8') as file:
            file.writelines(lines)


def main():
    for index, item in enumerate(disable_optimize_module_list):
        filepath = engine_folder + '\\' + item.replace('/', '\\')
        disable_optimize_code(filepath)
        # break


if __name__ == '__main__':
    init(autoreset=True)
    main()
