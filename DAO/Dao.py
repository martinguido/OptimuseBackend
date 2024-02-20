import json
from .Asset import Asset
from .AssetEnergyDemand import AssetEnergyDemand
from .AssetEnergyOutput import AssetEnergyOutput
from .AssetEnergySystem import AssetEnergySystem
from .EnergySystem import EnergySystem
from .EnergyType import EnergyType


class Dao:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
            energy_systems = [EnergySystem(item)
                              for item in data["energy_system"]]
            assets = [Asset(item) for item in data["asset"]]
            asset_energy_demands = [AssetEnergyDemand(
                item) for item in data["asset_energy_demand"]]
            asset_energy_outputs = [AssetEnergyOutput(
                item) for item in data["asset_energy_output"]]
            energy_types = [EnergyType(item) for item in data["energy_type"]]
            asset_energy_systems = [AssetEnergySystem(
                item) for item in data["asset_energy_system"]]

            return energy_systems, assets, asset_energy_demands, asset_energy_outputs, energy_types, asset_energy_systems
        except FileNotFoundError:
            print("File at path: "+self.file_path+" not found")
            return
        except json.JSONDecodeError:
            print("Cannot decode json from file at path: "+self.file_path)
            return
