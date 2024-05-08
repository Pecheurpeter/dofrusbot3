from pyautogui import *
import pyautogui
import time
import keyboard

# combat state :
# 1 en combat
# si state 1 alors check state 2 : placement
# si state 2 alors check state 3 : player_turn
# si state 2 alors check state 4 : other_player_turn
# (si state 3 alors state 4 invalide)

def scan_map():
    time.sleep(2)
    combat_squares = 0
    pic = pyautogui.screenshot(region=(430,108,1100,700))
    width, height = pic.size
    print("scanning map...")
    for x in range (0,width,50):
        for y in range (0, height, 50):
            r,g,b = pic.getpixel((x,y))
            if (r, g, b) == (199, 203, 123):
                combat_squares += 1
                print('bright square located', x+430,y+108)
            elif (r, g, b) == (189, 193, 117):
                combat_squares+=1
                print('dark square located', x+430,y+108)
    if (combat_squares > 50 ):
        print("player is in combat:", combat_squares, " combat squares are present in this map")
        return True
    else:
        print("player is not in combat", combat_squares, " combat squares are present in this map")
        return False

# state 2 : placement # se déclenche que si state 1 est validé 

blue_color_code = (0, 0, 255)
red_color_code = (255, 0, 0)

def get_squares(color):
        squares = []
        pic = pyautogui.screenshot(region=(430,108,1100,700))
        width, height = pic.size
        print("scanning combat map...")
        x = 0
        while x < width:
            y = 0
            while y < height:
                r,g,b = pic.getpixel((x,y))
                if (r, g, b) == color:
                    square_x = (x+430)
                    square_y = (y+108)
                    square = pyautogui.position(square_x, square_y)
                    squares.append(square)
                    print("square", square)
                    y+=40
                    x+=50
                y+=1
            x+=1
        if len(squares) > 1:
            print(len(squares), "squares found in map. Player is in combat state 2 : placement")
            return squares
        else:
            print("can't find squares, player is not in combat state 2 (placement)")
            return None

# (400x200)