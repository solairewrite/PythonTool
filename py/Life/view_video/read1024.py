# Author        : Zhixin.Ji
# Date          : 2020-04-20
# Description   : 爬取1024合集
import requests
from bs4 import BeautifulSoup  # 解析html
import re
import webbrowser
from colorama import init, Fore


class Resource:
    def __init__(self, text, link):
        self.text = text
        self.link = link

    def print_info(self):
        title = self.text
        delstr = ['★', '√', '㊣', '♀', '[', ']', '▲', '☆', '♂',
                  '◆', '◇', '↗', '↘', '【', '】', '▼', '△']
        for item in delstr:
            title = title.replace(item, '')
        print('{}\t{}'.format(title, self.link))


class Crawler:
    def __init__(self, in_url):
        init(autoreset=True)
        self.url = in_url
        self.resource_arr = list()

    def get_data_by_page(self, in_page=1, b_print_detail=False):
        """获取指定页的标题和链接"""
        self.resource_arr = list()
        turl = self.url
        if in_page >= 1:
            turl = '{}&page={}'.format(self.url, in_page)
        print(Fore.YELLOW + '获取: ' + turl)

        response = requests.get(turl)
        if not response.status_code == 200:
            return None
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')
        line_base = soup.find('base', id='headbase')
        link_prefix = line_base['href']

        line_arr = soup.find_all('a',
                                 href=re.compile('^html_data/'),
                                 text=re.compile(r'^\[[0-9][0-9]\.[0-9][0-9]].*(合集|專輯|大杂烩)'))
        for line in line_arr:
            t_resource = Resource(line.get_text(), link_prefix + line.attrs['href'])
            self.resource_arr.append(t_resource)

        self.stat(b_print_detail)

    def stat(self, b_print_detail=False):
        """统计资源并打印"""
        chinese_num = 0
        japanese_num = 0
        western_num = 0
        anim_num = 0
        for i, item in enumerate(self.resource_arr):
            if b_print_detail:
                if i % 10 == 0:
                    print(Fore.CYAN, '-' * 70)
                print('{}: '.format(i), end='')
                item.print_info()

            if '國' in item.text or '国' in item.text:
                chinese_num += 1
            elif '美' in item.text:
                western_num += 1
            elif '動' in item.text or '动' in item.text:
                anim_num += 1
            else:
                japanese_num += 1

        print(Fore.YELLOW, '资源总数:{}, 国产:{}, 日本:{}, 欧美:{}, 动画:{}'
              .format(len(self.resource_arr), chinese_num, japanese_num, western_num, anim_num))

    def open_link_by_filter(self, in_page, in_open_num, in_filter=''):
        """打开指定页面的链接,传入筛选字符串"""
        self.get_data_by_page(in_page)
        t_open_num = min(in_open_num, len(self.resource_arr))
        t_num = 0
        for item in self.resource_arr:
            if in_filter == '动' and ('动' in item.text or '動' in item.text):
                webbrowser.open_new_tab(item.link)
                t_num += 1

            elif in_filter in item.text:
                webbrowser.open_new_tab(item.link)
                t_num += 1

            if t_num >= t_open_num:
                return

    def open_link_by_index(self, in_page, in_start_index, in_end_index):
        """打开指定页面的链接,传入开始和结束索引"""
        self.get_data_by_page(in_page)
        for i, item in enumerate(self.resource_arr):
            if in_start_index <= i < in_end_index:
                webbrowser.open_new_tab(item.link)
