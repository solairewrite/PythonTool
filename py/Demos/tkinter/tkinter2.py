# Author        : Zhixin.Ji
# Date          : 2020-04-19
# Description   : 窗体程序
# Listbox(列表),Radiobutton(单选框),Scale(滑动条),Checkbutton(复选框)
import tkinter as tk

global window
global single_select_var
global single_select_label
global scale_var
global int1, int2
global check_label


def create_window():
    global window
    window = tk.Tk()
    window.title('python')
    window.geometry('800x600')
    window.iconbitmap('../../Resource/丝袜.ico')


def demo_listbox():
    """列表"""
    var = tk.StringVar()
    var.set((11, 22, 33, 44))

    lb = tk.Listbox(window, listvariable=var)
    lb.pack()
    lb.insert(0, '00')
    lb.delete(2)


def on_select_radiobutton():
    single_select_label.config(text=single_select_var.get())


def demo_radiobutton():
    """单选框"""
    global single_select_var
    single_select_var = tk.StringVar()
    # 默认都不选中,否则都选中
    single_select_var.set(0)

    global single_select_label
    single_select_label = tk.Label(window, text='请选择一位同伴')
    single_select_label.pack()

    r1 = tk.Radiobutton(window, text='阿库娅', value='阿库娅', variable=single_select_var, command=on_select_radiobutton)
    r2 = tk.Radiobutton(window, text='惠惠', value='惠惠', variable=single_select_var, command=on_select_radiobutton)
    r1.pack()
    r2.pack()


def on_change_scale(value):
    scale_var.set(value)


def demo_scale():
    """滑动条"""
    global scale_var
    scale_var = tk.DoubleVar()

    label = tk.Label(window, textvariable=scale_var)
    label.pack()

    scale = tk.Scale(
        window,
        from_=0, to=100,
        orient=tk.HORIZONTAL,
        lengt=700,
        showvalue=1,  # 是否在上方显示数值
        tickinterval=10,  # 显示刻度间隔
        resolution=0.1,  # 步进
        command=on_change_scale  # 回调函数
    )
    scale.set(10)
    scale.pack()


def on_click_checkbutton():
    txt = ''
    if int1.get() == 1:
        txt += ' 阿库娅'
    if int2.get() == 1:
        txt += ' 惠惠'
    txt = '独自前往' if txt == '' else '选择了: ' + txt
    check_label.config(text=txt)


def demo_checkbutton():
    """复选框"""
    global check_label
    check_label = tk.Label(window, text='选择同伴')
    check_label.pack()

    global int1, int2
    int1 = tk.IntVar()
    int2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='阿库娅',
                        variable=int1, onvalue=1, offvalue=0,
                        command=on_click_checkbutton)
    c2 = tk.Checkbutton(window, text='惠惠',
                        variable=int2, onvalue=1, offvalue=0,
                        command=on_click_checkbutton)
    c1.pack()
    c2.pack()


if __name__ == '__main__':
    create_window()
    demo_listbox()
    demo_radiobutton()
    demo_scale()
    demo_checkbutton()
    window.mainloop()
