# Author        : jizhixin
# Date          : 2022-08-03
# Description   : 打开1024链接
from enum import Enum
from Life.read_1024.read_1024 import Read1024, PornType


class LinkMode(Enum):
    """打开链接的模式"""
    OPEN_BY_TYPE = '按类型打开'
    OPEN_BY_INDEX = '按索引打开'
    OPEN_BY_STR = '按筛选字符打开'
    NOT_OPEN = '不打开'


# --------------------运行前需要设置的参数--------------------
# 网址,仅只支持1024
url = 'https://a227h.xyz/pw/thread.php?fid=3'
link_mode = LinkMode.OPEN_BY_TYPE  # 打开链接的模式
page_start = 1  # 打开第几页,从1开始
page_num = 5  # 打开多少页(按搜索字符)
open_types = [PornType.Japan, PornType.USA, PornType.Anim]  # 打开哪些类型
start_index = 50  # 打开链接的开始索引
open_link_num = 10  # 打开链接的数量
filter_str = '▲老含及▲欧美無码合集'  # 筛选字符串


def main():
    crawler = Read1024(url)

    if link_mode == LinkMode.OPEN_BY_INDEX:
        crawler.open_link_by_index(page_start, start_index, start_index + open_link_num)

    elif link_mode == LinkMode.OPEN_BY_STR:
        for i in range(page_start, page_start + page_num):
            global filter_str
            crawler.open_link_by_filter(i, open_link_num, filter_str, False)

    elif link_mode == LinkMode.NOT_OPEN:
        crawler.get_data_by_page(page_start, True)

    elif link_mode == LinkMode.OPEN_BY_TYPE:
        crawler.open_link_by_type(page_start, open_types)


if __name__ == '__main__':
    main()
