# Author        : jizhixin
# Date          : 2025-03-04
# Description   : 将下载好的文件:
# 1.移到根目录
# 2.规范化番号名
# 3.获取女优名
# 4.删除下载好的番号
# 5.删除空文件夹

from colorama import init
from _02_move_porn_to_root_folder import main as move_porn_to_root_folder
from _03_format_porn_name import main as format_porn_name
from _05_delete_empty_folder import main as delete_empty_folder
from _09_grab_av_actress_name import main as grab_av_actress_name
from _10_delete_downloaded_porn_number import main as delete_downloaded_porn_number


def main():
    move_porn_to_root_folder()
    format_porn_name()
    grab_av_actress_name()
    delete_downloaded_porn_number()
    delete_empty_folder()


if __name__ == '__main__':
    init(autoreset=True)
    main()
