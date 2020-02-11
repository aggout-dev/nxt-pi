import time
from script.script import Script


class Steer(Script):
    def do_execute(self, params):
        angle = params['angle']
        direction = params['dir']

        if direction == 'right':
            self.rolo.drive()
            time.sleep(2)
            self.rolo.drive_left(50)
            time.sleep(2)
            self.rolo.halt()
        else:
            self.rolo.drive()
            time.sleep(2)
            self.rolo.drive_right(50)
            time.sleep(2)
            self.rolo.halt()
