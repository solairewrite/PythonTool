# Author        : jizhixin
# Date          : 2022-07-29
# Description   : 格式化文件夹内porn视频的文件名,已忽略文件夹

import os
from colorama import init, Fore
from enum import Enum
from porn_tool import redirect_av_actress_name, is_video_fullname, porn_root_folder
from zhconv import convert

# -------------------- 运行前设置的变量 -----------------------
folder = os.path.join(porn_root_folder, '73')
only_see_no_modify = 0
# 只打印有修改的名字
only_print_change_name = 0
delete_starts = [
    'rh2048.com@', 'HD-', 'zzpp08.com@', 'avmans.com-', 'kpkp3.com_', 'kpkp56.com-',
    '8899xx.xyz_', '@蜂鳥@FENGNIAO-151.VIP-', 'avmans.com_', 'HD_',
    'hhd800.com@', 'zzpp01.com@', 'kckc-11.com@', 'freedl.org@',
    'kckc11.com@', 'kckc13.com@', 'kpkp69.com-',
    '[zzpp03.com]-', '@扶摇小飞鼠_', 'Woxav.Com@', 'zzpp06.com@',
    '[Xav-1.Xyz]', '[44x.me]', 'jav20s8.com@', '(無修正-流出) ',
    'bbsxv.xyz-', 'kckc14.com@', 'kpkp69.com_', 'javsubs91@',
    'kckc12.com@', 'kpkp3.com-', 'zzpp01.com_', '[Xavs1.Xyz]', 'JAVZIP.NET-',
    '[Xav-3.Xyz]', 'PP168.CC-', 'kckc16.com@', 'PP168.cc-', 'kckc17.com@',
    'aavv121.com@', 'taxv.xyz-', 'zzpp03.com-', '[Woxav.Com]', '[XavLt.Com]',
    '2048论坛@big2048.com -', '@蜂鳥@FENGNIAO131.VIP-', '18bt.net_',
    'freedl.org@', 'aavv333.com@', 'AVAV-66.XYZ@', 'XAVLT.COM@',
    'AVAV-55.XYZ@', 'avav66.xyz@', 'avav55.xyz@', 'avav77.xyz@', 'avav77.xyz',
    'GG5.CO@', 'gg5.co@', 'GG-5.CO@', 'AAVV-36.XYZ@', 'avav36.xyz@'
]

delete_ends = [
    '_60fps_CH_HD', '_CH_HD', '_FHD_CH', '_CH_SD', '_C', '_Uncen', '_2K', '_ch',
    '-HD', '_', '.', '_HD_CH', '-FHD', '-C', 'c', '~nyap2p.com', 'ch',
    '_CH-nyap2p.com', '.SD', '(Uncensored Leaked)', '-uncensored-nyap2p.com',
    '-uncensored', '.HD', '_1080', '-C_GG5', 'C-U', '-U', '-u'
]

# -------------------- 缓存变量 -----------------------
files = list()
change_num = 0


class CharType(Enum):
    Null = 'None'
    Alpha = '字母'
    Digit = '数字'
    Line = '-'


# 读取所有文件
def read_folder(infolder):
    global files
    for item in os.listdir(infolder):
        sub_path = os.path.join(infolder, item)
        if os.path.isfile(sub_path):
            files.append(sub_path)


def delete_start_str(instr):
    for delstr in delete_starts:
        if instr.startswith(delstr):
            instr = str(instr).removeprefix(delstr)
    return instr


def delete_end_str(instr):
    for delstr in delete_ends:
        if instr.endswith(delstr):
            instr = instr.removesuffix(delstr)
    return instr


def get_formatted_name(old_name):
    # 删除开头和末尾的字符
    old_name = delete_start_str(old_name)
    old_name = delete_end_str(old_name)

    chars = list(old_name)

    # 英文字母和数字之间加"-"
    last_type = CharType.Null
    for i in range(len(chars)):
        char = chars[i]

        if char == '-':
            break

        current_type = CharType.Null
        # print(i, char, end=' ')
        if char.isalpha():
            current_type = CharType.Alpha
        elif char.isdigit():
            current_type = CharType.Digit

        if current_type == CharType.Digit and last_type == CharType.Alpha:
            # print('need change', end=' ')
            chars.insert(i, '-')
            i += 1

        last_type = current_type
        # print(current_type.value)

    # 删除末尾的C
    num = len(chars)
    if num >= 2 and chars[num - 1] == 'C' and chars[num - 2].isdigit():
        del chars[num - 1]

    new_name = ''.join(chars)
    # 转大写
    new_name = new_name.upper()
    # 繁体转简体
    new_name = convert(new_name, 'zh-cn')
    # 女优名重定向
    new_name = redirect_av_actress_name(new_name)

    return new_name


def change_porn_names(infolder):
    for i, fullpath in enumerate(files):
        # if i != 1:
        #     continue
        if i <= -20:
            continue
        filename = os.path.split(fullpath)[1]
        if not is_video_fullname(filename):
            continue

        # real_name: ABP-747, file_type: .mp4
        old_name, file_type = os.path.splitext(filename)
        new_name = get_formatted_name(old_name)
        old_path = os.path.join(infolder, old_name) + file_type
        new_path = os.path.join(infolder, new_name) + file_type

        b_change = False
        color = ''
        if old_name != new_name:
            b_change = True
            global change_num
            change_num += 1
            color = Fore.YELLOW

        if only_see_no_modify:
            if (only_print_change_name and b_change) or (not only_print_change_name):
                print('{}{}'.format(str(i).ljust(3), old_name))
                print(color + '-> {}'.format(new_name))
                print()
        else:
            print(color + '{} {} -> {}'.format(str(i).ljust(3), old_name.ljust(20), new_name))
            os.rename(old_path, new_path)


def change_porn_name_in_folder(infolder):
    global files
    files = list()
    global change_num
    change_num = 0

    read_folder(infolder)
    change_porn_names(infolder)
    if not only_see_no_modify:
        print(Fore.YELLOW + '修改了 {} 个文件'.format(change_num))


if __name__ == '__main__':
    init(autoreset=True)
    # for i in range(1, 30):
    #     sub_folder = os.path.join(folder, str(i))
    #     print('{} {}'.format(sub_folder, '-' * 30))
    #     change_porn_name_in_folder(sub_folder)
    change_porn_name_in_folder(folder)
