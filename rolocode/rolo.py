DEFAULT_POWER = 100

class Rolo:

    def __init__(self, brick_controller):
        assert brick_controller is not None
        self.brick_controller = brick_controller
        self.wheels = [brick_controller.motor_b, brick_controller.motor_c]
        self.steering = brick_controller.motor_a

    def drive(self, power=DEFAULT_POWER):
        for motor in self.wheels:
            motor.run(power=power)

    def turn_wheels(self, angle, power=DEFAULT_POWER):
        for motor in self.wheels:
            motor.turn(power, tacho_units=angle)

    def steer_right(self, angle):
        self.steering.turn(DEFAULT_POWER, angle)

    def steer_left(self, angle):
        self.steering.turn(DEFAULT_POWER, -angle)

    def halt(self):
        for motor in self.wheels:
            motor.idle()

    def disconnect(self):
        if self.is_connected():
            self.brick_controller.sock.close()

    def is_connected(self):
        self.brick_controller.sock is not None
