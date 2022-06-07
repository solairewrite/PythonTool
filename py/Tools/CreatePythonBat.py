# Author        : Zhixin.Ji
# Date          : 2019-12-06
# Description   : 创建.py的.bat执行文件
import os
from colorama import init, Fore

# --------------------运行前需要设置的变量--------------------
b_use_relative_path = True  # 是否使用相对路径
bat_path = 'F:\\Learn\\Python\\bat'  # 不使用相对路径时,bat目录
relative_path = '../../bat'  # bat文件夹相对于自身CreatePythonBat.py的路径

b_folder = False  # 是否为文件夹下的所有py文件创建bat
py_path = '/view_code/stat_BP.py'
py_folder = 'F:\\Learn\\Python\\py'


class CreatePythonBat:
    @staticmethod
    def create(b_relative_path, in_py_path, in_bat_folder):
        """为.py创建.bat,传入py的绝对路径,传入bat的绝对路径或相对路径"""
        if not os.path.exists(in_py_path):
            print(Fore.RED + in_py_path, ' 不存在')
            return

        t_bat_folder = in_bat_folder
        if b_relative_path:
            # 自身偏移relative_path的绝对路径
            t_bat_folder = os.path.abspath(relative_path)
        if not os.path.exists(t_bat_folder):
            print(Fore.RED + t_bat_folder, '不存在')
            return

        py_name = os.path.split(in_py_path)[1].replace('.py', '')
        t_bat_path = os.path.join(t_bat_folder, 'py_{}.bat'.format(py_name))

        with open(t_bat_path, 'w+', encoding='utf-8') as t_file:
            t_file.write('@echo off\n')
            t_py_folder = os.path.split(in_py_path)[0]
            if b_relative_path:
                bat_to_py = os.path.relpath(t_py_folder, t_bat_folder)
                t_file.write('cd {}\n'.format(bat_to_py))
            else:
                t_file.write('cd {}\n'.format(t_py_folder))
            # 单独一行 cmd /k 在某些电脑上,导致cmd彩色输出无效
            t_file.write('cmd /k py -3 {}\n'.format(os.path.split(in_py_path)[1]))

        des = '成功' if os.path.exists(t_bat_path) else '失败'
        print(Fore.GREEN + '{} 创建{}'.format(t_bat_path, des))

    @staticmethod
    def create_all(b_relative_path, in_py_folder, in_bat_folder):
        t_filename_list = os.listdir(in_py_folder)

        print('目录: ', in_py_folder)
        print('文件数量: ', len(t_filename_list))

        for t_filename in t_filename_list:
            if not t_filename.endswith('.py'):
                continue
            t_path = os.path.join(in_py_folder, t_filename)
            CreatePythonBat.create(b_relative_path, t_path, in_bat_folder)


if __name__ == '__main__':
    init(autoreset=True)

    _bat_path = relative_path if b_use_relative_path else bat_path
    if b_folder:
        CreatePythonBat.create_all(True, py_folder, _bat_path)
    else:
        CreatePythonBat.create(True, py_path, _bat_path)
