import time
from script.script import Script


class Steer(Script):
    def do_execute(self, params):
        left_speed = params['left_speed']
        right_speed = params['right_speed']

        self.rolo.drive(left_speed, right_speed)
        time.sleep(2)
        self.rolo.halt()
