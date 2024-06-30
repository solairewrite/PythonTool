# Author        : jizhixin
# Date          : 2024-06-28
# Description   : 统计UE图片

import os
from colorama import init, Fore

root_folder = 'D:\\UE照片'
all_subfolder_name = '_全部照片'

all_imgs = list()
module_imgs = list()


# 获取全部照片
def get_all_images():
    all_subfolder = os.path.join(root_folder, all_subfolder_name)
    for item in os.listdir(all_subfolder):
        all_imgs.append(item)


# 获取各模块的照片
def get_module_images():
    for subfolder_name in os.listdir(root_folder):
        if subfolder_name == all_subfolder_name:
            continue

        subfolder = os.path.join(root_folder, subfolder_name)
        for item in os.listdir(subfolder):
            module_imgs.append(item)


# 打印未分配到模块中的图片
def print_info():
    # 全部照片文件夹 在 模块文件夹 中重复的
    for index, all_img in enumerate(all_imgs):
        b_inmodule = all_img in module_imgs
        color = Fore.CYAN if b_inmodule else Fore.YELLOW
        print(color + '{0} {1}'.format(str(index).ljust(3), all_img))

    print('{0}{1}{0}'.format('\n', "-" * 100))

    # # 模块文件夹 在 全部照片文件夹 中重复的
    # for index, module_img in enumerate(module_imgs):
    #     b_inall = module_img in all_imgs
    #     color = Fore.GREEN if b_inall else Fore.CYAN
    #     print(color + '{0} {1}'.format(str(index).ljust(3), module_img))


def main():
    get_all_images()
    get_module_images()
    print_info()


if __name__ == '__main__':
    init(autoreset=True)
    main()
