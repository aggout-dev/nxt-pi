import time
from script.script import Script


class Steer(Script):
    def do_execute(self, params):
        angle = params['angle']
        direction = params['dir']

        if direction == 'right':
            self.rolo.steer_right(angle)
            time.sleep(2)
            self.rolo.steer_left(angle)
        else:
            self.rolo.steer_left(angle)
            time.sleep(2)
            self.rolo.steer_right(angle)
