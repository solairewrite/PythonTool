import os
from colorama import init, Fore
from zhconv import convert

folder = 'E:\\Porn\\23'


def read_folder(inpath):
    for item in os.listdir(inpath):
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            color = ''
            filename, end = os.path.splitext(item)
            if not (filename.startswith('bdsm') or filename.startswith('ssni')):
                filename = filename + ' 藤森里穗'
                color = Fore.CYAN
            new_path = folder + '\\' + filename + end
            print(color + '{} -> {}'.format(sub_path.ljust(30), new_path))
            os.rename(sub_path, new_path)


def test_zhconv():
    fanti = '廣瀨雛'
    jianti = convert(fanti, 'zh-cn')
    print(jianti)


if __name__ == '__main__':
    init(autoreset=True)
    # read_folder(folder)
    test_zhconv()
