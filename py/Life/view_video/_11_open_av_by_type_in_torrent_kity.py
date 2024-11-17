# Author        : jizhixin
# Date          : 2024-02-17
# Description   : 搜索特性类型的AV番号,打开TorrentKitty网页,已下载的不再下载

import os
from colorama import init, Fore
from _00_porn_tool import get_all_folder_porn_number
import chardet
import webbrowser

torrent_kitty_url = 'https://www.torkitty.net/search/'

# 2024-02-17 只搜到MISM-306
# 3024-03-10 CMC-306
# 2024-03-16 DASD-999
av_type = "NEOB"
start_num = 30
count = 30
end_num = start_num + count


def get_numstr(num):
    if num >= 100:
        return str(num)
    if num >= 10:
        return '0' + str(num)
    return '00' + str(num)


# 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号
def open_av_links():
    all_numbers = get_all_folder_porn_number()

    for index, num in enumerate(range(start_num, end_num)):
        numstr = get_numstr(num)
        porn_number = '{}-{}'.format(av_type, numstr)
        # print(porn_number)
        if porn_number in all_numbers:
            print(Fore.RED + '{} 已下载: {}'.format(str(index).ljust(3), porn_number))
        else:
            search_url = torrent_kitty_url + porn_number + '/'
            # print(Fore.YELLOW + '{} {}'.format(str(index).ljust(3), search_url))
            webbrowser.open_new_tab(search_url)


if __name__ == '__main__':
    init(autoreset=True)
    open_av_links()
