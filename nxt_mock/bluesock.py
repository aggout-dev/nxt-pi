import nxt_mock.brick


class BlueSock:
    def __init__(self, address):
        pass

    def connect(self):
        print('mock BlueSock.connect()')
        return nxt_mock.brick.Brick()
