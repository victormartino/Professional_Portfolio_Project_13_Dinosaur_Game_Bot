import pyautogui
import webbrowser
import time
import win32api, win32con
import keyboard
import numpy as np

VK_UP = 0x26
TARGET_R_VALUE = 83
URL = 'https://elgoog.im/dinosaur-game/'


def jump():
    win32api.keybd_event(VK_UP, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(VK_UP, 0, win32con.KEYEVENTF_KEYUP, 0)


webbrowser.open(URL)
time.sleep(2)
pyautogui.press('space')
time.sleep(3)

while True:
    if np.any(np.array(pyautogui.screenshot(region=(233, 735, 250, 110)))[:, :, 0] == TARGET_R_VALUE):
        jump()

    if keyboard.is_pressed('q'):
        break
