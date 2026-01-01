import numpy as np

class WindSolver:
    def __init__(self, wind_speed):
        self.wind_speed = wind_speed

    def thrust(self, rho, area, Ct):
        return 0.5 * rho * area * Ct * self.wind_speed**2


