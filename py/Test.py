import os
from colorama import init, Fore

folder = 'E:\\Porn\\33'

scl = [
    'YVG-042',
    'CMN-218',
    'DVAJ-458',
    'DOKS-468',
    'DDT-607',
    'RVG-071',
    'DDT-588',
    'DDT-563',
    'BDSR-295',
]


def read_folder(inpath):
    for index, item in enumerate(os.listdir(inpath)):
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            color = ''
            filename, end = os.path.splitext(item)
            bscl = False
            for code in scl:
                if code in filename:
                    bscl = True
                    break
            if bscl:
                color = Fore.YELLOW
                filename = filename + ' 水菜丽'
            else:
                filename = filename + ' 素人'

            new_path = folder + '\\' + filename + end
            print(color + '{} {} -> {}'.format(str(index).ljust(3), sub_path.ljust(30), new_path))
            os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
