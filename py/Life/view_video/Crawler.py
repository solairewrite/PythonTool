# Author        : Zhixin.Ji
# Date          : 2020-03-23
# Description   : 打开1024链接
from enum import Enum
from view_video.read1024 import Crawler


class LinkMode(Enum):
    """打开链接的模式"""
    OPEN_BY_INDEX = '按索引打开'
    OPEN_BY_STR = '按筛选字符打开'
    NOT_OPEN = '不打开'


# --------------------运行前需要设置的参数--------------------
# 网址,仅只支持1024
url = 'http://w11.a6def2ef910.rocks/pw/thread.php?fid=3'
link_mode = LinkMode.OPEN_BY_STR  # 打开链接的模式
page_start = 1  # 打开第几页,从1开始
page_num = 5  # 打开多少页(按搜索字符)
start_index = 50  # 打开链接的开始索引
open_link_num = 10  # 打开链接的数量
filter_str = '▲老含及▲欧美無码合集'  # 筛选字符串
# filter_str = '動漫'  # 筛选字符串
# filter_str = '動漫'  # 筛选字符串


def main():
    crawler = Crawler(url)

    if link_mode == LinkMode.OPEN_BY_INDEX:
        crawler.open_link_by_index(page_start, start_index, start_index + open_link_num - 1)

    elif link_mode == LinkMode.OPEN_BY_STR:
        for i in range(page_start, page_start + page_num):
            global filter_str
            crawler.open_link_by_filter(i, open_link_num, filter_str, False)

    else:
        crawler.get_data_by_page(page_start, True)


if __name__ == '__main__':
    main()
