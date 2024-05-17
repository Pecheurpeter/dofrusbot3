import pyautogui
import time

#y +30 par rapport aux screens
red_square_room_one = [(570,630), (615, 650)]
red_square_room_two = [(520, 700), (570, 730), (660, 780)]
red_square_room_three = [(790, 600), (740, 630), (840, 630)]
red_square_room_four = [(890, 530)] #does not matter
red_square_room_five = [(990, 610)]
red_square_room_six = [(1280, 420), (1320, 450)]
red_square_room_seven = [(1330, 400)]
red_square_room_eight = [(550, 680)]
red_square_room_nine = [(700, 750), (650, 380), (1330, 380), (1330, 730)]
red_square_room_ten = [(800, 620), (850, 630), (890, 650)]

def check_square(square):
    pic = pyautogui.screenshot(region=(square[0], square[1],10,10))
    width, height = pic.size
    correct_square = (0,0)
    print("check if square is free")
    red_pixel = 0
    x = 0
    while x < width:
        y = 0
        while y < height:
            r,g,b = pic.getpixel((x,y))
            if r == 255 and g == 0 and b == 0:
                red_pixel +=1
                print(red_pixel)
            y+=1
        x+=1
    if red_pixel > 8:
        print(red_pixel,"pixels located on red square : seems free")
        correct_square = (x+square[0], y+square[1])
        pyautogui.moveTo(correct_square)
        pyautogui.click(correct_square)
    elif red_pixel < 1 :
        print(red_pixel, "red pixels located on square, not a red square")
    elif red_pixel > 2 and red_pixel < 7:
        print(red_pixel, "seem like a player is located here : ", x,y)
        return True

def placement(room):
    for square in room:
        check_square(square)

