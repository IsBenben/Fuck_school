# Convert from C++

from random import randint, randrange, choice
import ctypes
from ctypes import windll, wintypes
import time
import threading

gdi = windll.gdi32
user = windll.user32

def screendraw_thread():
    def is_key_pressed(key):
        return user.GetKeyState(key) & 0x8000 != 0

    def drawLine(hdc):
        rgb = randint(0, 0xffffff)
        x1 = randrange(0, width)
        x2 = randrange(0, width)
        y1 = randrange(0, height)
        y2 = randrange(0, height)
        w = randint(3, 10)
        hpen = gdi.CreatePen(0, w, rgb)
        gdi.SelectObject(hdc, hpen)
        gdi.MoveToEx(hdc, x1, y1, 0)
        gdi.LineTo(hdc, x2, y2)

    class POINT(ctypes.Structure):
        _fields_ = [("x", wintypes.LONG), 
                    ("y", wintypes.LONG)]

    def drawCursorCircle(hdc):
        mouse = POINT()
        user.GetCursorPos(ctypes.byref(mouse))
        x, y = mouse.x, mouse.y

        rgb = randint(0, 0xffffff)
        w = randint(3, 10)

        hpen = gdi.CreatePen(0, 1, rgb)
        gdi.SelectObject(hdc, hpen)
        gdi.Ellipse(hdc, x - w, y - w, x + w, y + w)
        gdi.DeleteObject(hpen)

    def drawIcon(hdc):
        x = randrange(0, width)
        y = randrange(0, height)
        id = randint(32512, 32516)
        hIcon = user.LoadIconW(0, id)
        user.DrawIcon(hdc, x, y, hIcon)
        user.DestroyIcon(hIcon)

    def drawDissolution(hdc):
        w = randint(10, 30)
        x = randint(0, width - w)
        s = randint(10, 30)
        gdi.BitBlt(hdc, x, s, w, height, hdc, x, 0, 13369376)

    def drawMovescreen(hdc):
        mul = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dir = choice(mul)
        s = randint(3, 10)
        gdi.BitBlt(hdc, dir[0] * s, dir[1] * s, width, height, hdc, 0, 0, 13369376)

    ikun = 2.5  # 两年半

    hWnd = user.GetDesktopWindow()
    fns = [drawLine, drawCursorCircle, drawIcon, drawDissolution, drawMovescreen]
    while True:
        if is_key_pressed(ord('W')) or is_key_pressed(ord('w')):
            print('^C\nikun: infinity')
            break
        
        hdc = user.GetDC(hWnd)
        width = gdi.GetDeviceCaps(hdc, 118)
        height = gdi.GetDeviceCaps(hdc, 117)
        choice(fns)(hdc)

        user.ReleaseDC(hWnd, hdc)
        time.sleep(ikun)

threading.Thread(target=screendraw_thread).start()
