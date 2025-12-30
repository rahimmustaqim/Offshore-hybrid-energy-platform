class PlatformDynamics:
    def __init__(self, mass, damping):
        self.mass = mass
        self.damping = damping
        self.velocity = 0.0
        self.position = 0.0

    def update(self, force, dt):
        acceleration = (force - self.damping * self.velocity) / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
