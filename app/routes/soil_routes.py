from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.models.soil_model import SoilModel

router = APIRouter()
soil_model = SoilModel()

class RegionRequest(BaseModel):
    region: str

@router.post("/soil/analyze")
async def analyze_soil(
    soil_image: UploadFile = File(...),
    region: str = Form(...)
):
    """Analyze soil from image and provide recommendations"""
    try:
        # Save the image temporarily
        image_path = soil_model.save_image(soil_image)
        
        # Analyze the soil
        analysis = soil_model.analyze_soil(image_path, region)
        
        # Clean up the temporary file
        soil_model.cleanup_image(image_path)
        
        return {"status": "success", "data": analysis}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/soil/recommendations")
async def get_recommendations(region: RegionRequest):
    """Get soil recommendations based on region"""
    try:
        recommendations = soil_model.get_recommendations(region.region)
        return {"status": "success", "data": recommendations}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 