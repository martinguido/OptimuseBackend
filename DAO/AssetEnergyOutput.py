
class AssetEnergyOutput:

    # Constructor to initialize an AssetEnergyOutput object
    def __init__(self, data):
        self.asset = data["asset"]
        self.energy_output = data["energy_output"]
