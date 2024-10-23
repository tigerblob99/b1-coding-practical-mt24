class PDController:
    def __init__(self, kp, kd):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.previous_error = 0

    def compute(self, setpoint, measured_value,dt):
        # Calculate error
        error = setpoint - measured_value

        # Proportional term
        P = self.kp * error

        # Derivative term
        D = self.kd * (error - self.previous_error) / dt

        # Update previous error
        self.previous_error = error

        # Control output
        output = P + D
        return output

