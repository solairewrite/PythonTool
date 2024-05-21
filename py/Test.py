import os
from colorama import init, Fore
from zhconv import convert

folder = 'E:\\Movie\\老友记.全10季.Friends.1080p.NF.WEB-DL.DDP5.1.x264-DHTCLUB\\老友记.第十季.Friends.S10.1080p.NF.WEB-DL.DDP5.1.x264-DHTCLUB'
new_foler = 'E:\\Movie\\老友记 S10'
b_only_see_no_modify = 0


def doit():
    episode = 0
    for index, item in enumerate(os.listdir(folder)):
        # if index >= 22:
        #     continue
        old_name: str = os.path.splitext(item)[0]
        old_type = os.path.splitext(item)[1]
        # if old_type != '.ass' or old_name.endswith('.tc'):
        #     continue

        old_path = os.path.join(folder, item)
        if os.path.isfile(old_path):
            # episode = int(old_name.replace('[繁體中文] 進擊的巨人 第三季 ep ', ''))
            episode += 1
            if episode > 22:
                continue
            # index = episode - 1
            numstr = episode < 10 and '0{}'.format(episode) or str(episode)
            new_name = '老友记 S10 E{}'.format(numstr)
            new_path = os.path.join(new_foler, new_name) + old_type
            print(old_path)
            print(Fore.YELLOW + new_path)

            if not b_only_see_no_modify:
                if not os.path.isdir(new_foler):
                    os.makedirs(new_foler)
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


if __name__ == '__main__':
    init(autoreset=True)
    doit()
    # change_actress_name()
    a = 'Clannad S2 另一个世界 杏篇'
    b = 'Clannad S2 特别篇 一年前的事'
    c = 'Clannad S2 总集篇'
