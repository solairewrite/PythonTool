# Python
用Python3做了一些便利的小工具  

## 命令
+ 查看python版本  
`py -3 -V`  
+ 运行python  
`py -3 fullpath.py`
+ .bat 运行 .py  
```
@echo off
cmd /k py -3 F:\Learn\Python\py\CheckConfig.py
```
+ 安装包,镜像  
py -3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple chardet
+ 更新pip  
py -3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

## import module
+ pycharm运行程序  
资源管理器中,项目根目录右键,Mark Directory as: Sources Root  
`from Work.Tools.Read_ini import ReadINI`  
+ cmd运行程序  
```
import sys
sys.path.append('F:\\Learn\\Python\\py')
from Work.Tools.Read_ini import ReadINI
```

## 创建.exe文件
+ 安装  
`py -3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller`  
+ 检测  
`pyinstaller --version`  
+ 创建.exe  
`pyinstaller -F F:\Learn\Python\py\Test.py`  
.exe文件在dist目录下  
建议cd进入文件夹执行命令,因为会产生其他文件,便于删除  
参数:
    + -F: 生成单个可执行文件  
    + -w: 程序运行时不显示cmd  
    + --distpath Dir: 指定exe路径,默认当前路径
    + -i Dir: icon,需要移动.exe文件位置才能看到
    + --hidden-import ModuleName: 导入包
+ 注意  
被 import 的 .py 导入的模块,需要 --hidden-import  
.exe警告记录在build/warn-XXX.txt  

## 概念
Python程序运行时,从模块顶层开始,逐行执行,不需要程序入口(main())  
+ `if __name__ == '__main__'`  
仅运行当前代码,不运行import的代码  
+ `__name__`  
内置变量,指当前模块  
如果是被执行的.py文件,值为`'__main__'`  
如果是被导入的模块,值为模块名  
+ `__main__`  
被执行的模块  
