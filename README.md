# Fuck School

## 介绍

Fuck School 是一个基于 Python 的工具，用于在学校的信息技术课堂上对电脑进行恶搞操作。

本程序仅适用于 Windows 操作系统。

## 工作方式

1. 通过 `update.py`（更新程序） 根据 `fucks` 文件夹，自动替换 `model.py`（界面程序），生成 `main.py`（最终程序）。
2. 运行 `main.py`，选择恶搞文件，等待完成。
3. 导出至自启动文件夹：`C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\fuck_school.pyw'`。
4. 不会自动运行该自启动文件，需要手动运行，在弹出的窗口点击确定即可。

**警告：** 仅仅为了玩梗。请不要真的运行此程序，后果自负。

**警告：** 如果不小心运行，请在弹出的窗口按下 `W` 退出。并重新打开 `main.py`，全部选择禁用更新。

## 恶搞文件语法

恶搞文件全部使用Python编写。每个恶搞文件需要配合 `txt` 格式的说明文件。

一些占位符会在运行时动态替换：
- `{username}`：第一步选择的用户名。
- `{filename}`：文件名（不带扩展名）。

**注意：** 最终，这些恶搞文件会被添加在一起，请保证前后有足够的空行。保证无限循环在一个线程内运行，否则可能会阻塞导致部分恶搞文件无法正常运行。

## 帮助文件语法

帮助文件和恶搞文件在同一目录。扩展名需要为 `txt`。

文字样式：
- `【文字】`：标题。
- `“文字”`：名称，例如文件名。
- `文字`：普通文本。

占位符：
- `{filename}`：文件名（不带扩展名）。
- `*`：替换并显示为 `※`。

## 关于

**重要的事情再说一遍：** 仅仅为了玩梗。请不要真的运行此程序，后果自负。

本软件按 MIT 协议开源。
