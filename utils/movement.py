import pyautogui
import time
def enter_gobball_dungeon():
    pyautogui.moveTo(1174,338)
    time.sleep(.2)
    pyautogui.keyDown('shift')
    time.sleep(.2)
    pyautogui.click(1174,338)
    time.sleep(.2)
    pyautogui.keyUp('shift')
    pyautogui.click(693, 587)

def locate_bouftou():
    pic = pyautogui.screenshot(region=(430,278,1100,600))
    width, height = pic.size
    print("looking for bouftous")
    for x in range (0, width, 20):
        for y in range (0, height, 20):
            r,g,b = pic.getpixel((x,y))
            if r == 252 and g == 235 and b == 196:
                print('bouftou located in', x+430, y+278)
                return (x+430, y+278)