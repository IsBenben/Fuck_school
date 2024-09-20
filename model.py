# *-* encoding: utf-8 *-*

# 请使用该main.py文件！它整合了所有功能，可以更方便的“Fuck School”
# model.py是main.py的模板，但缺失了很多重要信息，和main.py有本质的区别
# 若想通过model.py生成main.py，请使用update.py

import tkinter as tk
from tkinter import font
import os

fucks = []
descriptions = []

class SelectPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.list = tk.Listbox(self, selectmode=tk.SINGLE)
        self.list.pack(fill=tk.BOTH, expand=True)

        special_folder = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
        for user in os.listdir('C:\\Users\\'):
            if user in special_folder:
                continue
            self.list.insert(tk.END, user)

class FuckPage(tk.Frame):
    def __init__(self, master=None, index=0):
        super().__init__(master)

        self.index = index
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self, font=font.Font(family='新宋体'))
        self.text.pack(fill=tk.BOTH, expand=True)

        self.text.tag_config('name', font=font.Font(family='新宋体', slant='italic'))
        self.text.tag_config('title', font=font.Font(family='新宋体', weight='bold'))

        for line in descriptions[self.index].split('\n'):
            name = False
            title = False

            for char in line:
                if char == '“':
                    name = True
                elif char == '【':
                    title = True
                
                style = []
                if name:
                    style.append('name')
                if title:
                    style.append('title')
                self.text.insert(tk.END, char, *style)

                if char == '”':
                    name = False
                elif char == '】':
                    title = False
            self.text.insert(tk.END, '\n')

class GoodbyePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Message(self, text='恭喜你，你已经成功完成了设置向导！\n\n确定要应用你的设置吗，请慎重决定！')
        self.label.pack()

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fuck School")
        self.resizable(False, False)

        self.index = 0
        self.last_page = None
        self.create_widgets()
        self.create_widgets()
        self.selected = []

    def select(self, value):
        print('用户选择', value)
        self.selected.append(value)
        self.create_widgets()

    def create_widgets(self):
        if self.last_page:
            self.last_page.destroy()

        if self.index == 0:
            self.top_frame = tk.Frame(self)
            self.top_frame.pack(side=tk.TOP, fill=tk.X)

            self.left_button = tk.Button(self.top_frame, text='...')
            self.left_button.pack(side=tk.LEFT)

            self.right_button = tk.Button(self.top_frame, text='...')
            self.right_button.pack(side=tk.RIGHT)

            self.title_label = tk.Label(self.top_frame, text='...')
            self.title_label.pack(side=tk.TOP, fill=tk.X)

        if self.index == 1:
            self.left_button.config(state=tk.DISABLED, text='【禁用】', command=lambda: None)
            self.right_button.config(state=tk.NORMAL, text='确定', command=lambda: self.select(l.get(l.curselection()[0])) if l.curselection() else None)
            self.title_label.config(text='选择用户')

            self.last_page = SelectPage(self)
            l = self.last_page.list
            self.last_page.pack(fill=tk.BOTH, expand=True)
        
        if 2 <= self.index <= 1 + len(fucks):
            self.left_button.config(state=tk.NORMAL, text='启用', command=lambda: self.select('enable'))
            self.right_button.config(state=tk.NORMAL, text='禁用', command=lambda: self.select('disable'))
            self.title_label.config(text='恶搞模块')

            self.last_page = FuckPage(self, index=self.index - 2)
            self.last_page.pack(fill=tk.BOTH, expand=True)
        
        if self.index > 1 + len(fucks):
            self.left_button.config(state=tk.NORMAL, text='应用（慎重）', command=lambda: self.last_step())
            self.right_button.config(state=tk.NORMAL, text='退出', command=lambda: self.destroy())
            self.title_label.config(text='再见！')

            self.last_page = GoodbyePage(self)
            self.last_page.pack(fill=tk.BOTH, expand=True)
        
        self.index += 1
    
    def last_step(self):
        result = []
        username = self.selected.pop(0)
        for code, state in zip(fucks, self.selected):
            if state == 'enable':
                result.append(code.replace('{username}', username))
        codes = '\n\n'.join(result)
        with open(f'C:\\Users\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fuck_school.pyw', 'w', encoding='utf-8') as f:
            f.write(codes + '\n\n# This file is generated by Fuck School. Please do not modify it.\n# 这个文件是由 Fuck School 自动生成的。请不要修改它。\n\n')
        self.destroy()
        
MainWindow().mainloop()
