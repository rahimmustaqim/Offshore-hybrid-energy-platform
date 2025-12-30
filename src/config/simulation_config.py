class SimulationConfig:
    def __init__(self):
        self.dt = 0.1          # time step [s]
        self.t_end = 100.0     # simulation duration [s]

        # Environmental conditions
        self.wind_speed = 12.0     # m/s
        self.wave_height = 2.0     # m
        self.wave_period = 8.0     # s

        # Platform properties
        self.mass = 1.5e6          # kg
        self.damping = 2.0e4
