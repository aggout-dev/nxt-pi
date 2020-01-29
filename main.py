#!/usr/bin/env python3

from script.drive import Drive
from script.steer import Steer


def test_drive1():
    params = {'power': 100, 'time': 3}
    Drive().execute(params)


def test_drive2():
    params = {'power': 50, 'time': 2}
    Drive().execute(params)


def test_steer1():
    params = {'angle': 30, 'dir': 'right'}
    Steer().execute(params)


def test_steer2():
    params = {'angle': 30, 'dir': 'left'}
    Steer().execute(params)


if __name__ == '__main__':
    test_drive1()
    test_drive2()
    test_steer1()
    test_steer2()
