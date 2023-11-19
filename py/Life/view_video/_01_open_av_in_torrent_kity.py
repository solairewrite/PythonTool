# Author        : jizhixin
# Date          : 2022-11-05
# Description   : 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号,已下载的不再下载

import os
from colorama import init, Fore
from _00_porn_tool import get_porn_number, get_all_folder_porn_number, av_txt
import chardet
import webbrowser

# torrent_kitty_url = 'https://torrentkitty.tv/search/'
torrent_kitty_url = 'https://www.torkitty.net/search/'

start_line = 0  # AV.txt打开网页的起始行数
end_line = 30  # 包含行号为end_line的这一行


# 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号
def open_av_links(txt_path):
    all_numbers = get_all_folder_porn_number()
    with open(txt_path, 'rb') as tfile:
        tencoding = chardet.detect(tfile.read())['encoding']
    with open(txt_path, 'r', encoding=tencoding, errors='ignore') as tfile:
        for index, line in enumerate(tfile):
            if start_line <= index < end_line:
                # print(str(index) + ' ' + line, end='')
                line = line.strip()
                porn_number = get_porn_number(line)
                if porn_number:
                    if porn_number in all_numbers:
                        print(Fore.RED + '{} 已下载: {}'.format(str(index).ljust(3), porn_number))
                    else:
                        # print(porn_number)
                        search_url = torrent_kitty_url + porn_number + '/'
                        # print(Fore.YELLOW + '{} {}'.format(str(index).ljust(3), search_url))
                        webbrowser.open_new_tab(search_url)


if __name__ == '__main__':
    init(autoreset=True)
    open_av_links(av_txt)
