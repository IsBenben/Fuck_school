import os
import threading
import time

def cake_thread():
    magics = [114, 514, 1919, 810]
    filename_template = 'C:\\Users\\{username}\\Desktop\\cake{}.txt'
    contents = """一个大蛋糕：

                    0   0
                    |   |
                ____|___|____
            0  |~ ~ ~ ~ ~ ~|   0
            |  |           |   |
        ___|__|___________|___|__
        |/\/\/\/\/\/\/\/\/\/\/\/|
    0   |       H a p p y       |   0
    |   |/\/\/\/\/\/\/\/\/\/\/\/|   |
    _|___|_______________________|___|__
    |/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    |                                   |
    |         B i r t h d a y! ! !      |
    | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
    |___________________________________|

    生日快乐！你删不掉他的快乐！

    哈哈哈，永远别想删掉他，删掉就自动重新创建！！！
    """

    def check_file():
        if not os.path.exists(filename):
            return False
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                if f.read() == contents:
                    return True
            return False
        except Exception as e:
            print('检查错误：', e)
            return False

    while True:
        for magic in magics:
            filename = filename_template.format(magic)
            if not check_file():
                print('Cake 已丢失，准备重新创建。')
                try:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(contents)
                    print('成功创建 Cake。')
                except Exception as e:
                    print('创建文件错误：', e)
        time.sleep(0.01)

threading.Thread(target=cake_thread).start()
