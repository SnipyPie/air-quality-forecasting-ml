from fastapi import APIRouter, HTTPException
from app.api.schemas import CityRequest
from app.ingestion.geocoding import get_coordinates
from app.ingestion.pollution_fetcher import get_pollution
from app.inference.predict import predict_aqi
from app.storage.db import engine
import pandas as pd

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


from app.services.aqi_service import get_current_air_quality

@router.post("/current-air-quality")
def current_air_quality(request: CityRequest):
    return get_current_air_quality(request.city)

from app.services.prediction_service import get_prediction

@router.post("/predict")
def predict(request: CityRequest):
    return get_prediction(request.city)

from app.services.history_service import get_history_data
@router.get("/history")
def get_history(city: str,date: str):
    return get_history_data
