# Author        : jizhixin
# Date          : 2023-03-25
# Description   : 

import os
from colorama import init, Fore

folder = 'E:\\movie\\生活大爆炸 第九季'

bModify = 1


def read_folder(inpath):
    for index, item in enumerate(os.listdir(inpath)):
        # if '生活大爆炸' not in item:
        #     continue
        # if index >= 16:
        #     continue
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            color = ''
            filename, end = os.path.splitext(item)
            num = index + 0
            episode = num + 1 < 10 and '0' + str(num + 1) or str(num + 1)
            filename = '生活大爆炸 S09 E{0}'.format(episode)
            new_path = folder + '\\' + filename + end
            print(color + '{} {} -> {}'.format(str(index).ljust(3), sub_path.ljust(30), new_path))
            if bModify:
                os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
