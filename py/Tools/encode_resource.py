# Author        : Zhixin.Ji
# Date          : 2020-04-19
# Description   : 将资源文件编码成字符串,存于.py文件的变量中
# 避免pyinstaller打包时,只打包.py文件不打包图片
# base64是一种编码方式,将二进制数据编码为字符串
import base64
import os

# pyinstaller打包的.py文件的路径
py = '../Life/open_1024.py'
# py = '../Test.py'
# 资源路径
resource = '../../Resource/girl.ico'

"""
使用示例
from girl import girl

with open('icon.ico', 'wb+') as file:
    # 将字符串解码为二进制数据
    file.write(base64.b64decode(girl))
window.iconbitmap('icon.ico')
os.remove('icon.ico')
"""


def encode():
    resource_abspath = os.path.abspath(resource)
    with open(resource_abspath, 'rb') as file:
        resource_filename = os.path.split(resource_abspath)[1]
        varname = os.path.splitext(resource_filename)[0]
        # 将二进制数据编码为字符串
        b64str = base64.b64encode(file.read())
        datastr = '{} = {}'.format(varname, b64str)
        databyte = datastr.encode()

    py_abspath = os.path.abspath(py)
    folder = os.path.split(py_abspath)[0]
    py_filename = os.path.join(folder, varname + '.py')
    with open(py_filename, 'wb+') as file:
        file.write(databyte)


if __name__ == '__main__':
    encode()
