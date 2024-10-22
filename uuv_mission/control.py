class PDController:
    
    def __init__(self, K_P: float, K_D: float):
        #initalising the controller with the proportional and derivative gains
        self.K_P = K_P
        self.K_D = K_D
        self.previous_error = 0

    def compute_action(self, reference: float, output: float) -> float:
        error = reference - output
        # euler backward approximation of the derivative
        derivative = error - self.previous_error
        #implementing the proportional and derivate gains to compute the action
        action = self.K_P * error + self.K_D * derivative
        #updating the previous error to be used for the next iteration
        self.previous_error = error
        return action