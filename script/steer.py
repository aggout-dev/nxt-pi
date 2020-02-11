import time
from script.script import Script


class Steer(Script):
    def do_execute(self, params):
        min_speed = params['min_speed']
        direction = params['dir']

        if direction == 'right':
            self.rolo.drive()
            time.sleep(2)
            self.rolo.drive_left(min_speed)
            time.sleep(2)
            self.rolo.halt()
        else:
            self.rolo.drive()
            time.sleep(2)
            self.rolo.drive_right(min_speed)
            time.sleep(2)
            self.rolo.halt()
