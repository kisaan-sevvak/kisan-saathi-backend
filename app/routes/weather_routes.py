from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.models.weather_model import WeatherModel

router = APIRouter()
weather_model = WeatherModel()

class LocationRequest(BaseModel):
    latitude: float
    longitude: float

@router.get("/weather/forecast")
async def get_forecast(location: LocationRequest):
    """Get weather forecast based on location"""
    try:
        forecast = weather_model.get_forecast(
            location.latitude,
            location.longitude
        )
        return {"status": "success", "data": forecast}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/weather/alerts")
async def get_alerts(location: LocationRequest):
    """Get weather alerts for a specific location"""
    try:
        alerts = weather_model.get_alerts(
            location.latitude,
            location.longitude
        )
        return {"status": "success", "data": alerts}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 