# Author        : Zhixin.Ji
# Date          : 2020-04-19
# Description   : 窗体程序
# Canvas(画布可以绘制图片,直线,圆,矩形),Menu,Frame,messagebox
# pack布局,grid布局,place指定位置
import tkinter as tk
import tkinter.messagebox as mb

window = tk.Tk()
photo = tk.PhotoImage(file='../../../Resource/丝袜.png')


def init_window():
    window.title('python')
    window.geometry('800x600')
    window.iconbitmap('../../Resource/girl.ico')


def demo_canvas():
    canvas = tk.Canvas(
        window,
        bg='orange',
        height=100, width=200,
    )
    canvas.pack()

    # 图片,image必须为全局变量
    # north-west
    canvas.create_image(10, 10, anchor='nw', image=photo)
    # 直线
    x0, y0, x1, y1 = 50, 50, 80, 80
    canvas.create_line(x0, y0, x1, y1)
    canvas.create_oval(x0, y0, x1, y1, fill='yellow')
    # 扇形
    canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=180)
    # 矩形
    canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)


def on_click_menu():
    print('点击菜单')


def demo_menu():
    menubar = tk.Menu(window)
    window.config(menu=menubar)
    # 横向栏
    filemenu = tk.Menu(menubar, tearoff=0)
    # 下拉菜单
    menubar.add_cascade(label='文件', menu=filemenu)
    # 子菜单
    filemenu.add_command(label='新文件', command=on_click_menu)
    filemenu.add_command(label='打开', command=on_click_menu)
    # 分割线
    filemenu.add_separator()
    filemenu.add_command(label='删除', command=on_click_menu)

    editmeun = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='编辑', menu=editmeun)
    editmeun.add_command(label='全部删除', command=on_click_menu)

    # 子菜单的子菜单
    submenu = tk.Menu(filemenu)
    filemenu.add_cascade(label='邪恶', menu=submenu)
    submenu.add_command(label='绅士', command=on_click_menu)


def demo_frame():
    frame = tk.Frame(window)
    frame.pack()

    frame1 = tk.Frame(frame)
    frame2 = tk.Frame(frame)
    frame1.pack(side='left')
    frame2.pack(side='right')

    tk.Label(frame1, text='容器1-元素A').pack()
    tk.Label(frame1, text='容器1-元素B').pack()
    tk.Label(frame2, text='容器2-元素A').pack()


def demo_messagebox():
    # tkinter.messagebox 需要额外引入
    mb.showinfo(title='信息', message='阿库娅')
    mb.showwarning(title='警告', message='阿库娅')
    mb.showerror(title='错误', message='阿库娅')
    res = mb.askyesno(title='选择', message='返回 True / False')
    print(res)


def demo_pack():
    """对齐"""
    tk.Label(window, text='阿库娅').pack(side='top')
    tk.Label(window, text='阿库娅').pack(side='bottom')
    tk.Label(window, text='阿库娅').pack(side='left')
    tk.Label(window, text='阿库娅').pack(side='right')


def demo_grid():
    """栅格,开某些窗口会导致报错"""
    for i in range(4):
        for j in range(3):
            tk.Label(window, text='{}-{}'.format(i, j)) \
                .grid(row=i, column=j, padx=10, pady=10)


def demo_place():
    """指定位置,开某些窗口会导致报错"""
    tk.Label(window, text='指定位置') \
        .place(x=70, y=30, anchor='nw')


if __name__ == '__main__':
    init_window()
    # demo_canvas()
    # demo_menu()
    # demo_frame()
    # demo_messagebox()
    # demo_pack()
    # demo_grid()
    demo_place()
    window.mainloop()
