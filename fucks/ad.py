import tkinter as tk
from tkinter import messagebox, font
import threading
import time
import webbrowser
import random

def ad_thread():
    class MainWindow(tk.Tk):
        def __init__(self):
            super().__init__()
            self.overrideredirect(True)
            self.geometry('480x360+{x}+{y}'.format(x=random.randint(0, self.winfo_screenwidth() - 480),
                                                   y=random.randint(0, self.winfo_screenheight() - 360)))
            self.attributes('-topmost', True)
            self.resizable(False, False)
            self.protocol('WM_DELETE_WINDOW', self.close)
            self.bind('<Key-W>', self.always_close)
            self.bind('<Key-w>', self.always_close)

            bg = tk.Frame(self, bg='#333333')
            bg.pack(fill=tk.BOTH, expand=True)

            title = tk.Label(bg, text='提示：', font=font.Font(size=36, weight='bold'), fg='white', bg='#333333')
            title.pack(padx=10, pady=10, fill=tk.X)
            title = tk.Label(bg, text='不要298，不要198，不要98！', font=font.Font(size=24, weight='bold'), fg='#919810', bg='#114514')
            title.pack(padx=10, pady=10, fill=tk.X)
            title = tk.Label(bg, text='您已获得一张免费的广告，广告窗口无法关闭。', font=font.Font(size=16, weight='bold'), fg='#919810', bg='#114514')
            title.pack(padx=10, pady=10, fill=tk.X)
            button = tk.Button(bg, text='点击查看广告', font=font.Font(size=32, weight='bold'), fg='white', bg='#222222', command=self.open_ad)
            button.pack(padx=10, pady=10, fill=tk.X)

        def close(self):
            messagebox.showwarning('警告', '广告窗口无法关闭！接受惩罚：出现5个新广告窗口。')
            for _ in range(5):
                threading.Thread(target=lambda: MainWindow().mainloop()).start()
        
        def always_close(self, _):
            self.destroy()
            raise KeyboardInterrupt

        def open_ad(self):
            webbrowser.open('https://www.bilibili.com/video/BV1GJ411x7h7/')
            messagebox.showinfo('提示', '广告内容已打开，请注意观看！')
            self.destroy()
        
        def report_callback_exception(self, exc, val, tb):
            raise exc

    while True:
        try:
            start = time.time()
            MainWindow().mainloop()
            dis = time.time() - start
            time.sleep(min(dis * 2, 90))
        except KeyboardInterrupt:
            print('^C\nAD 线程结束')
            break

ad = threading.Thread(target=ad_thread)
ad.start()
