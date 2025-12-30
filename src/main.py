from coupling.coupling_manager import CouplingManager
from config.simulation_config import SimulationConfig

def main():
    config = SimulationConfig()
    simulation = CouplingManager(config)
    simulation.run()

if __name__ == "__main__":
    main()
