from typing import Union

from fastapi import FastAPI

from DAO.Dao import Dao
from DAO.Asset import Asset
from DAO.AssetEnergyDemand import AssetEnergyDemand
from DAO.AssetEnergyOutput import AssetEnergyOutput
from DAO.AssetEnergySystem import AssetEnergySystem
from DAO.EnergySystem import EnergySystem
from DAO.EnergyType import EnergyType

app = FastAPI()
file_path = "json_database.json"
dao = Dao(file_path)
energy_systems, assets, asset_energy_demands, asset_energy_outputs, energy_types, asset_energy_systems = dao.load_data()


@app.get("/")
def read_root():
    print(energy_systems, assets, asset_energy_demands,
          asset_energy_outputs, energy_types, asset_energy_systems)
    return energy_systems
