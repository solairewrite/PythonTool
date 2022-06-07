# Author        : Zhixin.Ji
# Date          : 2020-04-18
# Description   : 窗体程序
# TK(窗口),Label,Button,定时器,Entry(单行输入框),Text(多行输入框)
import tkinter as tk
import time

global window
bgcolor = '#C7EDCC'
global strvar
global entry  # 输入框


def demo_window():
    global window
    window = tk.Tk()
    window.title('窗口程序示例')
    window.geometry('800x600')
    window.config(bg=bgcolor)
    # 设置窗口Icon,只能用.ico
    window.iconbitmap('../../Resource/girl.ico')
    # 开启窗口
    # window.mainloop()


def demo_label():
    global window
    label = tk.Label(
        window,
        text='阿库娅',
        # 颜色可以用英文单词或rgb
        bg='pink',
        fg='#3CB371',
        font=('Arial', 18),
        width=15, height=2,
    )
    label.pack()

    # 变量设置文字
    # 4种变量类型: BooleanVar, IntVar, DoubleVar, StringVar
    global strvar
    strvar = tk.StringVar()
    strvar.set('惠惠')
    label2 = tk.Label(
        window,
        textvariable=strvar,
        fg='magenta', bg=bgcolor,
        font=18,
    )
    label2.pack()


def on_click_button():
    global strvar
    strvar.set('爆裂魔法')


def demo_button():
    button = tk.Button(
        window,
        text='释放大招',
        # 按钮回调函数
        command=on_click_button,
    )
    button.pack()


def demo_timer():
    """定时器"""
    window.title('邪恶py ' + time.strftime('%Y-%m-%d %H:%M:%S'))
    window.after(1000, demo_timer)


def on_enter_txt(instr):
    global strvar
    global entry
    # 获取输入框内容
    strvar.set(entry.get())


def demo_entry():
    """单行输入框"""
    global entry
    global strvar
    entry = tk.Entry(
        window,
        # 绑定文字
        # textvariable=strvar,
    )
    # 回调函数
    entry.bind('<KeyRelease>', on_enter_txt)
    entry.pack()


def demo_text():
    """多行输入框"""
    text = tk.Text(window, width=50, height=10)
    text.insert('insert', '笨蛋女神\n')
    text.insert('insert', '阿库娅\n')
    text.insert('end', '大祭司\n')
    text.pack()


if __name__ == '__main__':
    demo_window()
    demo_label()
    demo_button()
    demo_timer()
    demo_entry()
    demo_text()
    window.mainloop()
