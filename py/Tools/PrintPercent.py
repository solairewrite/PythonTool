# Author        : Zhixin.Ji
# Date          : 2020-04-16
# Description   : 打印进度条
import time


class PrintPercent:
    @staticmethod
    def print(percent, length=30):
        start_count = int(percent * length)
        space_count = length - start_count

        per_str = '\r[{}] {:.1f}%'.format(
            '*' * start_count + ' ' * space_count,
            percent * 100.0)
        if percent >= 1.0:
            per_str += '\n'
        print(per_str, end='', flush=True)


if __name__ == '__main__':
    t_max = 10
    for i in range(t_max):
        PrintPercent.print(i * 1.0 / t_max)
        time.sleep(0.1)
    PrintPercent.print(1.0)
