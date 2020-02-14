import time
from script.script import Script


class Steer(Script):
    def do_execute(self, params):
        min_speed = params['min_speed']
        direction = params['dir']

        _method = None
        if direction == 'right':
            _method = self.rolo.drive_right
        else:
            _method = self.rolo.drive_left

        self.rolo.drive()
        time.sleep(2)
        _method(min_speed)
        time.sleep(2)
        self.rolo.halt()
