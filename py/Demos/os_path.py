# Author        : Zhixin.Ji
# Date          : 2019-12-06
# Description   : 记录os的路径函数
import os
# __file__              当前模块路径路径
# sys.argv[0]           执行文件路径
# os.getcwd()           目录路径
# os.path.abspath('..') 上级目录
# os.path.abspath()     绝对路径
# os.path.split()       传入文件路径,输出目录和文件名; 传入目录,输出上级目录和文件夹名
# os.path.splitext      分离文件名和拓展名,文件后缀
# os.path.relpath(A, B) 获取相对路径 B->A
# os.listdir()          目录下所有文件
# os.path.exists()      文件/文件夹是否存在
# os.path.join()        连接路径

print(__file__)                     # F:/Learn/Python/py/Demos/os_path.py
print(os.getcwd())                  # F:\Learn\Python\py\Demos
print(os.path.abspath('..'))        # F:\Learn\Python\py
print(os.path.abspath('../bat'))    # F:\Learn\Python\py\bat
print(os.path.dirname(__file__))    # F:/Learn/Python/py/Demos
print(os.path.abspath(__file__))    # F:\Learn\Python\py\Demos\os_path.py
print(os.path.split(__file__))      # ('F:/Learn/Python/py/Demos', 'os_path.py')
print(os.path.split(os.getcwd()))   # ('F:\\Learn\\Python\\py', 'Demos')
