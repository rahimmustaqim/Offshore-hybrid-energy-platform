import numpy as np

class WindTurbine:
    def __init__(self, hub_height=100.0, rotor_area=200.0, Ct=0.8):
        self.hub_height = hub_height
        self.rotor_area = rotor_area
        self.Ct = Ct
        self.rho = 1.225

    def compute_loads(self, wind_speed):
        thrust = 0.5 * self.rho * self.Ct * self.rotor_area * wind_speed**2

        force = np.zeros(6)
        force[0] = thrust                     # surge force
        force[4] = thrust * self.hub_height   # pitch moment

        return force
