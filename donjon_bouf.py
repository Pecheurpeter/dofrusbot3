from pyautogui import *
import pyautogui
import time
import keyboard

def enter_dungeon():
    time.sleep(2)
    pyautogui.keyDown('shift')
    time.sleep(.2)
    pyautogui.click(1174,338)
    time.sleep(.2)
    pyautogui.keyUp('shift')
    time.sleep(.2)
    pyautogui.click(693, 587)
    

# boufton_noir_rgb = (100, 84 70)
# boufton_blanc = (252, 235, 196)

# regarder toute les 5 sec si le player est en combat (avec bouton pret)
def check_if_fight_has_started():
    while keyboard.is_pressed('k') == False:
        time.sleep(5)
        try:
            pyautogui.locateOnScreen('ready_button.png',region=(1450,750,200,100), confidence=.8)
            print("player is in combat")
            return True
        except pyautogui.ImageNotFoundException:
            time.sleep(.5)
            print("not in combat")
            return False

def find_my_pos():
    while keyboard.is_pressed('k') == False:
        time.sleep(1)
        try:
            position = pyautogui.locateOnScreen('mandra-combat.png', region=(430, 108, 1100, 700), grayscale=True, confidence=.8)
            print("mandra is located in ", position.left, position.top)
            return position.left, position.top
        except pyautogui.ImageNotFoundException:
            print("can't find player")


def attack_bouftou():
    pic = pyautogui.screenshot(region=(430,278,1100,600))
    width, height = pic.size
    print("looking for mob")
    for x in range (0,width,20):
        for y in range (0, height, 20):
            r,g,b = pic.getpixel((x,y))
            if r == 252 and g == 235 and b == 196:
                print('boufton blanc located')
                pyautogui.keyDown('shift')
                pyautogui.click(x+430, y+278)
                time.sleep(.2)
                pyautogui.keyUp('shift')
                time.sleep(.05)
                return True

bouftous_pos=[]
def locate_bouftou():
    pic = pyautogui.screenshot(region=(430,250,1100,600))
    width, height = pic.size
    print("looking for bouftous while in combat")
    x = 0
    while x < width:
        y = 0
        while y < height:
            r,g,b = pic.getpixel((x,y))
            if r == 252 and g == 235 and b == 196:
                bouftou = (x+430, y+250)
                bouftous_pos.append(bouftou)
                print('boufton blanc/bouftou located in : ', x+430, y+250)
                x+=20
                y+=20
            elif r == 100 and g == 84 and b == 70:
                boufton_noir = (x+430, y+250)
                bouftous_pos.append(boufton_noir)
                print("boufton noir located in ", x+430, y+250)
                x+=50
                y+=25
            y+=1
        x+=1
    return bouftous_pos

def locate_mandra():
    pic = pyautogui.screenshot(region=(430,278,1100,600))
    width, height = pic.size
    print("looking for mandra")
    x = 0
    while x < width:
        y = 0
        while y < height:
            r,g,b = pic.getpixel((x,y))
            if r == 195 and g == 73 and b == 49:
                mandra_pos = (x+430, y+278)
                print('Mandragova located in : ', x+430, y+278)
                return mandra_pos
            y+=1
        x+=1

def move_forward():
    mandra_pos = locate_mandra()
    pyautogui.moveTo(mandra_pos[0]+150, mandra_pos[1])
    time.sleep(.5)
    pyautogui.click(mandra_pos[0]+150, mandra_pos[1])
    time.sleep(1.5)

def check_po():
    locate_bouftou()
    mandra_x = locate_mandra()[0]
    mandra_y = locate_mandra()[1]
    for bouftou in bouftous_pos:
        print("x difference : ", mandra_x-bouftou[0])
        print("y difference : ", mandra_y-bouftou[1])
        if mandra_x-bouftou[0] < 400 and mandra_y-bouftou[1] < (200): #valeur absolue
            print("combo is in po")

def locate_perso_tour(): # a optimiser
    try:
        location = pyautogui.locateOnScreen('sadi-tour.png', region=(929, 748, 650, 100), confidence=.9)
        print("it's mandragova's turn")
        return location
        
    except pyautogui.ImageNotFoundException:
        print("It's another player's turn")
        time.sleep(.5)
        return None

def pass_tour(sec_to_wait, number_of_turn):
    location = locate_perso_tour()
    if location:
        for _ in range (number_of_turn):
            print("it's mandragova's turn")
            pyautogui.press('f1')
            print("tour", _+1 ,"passed")
            time.sleep(sec_to_wait)

def check_spell_castable():
    try:
        pyautogui.locateOnScreen('tremblement.png',region=(1250, 950, 50, 50),grayscale=True, confidence=.8)
        pyautogui.locateOnScreen('vent-empoisone.png',region=(1300, 950, 50, 50),grayscale=True, confidence=.8)
        pyautogui.locateOnScreen('puissance-sylvestre.png',region=(1350, 950, 50, 50),grayscale=True, confidence=.8)
        return True
    except pyautogui.ImageNotFoundException:
        print("combo not fully done")
        return False


        
            
def check_end_fight_tab():
    for _ in range (10):
        try:
            pyautogui.locateOnScreen('end_fight_tab.png', region=(500, 600, 1000, 200), grayscale=True, confidence=.5)
            print('end fight tab found')
            print('combat ended.')
            time.sleep(.5)
            return True
        except pyautogui.ImageNotFoundException:
            print("end fight tab not found")
            time.sleep(.5)
            return False


def start_combo(sec_to_wait):
    while keyboard.is_pressed('k') == False:
        attack_bouftou()
        if check_if_fight_has_started():
            time.sleep(5)
            get_ready()
            pass_tour(sec_to_wait, 4)
            fight()
            if locate_perso_tour():
                fight()


def fight_no_puissance_sylv():
    location = locate_perso_tour()
    if locate_perso_tour():
        keyboard.press_and_release('&')
        time.sleep(.5)
        pyautogui.click(location)
        print("tremblement lancé")
        time.sleep(.5)
        keyboard.press_and_release('é')
        time.sleep(.5)
        pyautogui.click(location)
        print("vent empoisonné lancé")
        time.sleep(.5)
        keyboard.press_and_release('f1')
        print("tour done")

def fight_tremblement():
    location = locate_perso_tour()
    if location:
        time.sleep(.5)
        keyboard.press_and_release('&')
        time.sleep(1)
        keyboard.press_and_release('&')
        print("tremblement pressed")
        time.sleep(3)
        pyautogui.click(location)
        print("tremblement lancé")
        time.sleep(.5)
        keyboard.press_and_release('f1')
        print("tour done")

def fight_tremblement_no_pass():
    location = locate_perso_tour()
    if location:
        time.sleep(.5)
        keyboard.press_and_release('&')
        time.sleep(1)
        keyboard.press_and_release('&')
        print("tremblement pressed")
        time.sleep(3)
        pyautogui.click(location)
        print("tremblement lancé")

def fight_first_room():
    attack_bouftou()
    pass_tour(16, 5)
    fight_tremblement()
    check_end_fight_tab()


def fight_room_two():
    attack_bouftou()
    get_ready()
    pass_tour(30, 6)
    fight_tremblement()
    fight()

def fight_room_three():
    attack_bouftou()
    time.sleep(3)
    pyautogui.moveTo(788, 555) # se placer pour avoir po
    time.sleep(1)
    pyautogui.click(788, 555) # se placer pour avoir po
    get_ready()
    fight()
    #ok


def fight_room_four():
    attack_bouftou()
    time.sleep(4)
    get_ready()
    time.sleep(3)
    fight()
    #ok

def fight_room_five():
    attack_bouftou()
    time.sleep(2)
    pyautogui.click(984, 559)
    get_ready()
    print("player ready, fight is starting")
    print("it's player's turn")
    pyautogui.moveTo(1027, 533)
    pyautogui.click(1027, 533)
    time.sleep(2.5)
    fight_tremblement_no_pass()
    time.sleep(2)
    pyautogui.moveTo(934, 592)
    time.sleep(.5)
    pyautogui.click(934, 592)
    time.sleep(2)
    fight() 
    # a re test

def fight_room_six():
    attack_bouftou()
    time.sleep(5)
    pyautogui.moveTo(1275, 359)
    time.sleep(.5)
    pyautogui.click(1275, 359)
    get_ready()
    time.sleep(2.5)
    fight()
    #ok

def fight_room_seven():
    attack_bouftou()
    time.sleep(5)
    pyautogui.moveTo(733, 687)
    time.sleep(.5)
    pyautogui.click(733, 687)
    get_ready()
    time.sleep(2.5)
    pyautogui.move(889, 609)
    time.sleep(.5)
    pyautogui.click(889, 609)
    time.sleep(1)
    pass_tour(30, 5)
    fight()
    # a retester (juste a attentre 5 tours au pire que les bouf se rapprochent)

def fight_room_eight():
    attack_bouftou()
    time.sleep(4)
    get_ready()
    pass_tour(28, 5)
    fight()
    # a re-test

def fight_room_nine():
    attack_bouftou()
    time.sleep(5)
    pyautogui.moveTo(695, 707)
    time.sleep(.5)
    pyautogui.click(695, 707)
    time.sleep(.5)
    get_ready()
    time.sleep(2.5)
    pyautogui.moveTo(788, 652)
    time.sleep(.5)
    pyautogui.click(788, 652)
    time.sleep(.5)
    fight()

#ok fix le lancé de sort quand deja lancé dans fight()

def fight_last_room():
    attack_bouftou()
    time.sleep(5)
    get_ready()
    fight()
    sec = 25
    for _ in range (4):
        time.sleep(sec)
        pyautogui.press('f1')    
        sec -=2
    pass_tour(5,1)
    fight()
    pass_tour(4,1)
    fight()
    while check_if_fight_has_started() == True:
        fight()
