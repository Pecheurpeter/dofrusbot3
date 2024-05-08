import keyboard
import pyautogui
import time
import mouseinfo

def print_cordinate():
    time.sleep(3)
    while keyboard.is_pressed('k') == False:
        print(pyautogui.position())
        time.sleep(3)
        
# print_cordinate()

pyautogui.displayMousePosition()