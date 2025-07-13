# Author        : Zhixin.Ji
# Date          : 2020-07-01
# Description   : 统计代码行数
from colorama import init, Fore
import os
import chardet
import time

# ------------------------ 运行前设置的变量 ------------------------
path_list: list[str] = [
    # r'D:\UEProject\DreamParadise\Content\Script\Nagisa',
    # r'G:\UnrealEngine\UE5.6\UnrealEngine\Engine\Plugins\Chooser\Source\Chooser',
    r'G:\UnrealEngine\UE5.6\UnrealEngine\Engine\Plugins\Animation\BlendStack\Source\Runtime',
]

# 要统计的文件类型
filetypes = [
    '.h',
    '.cpp',
    '.py',
    '.cs',
    '.lua',
]
# 是否打印所有文件类型
b_print_all_file_types = True

# --------------------- 全局变量 --------------------------
all_file_types = list()


class CodeInfo:
    def __init__(self, inpath, in_line_count):
        if not os.path.isfile(inpath):
            return
        self.path = inpath
        self.name = os.path.split(inpath)[1]
        self.line_count = in_line_count

    def print_info(self, incolor=''):
        print(incolor + '{} {}'.format(str(self.line_count).ljust(7), self.name))


# 所有的统计信息,CodeInfo数组
code_infos = list()


# 判断一个文件是否是指定的文件类型
def is_correct_file_type(inpath):
    if not os.path.isfile(inpath):
        return False
    tfilename = os.path.split(inpath)[1]
    tend = os.path.splitext(tfilename)[1]
    if tend in filetypes:
        return True
    return False


# 递归获取文件夹下的所有文件
def get_all_files(inpath, outlist):
    # 文件
    if os.path.isfile(inpath):
        # 要统计的文件类型
        if is_correct_file_type(inpath):
            outlist.append(inpath)
        # 所有文件类型
        file_name = os.path.split(inpath)[1]
        file_type = os.path.splitext(file_name)[1]
        if file_type not in all_file_types:
            all_file_types.append(file_type)
    # 文件夹
    elif os.path.isdir(inpath):
        for item in os.listdir(inpath):
            tpath = os.path.join(inpath, item)
            get_all_files(tpath, outlist)
    return outlist


# 统计信息
def stat_code():
    for path in path_list:
        tfiles = get_all_files(path, list())
        for item in tfiles:
            with open(item, 'rb') as tfile:
                tencoding = chardet.detect(tfile.read())['encoding']
            with open(item, 'r', encoding=tencoding, errors='ignore') as tfile:
                linecount = 0
                for _ in tfile:
                    linecount += 1

            tinfo = CodeInfo(item, linecount)
            code_infos.append(tinfo)


# 排序函数
def sort_func(item):
    return item.line_count


# 按照行数排序
def sort_codes():
    code_infos.sort(key=sort_func, reverse=True)


# 打印统计信息
def print_stat_info():
    file_count = len(code_infos)
    line_count = 0
    range_dict = {
        '1000+': 0,  # 超过1000行代码的文件个数
        '500 ~ 1000': 0,
        '100 ~ 500': 0,
        '50 ~ 100': 0,
        '0 ~ 50': 0,
        '0': 0,
    }
    for index, item in enumerate(code_infos):
        # tcolor = ''
        # # 每隔10行换色打印
        # if int((index / 10) % 2) == 0:
        #     tcolor = Fore.MAGENTA
        if index % 10 == 0:
            print()
        print(str(index + 1).ljust(5), end='')
        item.print_info()
        count = item.line_count
        line_count += count
        if count >= 1000:
            range_dict['1000+'] += 1
        elif count >= 500:
            range_dict['500 ~ 1000'] += 1
        elif count >= 100:
            range_dict['100 ~ 500'] += 1
        elif count >= 50:
            range_dict['50 ~ 100'] += 1
        elif count > 0:
            range_dict['0 ~ 50'] += 1
        else:
            range_dict['0'] += 1

    print()
    print(Fore.YELLOW + '文件个数: {}, 代码总行数: {:,}'.format(file_count, line_count))
    if b_print_all_file_types:
        print(Fore.YELLOW + '所有文件类型: {}'.format(' '.join(all_file_types)))
    print(Fore.CYAN + '代码行数\t\t文件数量')
    for item in range_dict.keys():
        if range_dict[item] > 0:
            print(Fore.CYAN + '{} : {}'.format(item.ljust(10), range_dict[item]))


if __name__ == '__main__':
    init(autoreset=True)
    print(Fore.YELLOW + '开始统计...')
    start_time = time.time()

    stat_code()
    sort_codes()
    print_stat_info()

    end_time = time.time()
    program_run_time = end_time - start_time
    print()
    # 格式化输出,打印保留2位小数
    print(Fore.GREEN + '程序运行时间: {:.1f}s'.format(program_run_time))
