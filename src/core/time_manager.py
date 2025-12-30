class TimeManager:
    def __init__(self, dt, t_end):
        self.dt = dt
        self.t = 0.0
        self.t_end = t_end

    def advance(self):
        self.t += self.dt

    def is_finished(self):
        return self.t >= self.t_end
