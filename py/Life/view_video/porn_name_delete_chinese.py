# Author        : jizhixin
# Date          : 2022-09-18
# Description   : 

import os
from colorama import init, Fore
from video_types import av_actress_names

folder = 'E:\\Porn\\24'


def read_folder(inpath):
    for item in os.listdir(inpath):
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            filename, end = os.path.splitext(item)
            has_chinese = False
            new_filename = ''
            for char in filename:
                if 0 <= ord(char) < 256:
                    new_filename += char
                else:
                    has_chinese = True
                    break
            if has_chinese:
                new_filename = new_filename.strip()
                new_path = folder + '\\' + new_filename + end
                print('   ' + sub_path)
                print(Fore.CYAN + '-> ' + new_path)
                os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
