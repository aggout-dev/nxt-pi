import time
from script.script import Script


class Rotate(Script):
    def do_execute(self, params):
        power = params['power']
        _dir = params['dir']
        secs = params['time']

        if _dir == 'right':
            self.rolo.rotate(power)
        else:
            self.rolo.rotate(-power)

        time.sleep(secs)
        self.rolo.halt()
