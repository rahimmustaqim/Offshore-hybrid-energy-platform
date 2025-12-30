import math

class WaveSolver:
    def __init__(self, H, T):
        self.H = H
        self.T = T

    def compute_force(self, time):
        omega = 2 * math.pi / self.T
        force = self.H * math.sin(omega * time) * 1e4
        return force
