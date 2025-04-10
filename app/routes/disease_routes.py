from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.models.disease_model import DiseaseModel

router = APIRouter()
disease_model = DiseaseModel()

class CropNameRequest(BaseModel):
    crop_name: str

@router.post("/diseases/detect")
async def detect_disease(
    plant_image: UploadFile = File(...),
    crop_name: str = Form(...)
):
    """Detect plant diseases from image and provide treatment recommendations"""
    try:
        # Save the image temporarily
        image_path = disease_model.save_image(plant_image)
        
        # Detect diseases
        detection = disease_model.detect_disease(image_path, crop_name)
        
        # Clean up the temporary file
        disease_model.cleanup_image(image_path)
        
        return {"status": "success", "data": detection}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/diseases/common")
async def get_common_diseases(crop: CropNameRequest):
    """Get common diseases for a specific crop"""
    try:
        diseases = disease_model.get_common_diseases(crop.crop_name)
        return {"status": "success", "data": diseases}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 