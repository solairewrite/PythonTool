# Author        : Zhixin.Ji
# Date          : 2019-12-07
# Description   : 命令行参数解析
import argparse

bcmd = False
author = ''
luckey_number = 0

parser = argparse.ArgumentParser(description='命令行参数分析')
parser.add_argument(
    # 参数名,'-'/'--'前缀表示可选参数,默认变量名是'--'后面的字符串
    '-c', '--b_run_by_cmd',
    # 参数类型,int,float,str,bool等
    # type=bool,
    # 参数储存方式,默认为'store'
    # 'store_true'表示如果有这个参数,就储存为True,且type参数不能赋值
    action='store_true',
    default=False,
    dest='bcmd',  # 储存的参数名,默认'--'后面的字符串
    help='是否以命令行启动')
parser.add_argument('-a', '--author',
                    default='未知作者')
parser.add_argument('-l', '--luckey_number',
                    type=int)

# 命令行传参的方式
# -c
#   效果: args.bcmd=True, 仅适用于action='store_true'
# -a sola
#   效果: args.author=sola
# -l=2
#   效果: args.luckey_number=2

args = parser.parse_args()
print(args)

print('初始值')
print('bcmd: ', bcmd)
print('author: ', author)
print('luckey_number: ', luckey_number)

bcmd = args.bcmd
author = args.author
luckey_number = args.luckey_number
print('显式赋值后')
print('bcmd: ', bcmd)
print('author: ', author)
print('luckey_number: ', luckey_number)
