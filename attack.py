from pyautogui import *
import pyautogui
import time
import keyboard
from donjon_bouf import locate_perso_tour

tremblement_region = (1250, 950, 50, 50)
vent_empoi_region = (1300, 950, 50, 50)
puissance_sylv_region = (1350, 950, 50, 50)

def get_ready():
    time.sleep(1)
    pyautogui.press('f1')
    time.sleep(6)

def is_my_turn():
    pic = pyautogui.screenshot()
    r,g,b = pic.getpixel((1106,901))
    if r == 255 and g == 102 and b == 0:
        print("it's mandragova's turn ! play !")
        return True
    elif r == 81 and g == 74 and b == 60:
        print("it's another players turn")
        return False

tremblement_pos = (1274, 983)
vent_empoi_pos = (1338, 974)
puissance_sylv_pos = (1391, 967)


def check_spell_cast(spell_pos):
    pic = pyautogui.screenshot()
    r,g,b = pic.getpixel((spell_pos))
    if r == 176 and g == 42 and b == 42:
        print("tremblement not cast")
        return "tremblement not cast"
    elif r == 88 and g == 21 and b == 21:
        print("tremblement cast")
        return("tremblement cast")
    elif r == 106 and g == 101 and b == 73:
        print("vent empoi not cast")
        return("vent empoi not cast")
    elif r == 53 and g == 50 and b == 36:
        print("vent empoi cast")
        return("vent empoi cast")
    elif r == 170 and g == 135 and b == 26:
        print("puissance sylv not cast")
        return("puissance sylv not cast")
    elif r == 85 and g == 67 and b == 13:
        print("puissance sylv cast")
        return("puissance sylv cast")
    else:
        print("can't find spell")
        return("can't find spell")


def cast_tremblement():
    location = locate_perso_tour()
    keyboard.press_and_release('&')
    time.sleep(.5)
    pyautogui.click(location)
    print("tremblement lancé")
    time.sleep(.5)
    return location

def cast_vent_empoi():
    cast_tremblement()
    keyboard.press_and_release('é')
    time.sleep(.5)
    pyautogui.click(locate_perso_tour())
    print("vent empoisonné lancé")
    time.sleep(.5)
    keyboard.press_and_release('"')
    time.sleep(.5)
    pyautogui.click(locate_perso_tour())
    print("puissance sylv lancé")

def cast_combo_fourbe():
    cast_tremblement()
    cast_vent_empoi()
    keyboard.press_and_release('f1')
    print("tour done")