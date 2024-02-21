from fastapi import APIRouter, HTTPException
from processor.assets_processor import MetricsProcessor

router = APIRouter()


@router.get("/asset/{asset_id}")
def energy_demand_for_asset(asset_id: str):
    if not asset_id.isdigit():
        raise HTTPException(
            status_code=405, detail="Asset id must be an integer")
    return MetricsProcessor.calculate_metrics(asset_id)
