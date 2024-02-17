# Author        : jizhixin
# Date          : 2023-05-20
# Description   : 将同一个女优的片子移到一个文件夹下

import os
from colorama import init, Fore
from _00_porn_tool import porn_root_folder, get_all_folder_actress_path

finish_actress_names = [
    '吉高宁宁', '桥本有菜', '有坂深雪', '楪可怜', '樱空桃', '凉森铃梦', '藤森里穗', '白石茉莉奈', '神宫寺奈绪',
    '美谷朱里',
    '河北彩花', '相泽南', '新村朱里', '深田咏美', '铃村爱里', '七森莉莉', '山岸逢花', '水川堇', '夏目彩春', '小蕾',
    '纱纱原百合', '爱弓凉', '桃乃木香奈', '小松杏', '横宫七海', '向井蓝', '神木丽', '石川澪', '坂道美琉', '七泽美亚',
    '松本一香', '神菜美舞', '日泉舞香', '水卜樱', '梦乃爱华', '天使萌', '枫花恋', '麻里梨夏', '沙月芽衣', '白桃花',
    '八卦海', '希岛爱理', '土屋奏', '神乐爱音', '永野一夏', '小宵虎南', '结城梨乃',
]

# 女优名字
actress_names = [
    # '名里䌷', '岬奈奈美'
    # '葵司', '本田桃', '白峰美羽', '久我花音', '小仓由菜'
    # '明里䌷', '樱井千春', '小仓由菜', '八挂海', '花狩舞'
    '日向真凛'
]
b_only_see_no_modify = 0


# 将同一个女优的片子移到一个文件夹下
def move_actress_to_folder(in_actress_name):
    old_paths = get_all_folder_actress_path(in_actress_name)

    target_folder = in_actress_name
    new_folder = os.path.join(porn_root_folder, target_folder)
    if not os.path.isdir(new_folder):
        if not b_only_see_no_modify:
            os.makedirs(new_folder)

    print(Fore.YELLOW + '番号数量: {0}'.format(len(old_paths)))
    for index, old_path in enumerate(old_paths):
        filename = os.path.split(old_path)[1]
        new_path = os.path.join(new_folder, filename)

        if new_path == old_path:
            continue

        count = index + 1
        print('{}{}'.format(str(count).ljust(5), old_path))
        print(Fore.CYAN + '{}{}'.format('->'.ljust(5), new_path))
        if count % 10 == 0:
            print()

        if not b_only_see_no_modify:
            os.rename(old_path, new_path)


def move_all_actresses():
    for actress_name in actress_names:
        move_actress_to_folder(actress_name)


if __name__ == '__main__':
    init(autoreset=True)
    move_all_actresses()
