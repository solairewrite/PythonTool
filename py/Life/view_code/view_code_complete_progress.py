# Author        : Zhixin.Ji
# Date          : 2020-07-19
# Description   : 检查代码完成进度,对比源项目和自己的项目
import os
from enum import Enum
from colorama import init, Fore

# ------------------ 运行前需要设置的变量 -------------------
source_path = 'D:\\Game Design Learning\\UE4Shop\\ActionRPG\\Source'
my_path = 'E:\\Learn\\ActionRPG\\Source'
filetypes = ['.h', '.cpp', '.cs']


# ------------------- 全局变量 ----------------------
# 代码文件完成状态
class CodeState(Enum):
    Not_Created = '未创建'
    Doing = '已创建,正在写'
    Finish = '完成'


# 所有代码文件的完成状态字典
code_state_dict = dict()
# 未创建的代码文件
not_created_codes = list()
# 正在编写的代码文件
doing_codes = list()
# 完成的代码文件
finish_codes = list()


# 递归获取文件夹下的所有文件
def get_all_files(inpath, outlist):
    # 文件
    if os.path.isfile(inpath):
        # 要统计的文件类型
        if is_correct_file_type(inpath):
            # 类名太长,替换
            # RPGAbilityTask_PlayMontageAndWaitForEvent
            inpath = inpath.replace('AndWaitForEvent', '')
            outlist.append(inpath)
    # 文件夹
    elif os.path.isdir(inpath):
        for item in os.listdir(inpath):
            tpath = os.path.join(inpath, item)
            get_all_files(tpath, outlist)
    return outlist


# 判断一个文件是否是指定的文件类型
def is_correct_file_type(inpath):
    if not os.path.isfile(inpath):
        return False
    tfilename = os.path.split(inpath)[1]
    tend = os.path.splitext(tfilename)[1]
    if tend in filetypes:
        return True
    return False


# 比较我的代码和源代码,设置完成进度code_state_dict
def get_code_propress():
    # 源代码
    source_files = get_all_files(source_path, list())
    for item in source_files:
        key = os.path.split(item)[1]
        code_state_dict[key] = CodeState.Not_Created

    # 我的代码
    my_files = get_all_files(my_path, list())
    for item in my_files:
        key = os.path.split(item)[1]
        if key in code_state_dict.keys():
            with open(item, 'r', encoding='utf-8', errors='ignore') as file:
                line = file.readline()
                if '// 完成' in line:
                    code_state_dict[key] = CodeState.Finish
                else:
                    code_state_dict[key] = CodeState.Doing

    # 设置代码状态数组
    for item in code_state_dict.keys():
        file_state = code_state_dict[item]
        if file_state == CodeState.Not_Created:
            not_created_codes.append(item)
        elif file_state == CodeState.Doing:
            doing_codes.append(item)
        elif file_state == CodeState.Finish:
            finish_codes.append(item)


def print_list(arr, color, title):
    print()
    print(color + '{0} {1}: {2} 个 {0}'.format('-' * 20, title, len(arr)))
    arr.sort()
    for item in arr:
        print(color + item)


def print_info():
    print_list(not_created_codes, Fore.RED, '未创建的代码')
    print_list(doing_codes, Fore.WHITE, '正在编写的代码')
    print_list(finish_codes, Fore.GREEN, '完成的代码')

    print()
    all_num = len(code_state_dict.keys())
    not_created_num = len(not_created_codes)
    doing_num = len(doing_codes)
    finish_num = len(finish_codes)
    print(Fore.YELLOW + '总共 {} 个文件'.format(all_num))
    # 打印百分数
    print(Fore.YELLOW + '未创建的 {} 个, {:.0%}'
          .format(not_created_num, not_created_num / all_num))
    print(Fore.YELLOW + '正在写的 {} 个, {:.0%}'
          .format(doing_num, doing_num / all_num))
    print(Fore.YELLOW + '已完成的 {} 个, {:.0%}'
          .format(finish_num, finish_num / all_num))


if __name__ == '__main__':
    init()
    get_code_propress()
    print_info()
