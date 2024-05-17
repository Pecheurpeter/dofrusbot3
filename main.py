import time
import rooms
from utils import movement, combat, map, placement

def main():
    while True:
        movement.enter_gobball_dungeon()
        bouftou_pos = movement.locate_bouftou()
        if bouftou_pos:
            combat.enter_combat()
        if map.scan_map():
            rooms.room_one()
            rooms.room_two()
            rooms.room_three()



