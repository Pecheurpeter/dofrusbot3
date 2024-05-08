from pyautogui import *
import pyautogui
import keyboard
import time
import combat
import attack
from donjon_bouf import attack_bouftou

def fight():
    while keyboard.is_pressed('k')==False:
        time.sleep(2)
        if combat.scan_map() == False:
            attack_bouftou()
            time.sleep(5)
            attack.get_ready()
        if combat.scan_map() == True:
            if attack.is_my_turn():
                if attack.check_spell_cast(attack.tremblement_pos) == "tremblement not cast" and attack.check_spell_cast(attack.vent_empoi_pos) == "vent empoi not cast" and attack.check_spell_cast(attack.puissance_sylv_pos) == "puissance sylv not cast":
                    attack.cast_combo_fourbe()
    

def room_one():
    while combat.scan_map() == False:
        attack_bouftou()
    time.sleep(4)
    attack.get_ready()
    if attack.is_my_turn():
        

#etat 1
#check si on est en combat 
#non : cherche un groupe
#oui : joue

#etat 2
#en combat : 
#est-ce mon tour ?
#oui : joue
# joue : passe, lance combo, (déplace)
#check portée : si portée: lance combo, sinon passe ou déplace
# passe si pas la portée 
#non ; fait rien
#le combat est fini ?
#oui : repart sur etat 1
#non : repart sur etat 2

