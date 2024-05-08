from pyautogui import *
import pyautogui
import time
import keyboard

red_squares_room_one = [(550,600), (600, 630), (550,700), (600, 730), (700, 780), (750,800), (890,780), (930,800)]
red_squares_room_two = []
red_squares_room_three=[(800,580)]
# red_squares_room_four=[()]any pos work
red_squares_room_five=[(1000, 580)]
red_squares_room_six=[(1265,394),(1300,420)]
red_squares_room_seven=[(1300,370)]
red_squares_room_eight=[(620, 625),(620, 675),(800,770),(900,770)]
red_squares_room_nine=[(710,720),(660,370),(1300,370),(1300,700)]
# red_squares_room_ten=[]any

def room_one():
    pyautogui.click(red_squares_room_one[1])

x = 520
y = 680
red_square = (x,y)

while len(red_squares_room_two) <= 8:
    red_square = (x,y)
    red_squares_room_two.append(red_square)
    x+=45
    y+=25

def room_two():
    pyautogui.click(red_squares_room_two[3])

def placement(squares_room):
    if len(squares_room) > 1 :
        for square_room in squares_room:
            pyautogui.move(square_room)
            pyautogui.click(squares_room)
            time.sleep(1)
        pyautogui.press('f1')
    else:
        pyautogui.move(squares_room)
        time.sleep(.5)
        pyautogui.click(squares_room)
        time.sleep(.5)

