DEFAULT_POWER = 100


class Rolo:

    def __init__(self, brick_controller):
        assert brick_controller is not None
        self.brick_controller = brick_controller
        self.wheels = [brick_controller.motor_b, brick_controller.motor_c]
        self.steering = brick_controller.motor_a

    def drive(self, power=DEFAULT_POWER):
        print(f'drive {power}')
        for motor in self.wheels:
            motor.run(power=power)

    def turn_wheels(self, angle, power=DEFAULT_POWER):
        print(f'turn_wheels {angle}, {power}')
        for motor in self.wheels:
            motor.turn(power, tacho_units=angle)

    def steer_right(self, angle):
        print(f'steer_right {angle}')
        self.steering.turn(DEFAULT_POWER, angle)

    def steer_left(self, angle):
        print(f'steer_left {angle}')
        self.steering.turn(-DEFAULT_POWER, angle)

    def halt(self):
        print(f'halt')
        for motor in self.wheels:
            motor.idle()

    def disconnect(self):
        print(f'disconnect')
        if self.is_connected():
            self.brick_controller.sock().close()

    def is_connected(self):
        print(f'is_connected')
        return self.brick_controller.sock() is not None
