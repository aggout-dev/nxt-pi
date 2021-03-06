#!/usr/bin/env python3

from script.drive import Drive
from script.steer import Steer
from script.rotate import Rotate
from script.combine import *
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
        self.rotate_script = Rotate(rolo)
        self.combine_script = Combine(rolo)

    def test_drive1(self):
        params = {'power': 100, 'time': 2}
        self.drive_script.execute(params)

    def test_drive2(self):
        params = {'power': -100, 'time': 2}
        self.drive_script.execute(params)

    def test_drive3(self):
        params = {'power': 75, 'time': 3}
        self.drive_script.execute(params)

    def test_drive4(self):
        params = {'power': -75, 'time': 3}
        self.drive_script.execute(params)

    def test_steer1(self):
        params = {'left_speed': 75, 'right_speed': 100}
        self.steer_script.execute(params)

    def test_steer2(self):
        params = {'left_speed': -75, 'right_speed': -100}
        self.steer_script.execute(params)

    def test_steer3(self):
        params = {'left_speed': 100, 'right_speed': 75}
        self.steer_script.execute(params)

    def test_steer4(self):
        params = {'left_speed': -100, 'right_speed': -75}
        self.steer_script.execute(params)

    def test_rotate1(self):
        params = {'power': 75, 'dir': 'left', 'time': 2}
        self.rotate_script.execute(params)

    def test_rotate2(self):
        params = {'power': 75, 'dir': 'right', 'time': 2}
        self.rotate_script.execute(params)

    def test_rotate3(self):
        params = {'power': 120, 'dir': 'left', 'time': 1}
        self.rotate_script.execute(params)

    def test_rotate4(self):
        params = {'power': 120, 'dir': 'right', 'time': 1}
        self.rotate_script.execute(params)

    def combine1(self):
        straight1 = CParams(100, 100, 2)
        straight2 = CParams(75, 75, 2)
        turn1 = CParams(75, 100, 2)
        turn2 = CParams(120, 80, 2)

        params = {'straight1': straight1, 'straight2': straight2, 'turn1': turn1, 'turn2': turn2}
        self.combine_script.execute(params)


def unit_tests(_main):
    _main.test_drive1()
    time.sleep(t_sleep)
    _main.test_drive2()
    time.sleep(t_sleep)
    _main.test_drive3()
    time.sleep(t_sleep)
    _main.test_drive4()
    time.sleep(t_sleep)
    _main.test_steer1()
    time.sleep(t_sleep)
    _main.test_steer2()
    time.sleep(t_sleep)
    _main.test_steer3()
    time.sleep(t_sleep)
    _main.test_steer4()
    time.sleep(t_sleep)
    _main.test_rotate1()
    time.sleep(t_sleep)
    _main.test_rotate2()
    time.sleep(t_sleep)
    _main.test_rotate3()
    time.sleep(t_sleep)
    _main.test_rotate4()


t_sleep = 1


def combine_tests(_main):
    _main.combine1()


if __name__ == '__main__':
    brick_connection = None
    rolo = None
    try:
        brick_connection = bluesock.BlueSock(address).connect()
        print(str(brick_connection))
        rolo = Rolo(NXTBrickController(brick_connection))
        m = Main(rolo)
        # unit_tests(m)
        combine_tests(m)

    except IOError:
        print("Error while running tests:")
        print(str(sys.exc_info()[1]))
    finally:
        if rolo is not None:
            print("disconnecting")
            rolo.disconnect()
