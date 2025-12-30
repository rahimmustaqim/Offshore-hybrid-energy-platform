import numpy as np

class WindSolver:
    def __init__(self, wind_speed):
        self.wind_speed = wind_speed

    def compute_force(self):
        rho = 1.225
        area = 200.0
        Ct = 0.8
        thrust = 0.5 * rho * Ct * area * self.wind_speed**2

        force = np.zeros(6)
        force[0] = thrust      # surge
        force[4] = thrust * 0.02  # pitch moment (simplified)

        return force
