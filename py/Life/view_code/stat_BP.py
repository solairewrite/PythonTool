# Author        : Zhixin.Ji
# Date          : 2020-10-23
# Description   : 统计UE4蓝图,打印层级结构,将原项目与自己的项目进行比对
import os
from colorama import init, Fore

# -------------配置变量-------------
# 原项目的Content路径
gas_doc_path = 'E:\\Learn\\GASDocumentation\\Content'
source_content = gas_doc_path
# 我的项目Content路径
my_gas_doc_path = 'E:\\Learn\\GASDoc\\Content'
my_content = my_gas_doc_path
bp_folders = ['GASDocumentation']
# 忽略列表
ignores = [

]
# 是否打印详细的文件列表
b_print_bp_list = True
# 是否只打印我未创建的文件
b_only_print_miss = False
# 写入log路径
log_path = 'C:\\Users\\Administrator\\Desktop\\未完成的蓝图.log'

# -------------全局变量-------------
# 原项目所有的BP列表
all_bps = []
# 子文件夹-BP列表字典
bp_dict = dict()
# 我的项目所有的BP列表
my_bps = []
# 我的项目,子文件夹-BP列表字典
my_dict = dict()
# 未创建的BP
todo_bps = []
# 写入log的信息
logs = []


# 统计Content中,所有需要统计的BP
def stat_bp(content_folder, inlist, indict):
    for item in bp_folders:
        sub_folder = os.path.join(content_folder, item)
        if os.path.isdir(sub_folder):
            bps = []
            get_folder_files(sub_folder, bps)
            for i, ele in enumerate(bps):
                bps[i] = ele.replace(content_folder + '\\', '').replace('.uasset', '')
            # 数组添加数组
            inlist.extend(bps)
            indict[item] = bps


# 获取文件夹内所有文件
def get_folder_files(path, filelist):
    if os.path.isfile(path):
        for item in ignores:
            if item in path:
                return
        filelist.append(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            sub_path = os.path.join(path, item)
            get_folder_files(sub_path, filelist)


# 获取未创建的列表
def get_todos():
    for item in all_bps:
        # if item not in my_bps:
        #     todo_bps.append(item)
        bfind = False
        for ele in my_bps:
            if item.lower() == ele.lower():
                bfind = True
                break
        if not bfind:
            todo_bps.append(item)

    tdiff_names = []

    for item in my_bps:
        # if item not in all_bps:
        #     tdiff_names.append(item)
        bfind = False
        for ele in all_bps:
            if item.lower() == ele.lower():
                bfind = True
                break
        if not bfind:
            tdiff_names.append(item)

    if len(tdiff_names) > 0:
        print_and_record(Fore.RED, 'BP文件名不一样: {} 个'.format(len(tdiff_names)))
        for item in tdiff_names:
            print_and_record(Fore.RED, item)
        print_and_record()


# 打印BP数量
def print_bp_num(inlist, indict, color):
    print_and_record(color, '总共 {} 个BP'.format(len(inlist)))
    for item in indict.keys():
        print_and_record(color, '{} : {}'.format(item.ljust(10), len(indict[item])))
    print_and_record()


# 打印文件层级列表
def print_files_level(files, is_source):
    # 文件层级
    last_dirs = []
    for item in files:
        # 判断我是否有创建文件,未创建的以红色显示
        color = ''
        if is_source and item not in my_bps:
            color = Fore.RED
        if b_only_print_miss and color == '':
            continue

        # 文件层级
        cur_dirs = item.split('\\')[0:-1]
        # 判断层级是否改变
        for i, tdir in enumerate(cur_dirs):
            if i > len(last_dirs) - 1:
                last_dirs.append(tdir)
                print_and_record('', '{}+{}'.format('\t' * i, tdir))
            if tdir != last_dirs[i]:
                last_dirs[i] = tdir
                print_and_record('', '{}+{}'.format('\t' * i, tdir))

        name = item.split('\\')[-1]
        if color == '':
            print(color + '\t' * len(cur_dirs) + name)
            pass
        else:
            print_and_record(color, '\t' * len(cur_dirs) + name)


def print_and_record(color='', instr=''):
    print(color + instr)
    logs.append(instr)


def write_log():
    # for line in logs:
    #     print(line)
    with open(log_path, 'w+', encoding='utf-8') as file:
        for line in logs:
            file.write(line + '\n')
    print()
    print(Fore.YELLOW + ' 统计结果保存到: ' + log_path)


if __name__ == '__main__':
    init(autoreset=True)

    stat_bp(source_content, all_bps, bp_dict)
    stat_bp(my_content, my_bps, my_dict)
    get_todos()

    print_and_record(Fore.YELLOW, '原项目')
    print_bp_num(all_bps, bp_dict, Fore.YELLOW)

    print_and_record(Fore.GREEN, '我的项目')
    print_bp_num(my_bps, my_dict, Fore.GREEN)

    print_and_record('', '未创建的BP: {} 个'.format(len(todo_bps)))

    if b_print_bp_list:
        print_files_level(all_bps, True)
    if b_only_print_miss:
        print_files_level(todo_bps, True)

    write_log()
