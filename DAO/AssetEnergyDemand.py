
class AssetEnergyDemand:

    # Constructor to initialize an AssetEnergyDemand object
    def __init__(self, data):
        self.asset = data["asset"]
        self.energy_type = data["energy_type"]
        self.energy_demand = data["energy_demand"]
