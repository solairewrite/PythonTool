# Author        : Zhixin.Ji
# Date          : 2020-09-14
# Description   : 文件选择框
import tkinter as tk
import tkinter.filedialog as tkfile


def choose_file():
    filename = tkfile.askopenfilename()
    print(filename)


def choose_folder():
    folder = tkfile.askdirectory()
    print(folder)


def main():
    window = tk.Tk()
    window.geometry('400x300')

    button = tk.Button(window, text='选择文件', command=choose_file)
    button.pack()

    button = tk.Button(window, text='选择文件夹', command=choose_folder)
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
