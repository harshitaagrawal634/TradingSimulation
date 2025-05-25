from simulation.simulation import Simulation

if __name__ == "__main__":
    simulation = Simulation(num_traders=5, trading_hours=0.01)  # 0.01 for quick test
    simulation.run()
