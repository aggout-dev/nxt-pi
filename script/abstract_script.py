import sys
from script.rolo_instance import rolo
from abc import ABCMeta, abstractmethod


class Script(metaclass=ABCMeta):
    @abstractmethod
    def do_execute(self, params):
        pass

    def __init__(self):
        self.rolo = None
        self.params = None

    def execute(self, params={}):
        try:
            self.rolo = rolo()
            self.params = params
            self.do_execute(params)
            self.rolo.disconnect()
        except IOError:
            print("Error while running test:")
            print(str(sys.exc_info()[1]))
            if self.rolo is not None:
                self.rolo.disconnect()
