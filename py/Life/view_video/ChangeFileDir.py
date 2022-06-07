# Author        : Zhixin.Ji
# Date          : 2020-03-22
# Description   : 修改文件目录,比如修改Porn文件的多层子级目录到根目录
import os
import shutil
import time
from colorama import Fore, Style
import re

# ----------运行前需要设置的变量----------
from_path = 'D:\\porn\\13'
to_path = 'D:\\porn\\13'
key_word = ''


class ChangeFileDir:
    @staticmethod
    def get_all_files(path, filelist):
        """获取文件夹及子文件夹下的所有文件"""
        if os.path.isfile(path):
            filelist.append(path)
        elif os.path.isdir(path):
            for item in os.listdir(path):
                sub_path = os.path.join(path, item)
                ChangeFileDir.get_all_files(sub_path, filelist)
        return filelist

    @staticmethod
    def print_list(str_arr, b_show_extension=False):
        """打印文件名列表,可以选择是否打印拓展名"""
        for t_str in str_arr:
            if os.path.isfile(t_str):
                t_str = os.path.split(t_str)[1]
            if b_show_extension:
                print(t_str)
            else:
                filename, extension = os.path.splitext(t_str)
                print(filename)

    @staticmethod
    def change_files_contain_str(instr, old_files, new_path):
        """传入旧文件路径列表,筛选字符串,新文件夹,移动所有包含筛选字符的文件"""
        change_num = 0
        for old_path in old_files:
            t_filename = os.path.split(old_path)[1]
            # if instr in t_filename:
            # 忽略大小写
            if re.search(instr, t_filename, re.IGNORECASE):
                b_change = ChangeFileDir.change_dir(old_path, new_path)
                if b_change:
                    change_num += 1
        print(Fore.CYAN, '移动了 {} 个文件'.format(change_num))
        print(Style.RESET_ALL)

    @staticmethod
    def change_dir(old_path, new_path):
        """修改文件目录,如果新文件夹已经存在相同文件,则删除当前文件"""
        # 如果文件夹new_path不存在,会导致数据丢失
        b_folder_exist = os.path.exists(new_path)
        if not b_folder_exist:
            os.makedirs(new_path)

        old_folder, filename = os.path.split(old_path)
        b_file_exist = os.path.exists(os.path.join(new_path, filename))
        if b_file_exist:
            b_same_folder = old_folder == new_path
            # 新文件夹(与旧文件夹非同一目录)存在相同文件,则删除旧文件夹的文件
            if not b_same_folder:
                print(Fore.RED, '删除{}'.format(old_path))
                print(Style.RESET_ALL)
                os.remove(old_path)
            return False

        print('移动{}'.format(old_path))
        shutil.move(old_path, new_path)
        return True


def change_porn_folder(filename_contain_str):
    start_time = time.time()

    all_files = list()
    ChangeFileDir.get_all_files(from_path, all_files)
    ChangeFileDir.change_files_contain_str(filename_contain_str, all_files, to_path)

    end_time = time.time()
    delta_time = end_time - start_time
    print(Fore.GREEN, '程序运行 {:.0f}ms'.format(delta_time * 1000))
    print(Style.RESET_ALL)


if __name__ == '__main__':
    change_porn_folder(key_word)
