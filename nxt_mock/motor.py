PORT_A = 0x00
PORT_B = 0x01
PORT_C = 0x02
PORT_ALL = 0xFF


class Motor:
    def __init__(self, brick, port):
        pass

    def turn(self, power, angle):
        print(f'mock Motor.turn({power}, {angle})')

    def idle(self):
        print(f'mock Motor.idle()')

    def run(self, power):
        print(f'mock Motor.run({power})')
