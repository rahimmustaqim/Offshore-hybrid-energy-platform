class SolarModel:
    def __init__(self, efficiency=0.2, area=500):
        self.efficiency = efficiency
        self.area = area

    def compute_power(self, irradiance=800):
        return self.efficiency * self.area * irradiance
