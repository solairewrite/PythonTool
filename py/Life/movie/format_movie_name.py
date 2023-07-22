# Author        : jizhixin
# Date          : 2023-03-25
# Description   : 

import os
from colorama import init, Fore

folder = 'E:\\movie\\为美好的世界献上祝福 S02'

bModify = 1


def get_episode(season_eipsode: str):
    episode = int(season_eipsode.split('E')[1])
    return episode < 10 and '0' + str(episode) or str(episode)


def read_folder(inpath):
    for index, item in enumerate(os.listdir(inpath)):
        # if '生活大爆炸' not in item:
        #     continue
        # if index >= 16:
        #     continue
        sub_path = os.path.join(inpath, item)
        if os.path.isfile(sub_path):
            color = ''
            filename, end = os.path.splitext(item)
            # if filename.startswith('The.Big.Bang.Theory.'):
            #     se = filename.replace('The.Big.Bang.Theory.', '').replace('.2017.1080p.BluRay.x265.10bit.AC3-BitsTV', '')
            # episode = get_episode(se)
            # print('{} -> {}'.format(se, num))
            num = index
            episode = num + 1 < 10 and '0' + str(num + 1) or str(num + 1)
            filename = '为美好的世界献上祝福 S02 E{0}'.format(episode)
            # filename = filename.lstrip('The.Big.Bang.Theory.')
            new_path = folder + '\\' + filename + end
            print(color + '{} {} \n->  {}'.format(str(index).ljust(3), sub_path.ljust(30), new_path))
            if bModify:
                os.rename(sub_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
