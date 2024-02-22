# Necessary imports
from typing import Union
from fastapi import FastAPI
from controller.assets_controller import router

# Instance of FastAPI
app = FastAPI()

# Include the router defined in assets_controller in the FastAPI instance
app.include_router(router)


# Define an endpoint to check the health status of the application
@app.get("/health")
def health():
    # Return an object with the health status of the application
    return {"status": "OK"}
