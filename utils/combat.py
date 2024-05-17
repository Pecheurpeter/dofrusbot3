import pyautogui
import time

def enter_combat(bouftou_location):
    pyautogui.moveTo(bouftou_location)
    time.sleep(.2)
    pyautogui.keyDown('shift')
    pyautogui.click(bouftou_location)
    time.sleep(.2)
    pyautogui.keyUp('shift')
    return True

def start_fight():
    pyautogui.press('f1')

def is_my_turn():
    pic = pyautogui.screenshot()
    r,g,b = pic.getpixel((1106,931)) #y+30
    if r == 255 and g == 102 and b == 0:
        print("it's my turn ! play !")
        return True
    elif r == 81 and g == 74 and b == 60:
        print("it's another players turn")
        return False
    
def pass_tour():
    my_turn = is_my_turn()
    if my_turn:
        print("it's my turn.")
        pyautogui.press('f1')
        print("turn passed")

def locate_perso_tour():
    player_color = (195, 73, 49)
    my_turn = is_my_turn()
    if my_turn:
        pic = pyautogui.screenshot(region=(929, 748, 650, 100))
        width, height = pic.size
        x = 0
        while x < width:
            y = 0
            while y < height:
                r,g,b = pic.getpixel((x,y))
                if (r,g,b) == player_color:
                    player_icon_pos = (x+929,y+748)
                y+=1
            x+=1
        print("player combat icon is in ", player_icon_pos)
    return (player_icon_pos)