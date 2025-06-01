# Author        : jizhixin
# Date          : 2025-05-25
# Description   : 将照片自动命名的难以阅读的名字,格式化为日期+时间

import os
from colorama import init, Fore

folder = 'D:\\UE照片\\Anim 03 MotionMatching'
# 是否进行重名
b_rename = 1
picture_types = ['.jpg']


def format_name(name: str) -> str:
    year = name[3:7]
    month = name[7:9]
    day = name[9:11]
    date = '{0}-{1}-{2}'.format(year, month, day)

    hour = name[11:13]
    minute = name[13:15]
    second = name[15:17]
    time = '{0}_{1}_{2}'.format(hour, minute, second)

    new_name = 'IMG {0} {1}'.format(date, time)
    return new_name


def main():
    for item in os.listdir(folder):
        finename, filetype = os.path.splitext(item)
        if filetype in picture_types:
            new_name = format_name(finename)
            old_path = os.path.join(folder, item)
            new_path = os.path.join(folder, new_name + filetype)
            print(old_path)
            print(Fore.YELLOW + new_path)
            if b_rename:
                os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    main()
