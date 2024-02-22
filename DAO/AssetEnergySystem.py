
class AssetEnergySystem:

    # Constructor to initialize an AssetEnergySystem object
    def __init__(self, data):
        self.asset = data["asset"]
        self.energy_system = data["energy_system"]
        self.energy_type = data["energy_type"]
