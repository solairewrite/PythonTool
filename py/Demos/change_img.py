# Author        : Zhixin.Ji
# Date          : 2020-04-19
# Description   : 更改图片格式,尺寸,PIL需要安装pillow模块
from PIL import Image

path = 'D:\\0_Download\\游戏.png'
new_size = (192, 192)


# png转ico
def png_to_ico():
    img = Image.open(path)
    # .ico文件需要用用画图打开
    tpath = path.replace('.png', '.ico')
    img.save(tpath)


# png转jpg
def png_to_jpg():
    img = Image.open(path)
    png = Image.new('RGB', img.size, (255, 255, 255))
    png.paste(img, img)
    tpath = path.replace('.png', '.jpg')
    png.save(tpath)


# png修改尺寸
def png_new_size(size):
    img = Image.open(path)
    new_img = img.resize(size)
    tpath = path.replace('.png', '{}x{}.png'.format(size[0], size[1]))
    new_img.save(tpath)


if __name__ == '__main__':
    png_to_ico()
    png_to_jpg()
    png_new_size(new_size)
