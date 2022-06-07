# Author        : Zhixin.Ji
# Date          : 2020-07-08
# Description   : 比较数组a,b
from colorama import init, Fore


class CompareList:
    def __init__(self, a, b):
        init(autoreset=True)

        self.list_a = a
        self.list_b = b

        self.both_list = []
        self.only_a_list = []
        self.only_b_list = []

        self.compare_list()

    def compare_list(self):
        for a in self.list_a:
            if a in self.list_b:
                self.both_list.append(a)
            else:
                self.only_a_list.append(a)
        for b in self.list_b:
            if b in self.list_a:
                if b not in self.both_list:
                    self.both_list.append(b)
            else:
                self.only_b_list.append(b)

        return self.both_list, self.only_a_list, self.only_b_list

    @staticmethod
    def __print_arr(msg, arr):
        print()
        print(Fore.YELLOW + msg + ' {} 个'.format(len(arr)))
        for item in arr:
            print(item)

    def print_info(self):
        CompareList.__print_arr('两个数组中都存在的元素:', self.both_list)
        CompareList.__print_arr('仅在a中存在的元素:', self.only_a_list)
        CompareList.__print_arr('仅在b中存在的元素:', self.only_b_list)
