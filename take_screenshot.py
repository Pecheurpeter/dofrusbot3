from pyautogui import *
import pyautogui
import time
import keyboard

def take_and_save_screenshot():
    region = pyautogui.screenshot(region=(430,108,1100,700))
    region.save(r"/var/www/html/dofus-bot/saved_image.png")
    return region