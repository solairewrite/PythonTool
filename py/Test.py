import os

content_path = 'E:\\Learn\\Character Skills\\Content'
num = 0
filesmap = dict()


# 获取文件夹内所有文件
def get_folder_files(path):
    if os.path.isfile(path):
        fullname = os.path.split(path)[1]
        name = os.path.splitext(fullname)[0]
        suffix = os.path.splitext(fullname)[1]
        if suffix not in filesmap.keys():
            filesmap[suffix] = list()
        filesmap[suffix].append(name)
        global num
        num += 1
    elif os.path.isdir(path):
        for item in os.listdir(path):
            sub_path = os.path.join(path, item)
            get_folder_files(sub_path)


get_folder_files(content_path)
print('总共有 {} 个文件'.format(num))
for suffix in filesmap.keys():
    print('{} : {}'.format(suffix, len(filesmap[suffix])))
    if suffix != '.uasset':
        for item in filesmap[suffix]:
            print('\t' + item)
