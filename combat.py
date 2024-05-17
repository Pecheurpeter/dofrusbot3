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