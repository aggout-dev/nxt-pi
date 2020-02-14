import time
from script.script import Script


class CParams:
    def __init__(self, power_l, power_r, duration):
        self.power_l = power_l
        self.power = power_l
        self.power_r = power_r
        self.duration = duration


class Combine(Script):
    def do_execute(self, params):
        straight1 = params['straight1']
        straight2 = params['straight2']
        turn1 = params['turn1']
        turn2 = params['turn2']

        self.rolo.drive_straight(straight1.power)
        time.sleep(straight1.duration)
        self.rolo.drive(turn1.power_l, turn1.power_r)
        time.sleep(turn1.duration)
        self.rolo.drive_straight(straight2.power)
        time.sleep(straight2.duration)
        self.rolo.drive(turn2.power_l, turn2.power_r)
        time.sleep(turn2.duration)
        self.rolo.halt()
