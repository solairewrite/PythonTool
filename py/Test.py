import os
from colorama import init, Fore

folder = 'E:\\Porn\\16'


def read_folder(inpath):
    for item in os.listdir(inpath):
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            end = os.path.splitext(item)[1]
            new_path = folder + '\\' + item[0:8] + ' 七森莉莉' + end
            print('{} -> {}'.format(sub_path, new_path))
            os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
