import os
from colorama import init, Fore

folder = 'D:\\Mary\\发票 2023-07-02'
b_only_see_no_modify = 0


def doit():
    for index, item in enumerate(os.listdir(folder)):
        old_name = os.path.splitext(item)[0]
        new_name: str = old_name.replace('_江苏省医疗门诊收费票据（电子）_', ' 发票 ')
        new_name = new_name.replace('_江苏省医疗住院收费票据（电子）_', ' 发票 ')
        new_name = new_name.split('元')[0]
        # print(old_name)
        # print(Fore.YELLOW + new_name)
        num_str = (index + 1 < 10) and '0{0}'.format(index + 1) or str(index + 1)
        new_path = os.path.join(folder, '{0}{1}.pdf'.format(num_str.ljust(3), new_name))

        old_path = os.path.join(folder, item)
        print(old_path)
        print(Fore.YELLOW + new_path)

        if not b_only_see_no_modify:
            os.rename(old_path, new_path)


if __name__ == '__main__':
    init(autoreset=True)
    doit()
