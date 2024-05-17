import time
from utils import placement, movement, combat, attack

def room_one():
    if placement.placement(placement.red_square_room_one):
        combat.start_fight()
    time.sleep(4)
    for _ in range (3):
        movement.move_forward()
        time.sleep(2)
        combat.pass_tour()
    attack.cast_tremblement()
    combat.pass_tour()

def room_two():
    if placement.placement(placement.red_square_room_two):
        combat.start_fight()
    time.sleep(4)
    for _ in range(3):
        movement.move_forward()
        time.sleep(2)
        combat.pass_tour()
    attack.cast_tremblement()
    combat.pass_tour()

def room_three():
    if placement.placement(placement.red_square_room_three):
        combat.start_fight()
    time.sleep(4)
    attack.cast_tremblement()
    combat.pass_tour()