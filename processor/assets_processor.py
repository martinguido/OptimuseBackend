
from fastapi import HTTPException
from DAO.Dao import Dao

file_path = "json_database.json"
dao = Dao(file_path)
energy_systems, assets, asset_energy_demands, asset_energy_outputs, energy_types, asset_energy_systems = dao.load_data()


class MetricsProcessor():
    def calculate_metrics(asset_id: str):
        asset_id = int(asset_id)
        name = None
        for asset in assets:
            if asset.id == asset_id:
                name = asset.name
                break
        if name == None:
            raise HTTPException(status_code=404, detail="Asset id not found")
        response = {"name": name, "energy_types": {"heat": 0, "water": 0, "light": 0,
                                                   "cool": 0}, "total_energy_demand": 0, "energy_output_reduction": 0}
        asset_energy_demand_by_asset_id = [
            demand for demand in asset_energy_demands if demand.asset == asset_id]

        for demand in asset_energy_demand_by_asset_id:
            energy_demand = demand.energy_demand
            response["total_energy_demand"] += energy_demand

            for energy_type in energy_types:
                if energy_type.id == demand.energy_type:
                    energy_type_name = energy_type.name
                    response["energy_types"][energy_type_name] += energy_demand
                    break

            for asset_energy_system in asset_energy_systems:
                if asset_energy_system.asset == asset_id and asset_energy_system.energy_type == demand.energy_type:
                    energy_system_for_asset = asset_energy_system.energy_system
                    break

            for energy_system in energy_systems:
                if energy_system.id == energy_system_for_asset:
                    energy_system_for_asset_name = energy_system.name
                    break

            if energy_system_for_asset_name == "electricity":
                for asset_energy_output in asset_energy_outputs:
                    if asset_energy_output.asset == asset_id:
                        energy_output_for_asset = asset_energy_output.energy_output
                        response["energy_output_reduction"] = round(
                            ((energy_demand - energy_output_for_asset) / energy_demand) * 100, 2)
                        break

        return response
