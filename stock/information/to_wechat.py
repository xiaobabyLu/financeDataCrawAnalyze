# 导入模块
from wxpy import *
import pyautogui
import pyperclip
import time
from wxauto import WeChat


'''
参考：https://wxpy.readthedocs.io/zh/latest/
    https://www.jianshu.com/p/ac38412330aa
    目前是需要你在电脑上登录微信客户端才能实现这种功能，还有一种就是可以通过扫码登录，扫码很难做到定时本次暂时不采用
'''
# 初始化机器人，扫码登陆
# bot = Bot()




def get_msg():
    """想发的消息，每条消息空格分开"""
    contents = "晚上你吃啥 啥，不知道 那听我安排吧 晚上回来先歇会 可以先吃个火龙果，我已经拿出来了 等会会有外卖给你打电话 " \
               "拿到外卖再开始做饭都不晚 什么外卖你别问 这次让我卖个关子可行"
    return contents.split(" ")


def send(msg):
    # 复制需要发送的内容到粘贴板
    pyperclip.copy(msg)
    # 模拟键盘 ctrl + v 粘贴内容
    pyautogui.hotkey('ctrl', 'v')
    # 发送消息
    pyautogui.press('enter')


def send_msg(friend):
    # Ctrl + alt + w 打开微信
    pyautogui.hotkey('ctrl', 'alt', 'w')
    # 搜索好友
    pyautogui.hotkey('ctrl', 'f')
    # 复制好友昵称到粘贴板
    pyperclip.copy(friend)
    # 模拟键盘 ctrl + v 粘贴
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # 回车进入好友消息界面
    pyautogui.press('enter')
    # 一条一条发送消息
    for msg in get_msg():
        send(msg)
        # 每条消息间隔 2 秒
        time.sleep(2)


if __name__ == '__main__':
    friend_name = 'z'
    send_msg(friend_name)