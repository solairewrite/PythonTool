# Author        : jizhixin
# Date          : 2023-03-25
# Description   : 

import os
from colorama import init, Fore
import re

folder = 'E:\\Movie\\无耻家庭'
movie_name = '无耻家庭'
season_pattern = r'S\d{2}'
episode_pattern = r'E\d{2}'

bModify = 1


def get_episode(filename: str):
    season_reg = re.search(season_pattern, filename)
    season_tuple = season_reg.span()
    season_str = filename[season_tuple[0]: season_tuple[1]]

    episode_reg = re.search(episode_pattern, filename)
    episode_tuple = episode_reg.span()
    episode_str = filename[episode_tuple[0]: episode_tuple[1]]

    result = '{0} {1}'.format(season_str, episode_str)
    return result


def read_folder(infolder):
    for index, item in enumerate(os.listdir(infolder)):
        old_path = os.path.join(infolder, item)
        if os.path.isfile(old_path):
            filename, end = os.path.splitext(item)

            episode = get_episode(filename)
            new_filename = '{0} {1}'.format(movie_name, episode)
            new_path = os.path.join(infolder, new_filename + end)

            if old_path != new_path:
                print()
                print(old_path)
                print(Fore.YELLOW + new_path)

                if bModify:
                    os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    read_folder(folder)
