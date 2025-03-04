# Author        : jizhixin
# Date          : 2023-11-19
# Description   : 删除AV.txt中下载好的番号

import os
from colorama import init, Fore
import chardet
from py.Life.view_video._00_porn_tool import get_folder_porn_number, av_txt, porn_root_folder, get_porn_number, current_folder

downloaded_folder = current_folder


# 获取下载好的番号
def get_downloaded_porn_numbers():
    folder = os.path.join(porn_root_folder, downloaded_folder)
    porn_numbers = list()
    get_folder_porn_number(folder, porn_numbers)
    return porn_numbers


# 获取AV.txt中下载完成的番号
def delete_downloaded_porn_numbers():
    downloaded_numbers = get_downloaded_porn_numbers()
    infos = list()

    txt_path = av_txt
    with open(txt_path, 'rb') as tfile:
        tencoding = chardet.detect(tfile.read())['encoding']
    with open(txt_path, 'r', encoding=tencoding, errors='ignore') as tfile:
        for index, line in enumerate(tfile):
            line_num = index + 1
            old_line = line
            line = line.strip()
            porn_number = get_porn_number(line)
            if porn_number:
                if porn_number in downloaded_numbers:
                    print(Fore.YELLOW + '{} {} 已下载'.format(str(line_num).ljust(3), porn_number))
                else:
                    infos.append(old_line)
                    print('{} {}'.format(str(line_num).ljust(3), porn_number))
            else:
                infos.append(old_line)

    with open(txt_path, 'w+', encoding='utf-8') as file:
        for line in infos:
            file.write(line)


def main():
    delete_downloaded_porn_numbers()


if __name__ == '__main__':
    init(autoreset=True)
    main()
