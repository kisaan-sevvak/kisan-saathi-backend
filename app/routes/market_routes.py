from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from app.models.market_model import MarketModel

router = APIRouter()
market_model = MarketModel()

class MarketRequest(BaseModel):
    crop_name: str
    region: str

@router.get("/market/prices")
async def get_prices(market: MarketRequest):
    """Get market prices for a specific crop and region"""
    try:
        prices = market_model.get_prices(
            market.crop_name,
            market.region
        )
        return {"status": "success", "data": prices}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/market/trends")
async def get_trends(market: MarketRequest):
    """Get market trends for a specific crop and region"""
    try:
        trends = market_model.get_trends(
            market.crop_name,
            market.region
        )
        return {"status": "success", "data": trends}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 