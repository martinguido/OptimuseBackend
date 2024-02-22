# Necessary imports
from fastapi import APIRouter, HTTPException

# Import the MetricsProcessor class from the assets_processor module in the processor package
from processor.assets_processor import MetricsProcessor

# Create an instance of APIRouter
router = APIRouter()


# Define a route for handling GET requests to '/asset/{asset_id}'
@router.get("/asset/{asset_id}")
def energy_demand_for_asset(asset_id: str):

    # Check if the asset_id is a valid integer, because all the asset ids in the file json_database.json are digits.
    if not asset_id.isdigit():

        # If not a valid integer, raise an HTTPException with status code 405 (Method Not Allowed) and detail message: Asset id must be an integer
        raise HTTPException(
            status_code=405, detail="Asset id must be an integer")

    # Call the calculate_metrics method of MetricsProcessor class to calculate metrics for the given asset_id
    return MetricsProcessor.calculate_metrics(asset_id)
