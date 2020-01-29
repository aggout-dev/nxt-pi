import time
from script.abstract_script import Script


class Drive(Script):
    def do_execute(self, params):
        power = params['power']
        secs = params['time']

        self.rolo.drive(power)
        time.sleep(secs)
        self.rolo.halt()
