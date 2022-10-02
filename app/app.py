
from fastapi import FastAPI
from app.settings import settings
from typing import Dict


def create_app() -> FastAPI:
    app = FastAPI(
        debug= settings.DEBUG,
        title= settings.APP_TITLE,
        version= settings.VERSION
    )

    @app.get("/")
    def home() -> Dict:
        return {"msg": "Hello World"}
    
    # app.include_router(api_routes)
    
    return app