# Author        : jizhixin
# Date          : 2022-11-05
# Description   : 使用的porn工具

import os
from colorama import init, Fore
import re

# porn_root_folder = 'F:\\Porn'
porn_root_folder = 'E:\\Porn2'
porn_root_folders = [
    'F:\\Porn',
    'E:\\Porn2',
]
current_folder = '23'
av_txt = 'C:\\Users\\jizhixin\\Desktop\\AV.txt'

test_folder = os.path.join(porn_root_folder, '2')
test_name = 'ABP-989 小女人'

video_types = ['.mp4', '.mkv', '.avi', '.MP4', '.mpg', '.wmv', '.rmvb', '.TS']
not_video_types = ['.torrent']

# 番号正则表达式
# porn_pattern = r'^[a-zA-z]{2,5}-[0-9]{3,4}(-[0-9])?' # 匹配最后表示上下集的-1
# porn_pattern = r'^[a-zA-z]{2,5}-[0-9]{3,4}'
porn_pattern = r'(^[a-zA-z]{2,5}-[0-9]{3,4})|(^[Ff][Cc]2-[0-9]{7})'  # 匹配素人FC2-2386297

av_actress_names = [
    '明里紬', '川北爱咲', '吉高宁宁', '桃乃木香奈', '神宫寺奈绪', '小松杏', '神乐爱音', '八木奈奈',
    '蓝芽水月', '横宫七海', '沙月芽衣', '河北彩花', '小岛南', '坂道美琉', '本庄铃', '神木丽', '凉森铃梦',
    '夏目彩春', '向井蓝', '桥本有菜', '沙月惠奈', '奥村沙织', '神菜美舞', '白桃花', '山岸逢花', '星奈爱',
    '藤森里穗', '新名爱明', '松冈千菜', '永野一夏', '纱纱原百合', '川北明沙', '深田结梨', '初川南', '枫花恋',
    '相泽南', '白石茉莉奈', '水川堇', '七泽美亚', '深田咏美', '樱井千春', '爱乃娜美', '小宵虎南', 'Rion',
    '三上悠亚', '八卦海', '松本一香', '有坂深雪', '舞咲美娜', '户田真琴', '天使萌', '日泉舞香', '水卜樱',
    '星宫一花', '天马唯', '园田美樱', '叶月桃', '永濑唯', '筱田优', '麻里梨夏', '吉良玲', '安斋拉拉', '流川夕',
    '石川澪', '结城梨乃', 'Julia', '河合明日菜', '逢见梨花', '希岛爱理', '山手梨爱', '朝田日葵', '宍户里帆',
    '天音真比奈', '梦乃爱华', '樱空桃', '岬奈奈美', '星野娜美', '小野六花', '宫下玲奈', '东条美铃', '日向真凛',
    '美谷朱里', '加美杏奈', '楪可怜', '牧野未央奈', '纱仓真菜', '楪花恋', '爱音玛利亚', '石原莉奈', '铃村爱里',
    '佐山爱', '水端麻美', '羽咲美晴', '彩美旬果', '小凑四叶', '北野未奈', '架乃由罗', '香水纯', '友田彩也香',
    '七森莉莉', '小蕾', '河南实里', '蓝川美夏', '盐见彩', '南条一香', '鹫尾芽衣', '恋渊桃菜', '神纳花',
    '花宫丽', '仓本堇', '星乃夏月', '田中宁宁', '广濑雏', '五芭', '九野雏乃', '枢木葵', '青空光', '星乃莉子',
    '新村朱里', '土屋奏', '有村希', '森莓莉', '美园和花', '大槻响', '藤井一夜', '一条美绪', '爱弓凉', '高桥圣子',
    '名里䌷'
]

change_names = {
    '本庄玲': '本庄铃', '小湊よつ葉': '小凑四叶', '安齋拉拉': '安斋拉拉', '恋渕ももな': '恋渊桃菜',
    '凉森玲梦': '凉森铃梦', '松本いちか': '松本一香', '牧野みおな': '牧野未央奈',
    '紗倉まな': '纱仓真菜', 'julia': 'Julia', '名里紬': '明里紬', '鈴村あいり': '铃村爱里',
    '塩見彩': '盐见彩', '新有菜': '桥本有菜', '蝶花恋': '楪可怜', '楪花恋': '楪可怜',
    '七泽米亚': '七泽美亚', '神木麗': '神木丽', '白桃はな': '白桃花', '神納花': '神纳花',
    '大槻ひびき': '大槻响', '愛乃娜美': '爱乃娜美', '小宵こなん': '小宵虎南', 'RION': 'Rion',
    '藤井いよな': '藤井一夜', '宮下玲奈': '宫下玲奈', '明里紬': '名里䌷'
}


# 判断文件全名是否是视频
def is_video_fullname(fullname):
    file_type = '.' + fullname.split('.')[-1]
    if file_type in video_types:
        return True
    return False


# 判断文件全名是否是视频
def is_video_fullpath(fullpath):
    if os.path.isfile(fullpath):
        fullname = os.path.split(fullpath)[1]
        file_type = '.' + fullname.split('.')[-1]
        if file_type in video_types:
            return True
    return False


# 从文件名中(不包含文件类型后缀)获取AV番号
def get_porn_number(file_name):
    match_result = re.search(porn_pattern, file_name)
    if match_result:
        # 转大写
        porn_number = match_result[0].upper()
        return porn_number
    else:
        return None


# 获取文件夹内所有的番号
def get_folder_porn_number(path, inlist):
    for fullname in os.listdir(path):
        if is_video_fullname(fullname):
            file_name = os.path.splitext(fullname)[0]
            porn_number = get_porn_number(file_name)
            if porn_number:
                if porn_number not in inlist:
                    inlist.append(porn_number)
                    # print(Fore.YELLOW + '{} -> {}'.format(porn_number.ljust(10), file_name))
                else:
                    print(Fore.MAGENTA + '重复番号: {0}, 文件夹: {1}'.format(porn_number, path))
            else:
                print(Fore.RED + '文件名不规范: {0}, 文件夹: {1}'.format(file_name, path))


# 获取porn文件夹下所有日本文件夹下的番号
def get_all_folder_porn_number():
    all_porn_numbers = list()

    for root_folder in porn_root_folders:
        for sub_folder_name in os.listdir(root_folder):
            if not sub_folder_name.startswith('Anim') and not sub_folder_name.startswith('USA'):
                sub_folder = os.path.join(root_folder, sub_folder_name)
                if os.path.isdir(sub_folder):
                    # print(str(i).ljust(3) + '-' * 30)
                    get_folder_porn_number(sub_folder, all_porn_numbers)

    all_porn_numbers.sort()
    print(Fore.YELLOW + '番号数量: {0}'.format(len(all_porn_numbers)))
    # for i, item in enumerate(all_porn_numbers):
    #     count = i + 1
    #     print('{} {}'.format(str(count).ljust(5), item))
    #     if count % 10 == 0:
    #         print()

    return all_porn_numbers


# 将change_names字典中包含的女优名重定向
def redirect_av_actress_name(av_name):
    for k, v in change_names.items():
        if k in av_name:
            return av_name.replace(k, v)
    return av_name


# 获取一个文件夹下所有指定女优视频的路径
def get_folder_all_actress_path(folder, inlist, actress_name):
    for fullname in os.listdir(folder):
        if is_video_fullname(fullname):
            if actress_name in fullname:
                inlist.append(os.path.join(folder, fullname))


# 获取porn文件夹下所有指定女优视频的路径
def get_all_folder_actress_path(actress_name):
    root_folder = porn_root_folder
    paths = list()

    for sub_folder_name in os.listdir(root_folder):
        if not sub_folder_name == actress_name \
                and not sub_folder_name.startswith('Anim') \
                and not sub_folder_name.startswith('USA') \
                and not sub_folder_name.startswith('SM'):
            sub_folder = os.path.join(root_folder, sub_folder_name)
            if os.path.isdir(sub_folder):
                get_folder_all_actress_path(sub_folder, paths, actress_name)

    # print(Fore.YELLOW + '番号数量: {0}'.format(len(paths)))
    # for i, item in enumerate(paths):
    #     count = i + 1
    #     print('{} {}'.format(str(count).ljust(5), item))
    #     if count % 10 == 0:
    #         print()

    return paths


# 获取一个文件夹下所有指定番号系列的视频的路径
def get_folder_all_codetype_path(folder, inlist, codetype):
    for fullname in os.listdir(folder):
        if is_video_fullname(fullname):
            if re.search(codetype, fullname, re.IGNORECASE):
                inlist.append(os.path.join(folder, fullname))


# 获取porn文件夹下所有指定番号系列的视频的路径
def get_all_folder_codetype_path(codetype):
    root_folder = porn_root_folder
    paths = list()

    for sub_folder_name in os.listdir(root_folder):
        if codetype not in sub_folder_name \
                and not sub_folder_name.startswith('Anim') \
                and not sub_folder_name.startswith('USA'):
            sub_folder = os.path.join(root_folder, sub_folder_name)
            if os.path.isdir(sub_folder):
                get_folder_all_codetype_path(sub_folder, paths, codetype)

    # print(Fore.YELLOW + '番号数量: {0}'.format(len(paths)))
    # for i, item in enumerate(paths):
    #     count = i + 1
    #     print('{} {}'.format(str(count).ljust(5), item))
    #     if count % 10 == 0:
    #         print()

    return paths


if __name__ == '__main__':
    init(autoreset=True)
    get_all_folder_porn_number()
