import sys
from abc import ABCMeta, abstractmethod


class Script(metaclass=ABCMeta):
    @abstractmethod
    def do_execute(self, params):
        pass

    def __init__(self, rolo):
        self.rolo = rolo
        self.params = None

    def execute(self, params={}):
        try:
            self.params = params
            self.do_execute(params)
        except IOError:
            print("Error while running test:")
            print(str(sys.exc_info()[1]))
