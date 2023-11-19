import os
from colorama import init, Fore
from py.Life.view_video._00_porn_tool import is_video_fullname, porn_root_folder

folder = os.path.join(porn_root_folder, '_X 筱田优')

bModify = 1
actress_name = '筱田优'


def read_folder(inpath):
    for index, item in enumerate(os.listdir(inpath)):
        if not is_video_fullname(item):
            continue

        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            color = ''
            filename, end = os.path.splitext(item)

            if actress_name not in filename:
                filename = filename + ' ' + actress_name
                filename = str(filename).upper()

                new_path = folder + '\\' + filename + end
                print(color + '{} {} -> {}'.format(str(index).ljust(3), sub_path.ljust(30), new_path))
                if bModify:
                    os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
