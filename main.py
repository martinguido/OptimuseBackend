from typing import Union
from fastapi import FastAPI
from controller.assets_controller import router

app = FastAPI()

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "OK"}
