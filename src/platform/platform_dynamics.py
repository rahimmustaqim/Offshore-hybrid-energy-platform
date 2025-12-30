import numpy as np

class PlatformDynamics6DOF:
    def __init__(self, mass, damping):
        self.mass = mass

        # State vectors
        self.position = np.zeros(6)   # [x y z roll pitch yaw]
        self.velocity = np.zeros(6)
        self.acceleration = np.zeros(6)

        # Mass, damping, stiffness matrices
        self.M = np.eye(6) * mass
        self.C = np.eye(6) * damping
        self.K = np.eye(6) * 1e4   # hydrostatic restoring (simplified)

    def update(self, force, dt):
        # force: numpy array (6,)
        self.acceleration = np.linalg.solve(
            self.M,
            force - self.C @ self.velocity - self.K @ self.position
        )

        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
