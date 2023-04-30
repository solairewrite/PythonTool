# Author        : jizhixin
# Date          : 2022-08-03
# Description   : 爬取1024合集
import requests
from bs4 import BeautifulSoup  # 解析html
import re
import webbrowser
from colorama import init, Fore
from enum import Enum


class PornType(Enum):
    China = "国产"
    Japan = "日本"
    USA = "欧美"
    Anim = "动画"
    Picture = "写真"
    Sanji = "三级"


class Resource:
    def __init__(self, text, link):
        self.text = text
        self.link = link
        self.type = self.get_porn_type(self.text)

    @staticmethod
    def get_porn_type(text):
        if ('國' in text or '国' in text) and '島國' not in text:
            return PornType.China
        elif '三级' in text:
            return PornType.Sanji
        elif '美' in text:
            return PornType.USA
        elif '動' in text or '动' in text:
            return PornType.Anim
        elif '写真' in text:
            return PornType.Picture
        else:
            return PornType.Japan

    def print_info(self):
        title = self.text
        del_strs = ['★', '√', '㊣', '♀', '[', ']', '▲', '☆', '♂',
                    '◆', '◇', '↗', '↘', '【', '】', '▼', '△', '●']
        for item in del_strs:
            title = title.replace(item, '')

        color = ''
        if self.type == PornType.Japan:
            color = Fore.CYAN
        elif self.type == PornType.USA:
            color = Fore.GREEN
        elif self.type == PornType.Anim:
            color = Fore.BLUE
        elif self.type == PornType.Picture or self.type == PornType.Sanji:
            color = Fore.MAGENTA
        print(color + '{}\t{}\t{}'.format(self.type.value, title, self.link))


class Read1024:
    def __init__(self, in_url):
        init(autoreset=True)
        self.url = in_url
        self.resource_arr = list()

    # 获取指定页面的标题和链接
    def get_data_by_page(self, in_page=1, b_print_detail=False):
        self.resource_arr = list()
        url = self.url
        if in_page >= 1:
            url = '{}&page={}'.format(self.url, in_page)
        print(Fore.YELLOW + '获取: ' + url)

        response = requests.get(url)
        if not response.status_code == 200:
            return None
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'html.parser')
        line_base = soup.find('base', id='headbase')
        # 链接前缀
        link_prefix = line_base['href']

        lines = soup.find_all('a', text=re.compile(r'^.*\d\d\.?\d\d.*'))
        valid_lines = list()

        for line in lines:
            line_text = line.get_text()
            if (re.match(r'^.*\[\d\d\.\d\d].*', line_text)
                    or re.match(r'^.*\[\d\d\d\d].*', line_text)
                    or re.match(r'^.*\d\d\.\d\d.*', line_text)):
                valid_lines.append(line)

        for line in valid_lines:
            t_resource = Resource(line.get_text(), link_prefix + line.attrs['href'])
            self.resource_arr.append(t_resource)

        self.stat(b_print_detail)

    # 统计国产,日本,欧美,动画资源分别有多少个,如果打印细节,每一个行链接都会被打印出来
    def stat(self, b_print_detail=False):
        chinese_num = 0
        japanese_num = 0
        western_num = 0
        anim_num = 0
        other_num = 0
        for i, item in enumerate(self.resource_arr):
            if b_print_detail:
                if i % 10 == 0:
                    print(Fore.CYAN, '-' * 70)
                print('{}: '.format(i), end='')
                item.print_info()

            if item.type == PornType.China:
                chinese_num += 1
            elif item.type == PornType.Japan:
                japanese_num += 1
            elif item.type == PornType.USA:
                western_num += 1
            elif item.type == PornType.Anim:
                anim_num += 1
            else:
                other_num += 1

        print(Fore.YELLOW, '资源总数:{}, 国产:{}, 日本:{}, 欧美:{}, 动画:{}, 其他:{}'
              .format(len(self.resource_arr), chinese_num, japanese_num, western_num, anim_num, other_num))

    # 打开指定页面的链接,仅打开包含筛选字符的链接
    # 对于动画,只需传入'动'即可,无需考虑简繁体
    def open_link_by_filter(self, in_page, max_open_num=-1, in_filter='', b_print_detail=False):
        self.get_data_by_page(in_page, b_print_detail)
        t_open_num = len(self.resource_arr)
        if 0 < max_open_num < t_open_num:
            t_open_num = max_open_num
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

    # 打开指定页面的链接,传入开始和结束索引
    def open_link_by_index(self, in_page, in_start_index, in_end_index):
        self.get_data_by_page(in_page)
        for i, item in enumerate(self.resource_arr):
            if in_start_index <= i < in_end_index:
                webbrowser.open_new_tab(item.link)

    # 根据类型打开指定页面的链接
    def open_link_by_type(self, in_page, types):
        self.get_data_by_page(in_page)
        for porn_type in types:
            for resource in self.resource_arr:
                if resource.type == porn_type:
                    print(resource.link)
                    webbrowser.open_new_tab(resource.link)
