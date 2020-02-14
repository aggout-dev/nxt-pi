DEFAULT_POWER = 100


class Rolo:

    def __init__(self, brick_controller):
        assert brick_controller is not None
        self.brick_controller = brick_controller
        self.wheels = (brick_controller.motor_b, brick_controller.motor_c)

    def drive(self, power=DEFAULT_POWER):
        print(f'drive {power}')
        self.drive(power, power)

    def drive(self, power_left=DEFAULT_POWER, power_right=DEFAULT_POWER):
        print(f'drive {power_left}, {power_right}')
        self.wheels[0].run(power=power_left)
        self.wheels[1].run(power=power_right)

    def drive_left(self, power=DEFAULT_POWER):
        print(f'drive_left {power}')
        if power == 0:
            self.wheels[0].brake()
        else:
            self.wheels[0].run(power=power)

    def drive_right(self, power=DEFAULT_POWER):
        print(f'drive_right {power}')
        if power == 0:
            self.wheels[1].brake()
        else:
            self.wheels[1].run(power=power)

    def rotate(self, power=DEFAULT_POWER):
        print(f'rotate {power}')
        self.wheels[0].run(power)
        self.wheels[1].run(-power)

    def halt(self):
        print(f'halt')
        for motor in self.wheels:
            motor.brake()

    def disconnect(self):
        print(f'disconnect')
        if self.is_connected():
            self.brick_controller.sock().close()

    def is_connected(self):
        print(f'is_connected')
        return self.brick_controller.sock() is not None
