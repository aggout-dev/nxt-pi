import os

if os.environ.get('MOCK_NXT') is None:
    from nxt.motor import *
else:
    from nxt_mock.motor import *


class NXTBrickController:
    def __init__(self, brick):
        self.brick = brick
        self.motor_a = Motor(self.brick, PORT_A)
        self.motor_b = Motor(self.brick, PORT_B)
        self.motor_c = Motor(self.brick, PORT_C)

    def sock():
        return self.brick.sock
