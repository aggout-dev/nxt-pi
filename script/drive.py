import time
from script.script import Script


class Drive(Script):
    def do_execute(self, params):
        power = params['power']
        secs = params['time']

        self.rolo.drive_straight(power)
        time.sleep(secs)
        self.rolo.halt()
