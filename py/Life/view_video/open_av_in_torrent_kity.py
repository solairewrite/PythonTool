# Author        : jizhixin
# Date          : 2022-11-05
# Description   : 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号

import os
from colorama import init, Fore
from porn_tool import get_porn_number
import chardet
import webbrowser

av_txt = 'C:\\Users\\jizhixin\\Desktop\\AV.txt'
# https://torrentkitty.se/search/SHKD-997/
torrent_kitty_url = 'https://torrentkitty.se/search/'


# 打开包含番号的txt文件,打开TorrentKitty网页,搜索所有番号
def open_av_links(txt_path):
    with open(txt_path, 'rb') as tfile:
        tencoding = chardet.detect(tfile.read())['encoding']
    with open(txt_path, 'r', encoding=tencoding, errors='ignore') as tfile:
        for line in tfile:
            line = line.strip()
            porn_number = get_porn_number(line)
            if porn_number:
                # print(porn_number)
                search_url = torrent_kitty_url + porn_number + '/'
                webbrowser.open_new_tab(search_url)


if __name__ == '__main__':
    init(autoreset=True)
    open_av_links(av_txt)
