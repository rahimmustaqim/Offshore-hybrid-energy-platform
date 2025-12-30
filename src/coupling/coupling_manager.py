from core.time_manager import TimeManager
from wind.wind_solver import WindSolver
from wave.wave_solver import WaveSolver
from platform.platform_dynamics import PlatformDynamics6DOF
from solar.solar_model import SolarModel

class CouplingManager:
    def __init__(self, config):
        self.time = TimeManager(config.dt, config.t_end)
        self.wind = WindSolver(config.wind_speed)
        self.wave = WaveSolver(config.wave_height, config.wave_period)
        self.platform = PlatformDynamics6DOF(config.mass, config.damping)
        self.solar = SolarModel()

    def run(self):
        print("Simulation started")
        while not self.time.is_finished():
            wind_force = self.wind.compute_force()
            wave_force = self.wave.compute_force(self.time.t)

            total_force = wind_force + wave_force

            self.platform.update(total_force, self.time.dt)

            solar_power = self.solar.compute_power()

            x, y, z, roll, pitch, yaw = self.platform.position

            print(
                f"t={self.time.t:.1f}s | "
                f"x={x:.3f} y={y:.3f} z={z:.3f} | "
                f"roll={roll:.4f} pitch={pitch:.4f} yaw={yaw:.4f} | "
                f"P_solar={solar_power:.1f} W"
            )

            self.time.advance()

        print("Simulation finished")
