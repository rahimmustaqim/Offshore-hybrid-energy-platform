import numpy as np

class PlatformDynamics6DOF:
    def __init__(self, mass, inertia, damping_lin, damping_rot):
        # State vectors
        self.position = np.zeros(6)   # [x y z roll pitch yaw]
        self.velocity = np.zeros(6)
        self.acceleration = np.zeros(6)

        # Mass matrix (translation + rotation)
        self.M = np.diag([
            mass, mass, mass,          # surge, sway, heave (kg)
            inertia, inertia, inertia  # roll, pitch, yaw (kg m^2)
        ])

        # Linear damping matrix
        self.C = np.diag([
            damping_lin, damping_lin, damping_lin,
            damping_rot, damping_rot, damping_rot
        ])

        # Hydrostatic restoring matrix
        self.K = np.zeros((6, 6))
        self.K[2, 2] = 1e5   # heave stiffness
        self.K[3, 3] = 5e6   # roll stiff
