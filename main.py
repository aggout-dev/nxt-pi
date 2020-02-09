#!/usr/bin/env python3

from script.drive import Drive
from script.steer import Steer
from rolocode.rolo import Rolo
from nxt_main.nxt_brick import NXTBrickController
import os
import time
import sys

'''
Added this conditional import to be able to still run the scripts when there's actually no
NXT brick connected. You can set the shell environment variable MOCK_NXT to whatever value before running main
to force mocking the NXT brick.
'''
if os.environ.get('MOCK_NXT') is None:
    import nxt.bluesock as bluesock
else:
    import nxt_mock.bluesock as bluesock

address = '00:16:53:08:09:1F'


class Main:

    def __init__(self, rolo):
        self.drive_script = Drive(rolo)
        self.steer_script = Steer(rolo)

    def test_drive1(self):
        params = {'power': 100, 'time': 3}
        self.drive_script.execute(params)

    def test_drive2(self):
        params = {'power': 50, 'time': 2}
        self.drive_script.execute(params)

    def test_steer1(self):
        params = {'angle': 30, 'dir': 'right'}
        self.steer_script.execute(params)

    def test_steer2(self):
        params = {'angle': 30, 'dir': 'left'}
        self.steer_script.execute(params)


if __name__ == '__main__':
    brick_connection = None
    rolo = None
    try:
        brick_connection = bluesock.BlueSock(address).connect()
        print(str(brick_connection))
        rolo = Rolo(NXTBrickController(brick_connection))
        m = Main(rolo)
        m.test_drive1()
        time.sleep(3)
        m.test_drive2()
        time.sleep(3)
        m.test_steer1()
        time.sleep(3)
        m.test_steer2()
    except IOError:
        print("Error while running tests:")
        print(str(sys.exc_info()[1]))
    finally:
        if rolo is not None:
            print("disconnecting")
            rolo.disconnect()
