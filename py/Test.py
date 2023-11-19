import os
from colorama import init, Fore
from zhconv import convert

folder = 'F:\\Porn\\Anim 02'
b_only_see_no_modify = 0


def doit():
    for index, item in enumerate(os.listdir(folder)):
        old_name: str = os.path.splitext(item)[0]
        old_type = os.path.splitext(item)[1]

        old_path = os.path.join(folder, item)
        if os.path.isfile(old_path):
            if old_name.startswith('[Milky]社全作品合集'):
                new_name = old_name + '.rar'
                new_path = os.path.join(folder, new_name)
                print(old_path)
                print(Fore.YELLOW + new_path)

                if not b_only_see_no_modify:
                    os.rename(old_path, new_path)


def change_actress_name():
    folder = 'F:\\Porn\\明里䌷'
    for item in os.listdir(folder):
        old = os.path.join(folder, item)
        item = item.replace('明里紬', '明里䌷')
        new = os.path.join(folder, item)
        print(old)
        print(Fore.YELLOW + new)
        os.rename(old, new)


def test():
    for item in os.listdir('D:\Learn\CLionLib'):
        print(item)


if __name__ == '__main__':
    init(autoreset=True)
    # doit()
    # change_actress_name()
    # print(convert('八掛海', 'zh-cn'))
    test()
