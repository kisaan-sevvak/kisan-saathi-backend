from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.models.crop_model import CropModel

router = APIRouter()
crop_model = CropModel()

class CropRequest(BaseModel):
    crop_name: str
    soil_type: str
    region: str
    season: str

@router.get("/crops/recommendations")
async def get_recommendations(crop: CropRequest):
    """Get crop recommendations based on parameters"""
    try:
        recommendations = crop_model.get_recommendations(
            crop.crop_name,
            crop.soil_type,
            crop.region,
            crop.season
        )
        return {"status": "success", "data": recommendations}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/crops")
async def add_crop(crop: CropRequest):
    """Add a new crop to the database"""
    try:
        result = crop_model.add_crop(
            crop.crop_name,
            crop.soil_type,
            crop.region,
            crop.season
        )
        return {"status": "success", "message": "Crop added successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 