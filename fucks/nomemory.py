import time
import threading

def nomemory_thread():
    while True:
        a = []
        for _ in range(114514):
            a.append('哈' * 23333)
        time.sleep(15)
        a.clear()
        time.sleep(5)

threading.Thread(target=nomemory_thread).start()
