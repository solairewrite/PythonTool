# 提供视频文件类型

import os

video_types = ['.mp4', '.mkv', '.avi', '.MP4', '.mpg']

not_video_types = ['.torrent']


# 判断文件是否是视频
def is_video(fullpath):
    if os.path.isfile(fullpath):
        for end in video_types:
            if fullpath.endswith(end):
                return True
    return False
