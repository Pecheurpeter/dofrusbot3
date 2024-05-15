import pyautogui
import time

def start_fight(bouftou_location):
    pyautogui.moveTo(bouftou_location)
    time.sleep(.2)
    pyautogui.keyDown('shift')
    pyautogui.click(bouftou_location)
    time.sleep(.2)
    pyautogui.keyUp('shift')
    return True


