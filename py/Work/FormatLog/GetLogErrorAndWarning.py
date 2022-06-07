# Author        : jizhixin
# Date          : 2022-06-06
# Description   : 获取Log中的error,warning和自定义信息.写入新的log文件
import chardet
import re
from colorama import init, Fore
from string import digits

# --------------------运行前需要设置的变量--------------------

# 要读取的log路径
log_path = 'E:\\WorkRelease\\ProjectFR\\Saved\\Logs\\ProjectFR.log'
# 提取警告后,写入新log的文件夹
output_path = 'D:\\360安全浏览器下载'
# 自定义筛选信息,包含这些字符串的行会被保留下来
keywords = [
    'commandline',
]

# --------------------全局变量--------------------
all_line_list = list()  # 所有的log行
my_log_list = list()  # 自定义筛选的信息
error_line_list = list()  # 错误信息
warning_line_list = list()  # 警告信息
log_infos = list()  # 提取出的全部有用信息
no_duplicate_logs = list()  # 去重信息


# 读取log文件,存储全部的行
def read_log():
    print(Fore.YELLOW + '读取log...')
    with open(log_path, 'rb+') as temp_file:
        temp_data = temp_file.read()
        temp_encode = chardet.detect(temp_data).get('encoding')

    with open(log_path, 'r', encoding=temp_encode, errors='ignore') as temp_file:
        for line in temp_file:
            global all_line_list
            all_line_list.append(line)

    print(Fore.YELLOW + '读取完成,开始解析...')


# 获取包含自定义信息,warning,error信息的行
def get_warn():
    for line in all_line_list:
        global my_log_list
        for item in keywords:
            if item in line:
                my_log_list.append(line)
                break

        if 'error' in line or 'Error' in line:
            global error_line_list
            error_line_list.append(line)

        if 'warning' in line or 'Warning' in line:
            global warning_line_list
            warning_line_list.append(line)


# 获取全部有用的log信息
def get_log_infos():
    global log_infos
    log_infos.append('error line count: {}\n'.format(len(error_line_list)))
    log_infos.append('warning line count: {}\n'.format(len(warning_line_list)))

    log_infos.append('\n{0} 自定义信息 {0}\n'.format('-' * 30))
    for line in my_log_list:
        log_infos.append(line)

    log_infos.append('\n{0} 错误 {0}\n'.format('-' * 30))
    for line in error_line_list:
        log_infos.append(line)

    log_infos.append('\n{0} 警告 {0}\n'.format('-' * 30))
    for line in warning_line_list:
        log_infos.append(line)


# 写入仅包含警告信息的log文件
def write_log():
    tpath = output_path + '\\全部警告.log'
    with open(tpath, 'w+', encoding='utf-8') as temp_file:
        for line in log_infos:
            temp_file.write(line)
    print(Fore.GREEN + '新log写入: {}'.format(tpath))


# 从字符串中删除数字后,如果还一样的就是重复的log,过滤掉这些log
def set_no_duplicate_logs():
    temp_list = list()
    global no_duplicate_logs
    remove_number = str.maketrans('', '', digits)
    for line in log_infos:
        temp_no_number_line = line.translate(remove_number)
        if temp_no_number_line not in temp_list:
            temp_list.append(temp_no_number_line)
            no_duplicate_logs.append(line)


# 写入没有重复警告的log文件
def write_no_duplicate_log():
    tpath = output_path + '\\去重警告.log'
    with open(tpath, 'w+', encoding='utf-8') as temp_file:
        for line in no_duplicate_logs:
            temp_file.write(line)
    print(Fore.GREEN + '新log写入: {}'.format(tpath))


if __name__ == '__main__':
    init(autoreset=True)
    # 全部警告
    read_log()
    get_warn()
    get_log_infos()
    write_log()
    # 去重警告
    set_no_duplicate_logs()
    write_no_duplicate_log()
