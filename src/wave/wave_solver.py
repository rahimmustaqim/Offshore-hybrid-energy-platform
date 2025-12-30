import numpy as np
import math

class WaveSolver:
    def __init__(self, H, T):
        self.H = H
        self.T = T

    def compute_force(self, time):
        omega = 2 * math.pi / self.T
        wave_force = self.H * math.sin(omega * time) * 1e4

        force = np.zeros(6)
        force[2] = wave_force     # heave
        force[3] = wave_force * 0.01  # roll moment

        return force
