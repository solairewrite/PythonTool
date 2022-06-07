# Author        : Zhixin.Ji
# Date          : 2020-09-04
# Description   : 读书进度
path = 'F:\\Learn\\Notes\\书籍\\京华烟云.txt'
current_line = 12768

line_index = 0
word_num = 0
current_word_num = 0
with open(path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        line_index += 1
        word_num += len(line)
        if line_index == current_line:
            current_word_num = word_num
            print('行数 {}, 字数 {}'.format(line_index, word_num))
print('行数 {}, 字数 {}'.format(line_index, word_num))
print('{0:.0f}%'.format(current_word_num * 100 / word_num))
