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
av_type = "MISM"
start_num = 270
end_num = 300


# 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号
def open_av_links():
    all_numbers = get_all_folder_porn_number()

    for index, num in enumerate(range(start_num, end_num)):
        porn_number = '{}-{}'.format(av_type, num)
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
