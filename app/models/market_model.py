from typing import Dict, Any, List
from datetime import datetime, timedelta
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class MarketModel:
    def __init__(self):
        self.base_url = os.getenv("MARKET_API_URL", "http://127.0.0.1:5000/request")
        # For production, you might want to host this API yourself or use a different endpoint
    
    def get_prices(self, crop_name: str, region: str) -> Dict[str, Any]:
        """Get market prices for a specific crop and region"""
        try:
            # Extract state and city from region (assuming format: "City, State")
            parts = region.split(',')
            if len(parts) >= 2:
                city = parts[0].strip()
                state = parts[1].strip()
            else:
                # Default to first part as city and empty state
                city = parts[0].strip()
                state = ""
            
            # Make request to Agmarknet API
            response = requests.get(
                self.base_url,
                params={
                    "commodity": crop_name,
                    "state": state,
                    "market": city
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    # Get the latest price data
                    latest = data[0]
                    return {
                        "current_price": float(latest.get("Model Prize", 0)),
                        "unit": "per quintal",  # Agmarknet uses quintal as unit
                        "market": f"{city}, {state}",
                        "last_updated": latest.get("Date", datetime.now().strftime("%d %b %Y")),
                        "price_range": {
                            "min": float(latest.get("Min Prize", 0)),
                            "max": float(latest.get("Max Prize", 0))
                        },
                        "historical_data": data[:7]  # Last 7 days of data
                    }
                else:
                    return {
                        "error": "No price data available for this commodity and region",
                        "commodity": crop_name,
                        "region": region
                    }
            else:
                return {
                    "error": f"Failed to fetch data: {response.status_code}",
                    "commodity": crop_name,
                    "region": region
                }
        except Exception as e:
            # Fallback to dummy data if API fails
            return {
                "current_price": 45.50,
                "unit": "per kg",
                "market": "Local Mandi",
                "last_updated": datetime.now().isoformat(),
                "price_range": {
                    "min": 40.00,
                    "max": 50.00
                },
                "error": str(e)
            }
    
    def get_trends(self, crop_name: str, region: str) -> Dict[str, Any]:
        """Get market trends for a specific crop and region"""
        try:
            # Extract state and city from region (assuming format: "City, State")
            parts = region.split(',')
            if len(parts) >= 2:
                city = parts[0].strip()
                state = parts[1].strip()
            else:
                # Default to first part as city and empty state
                city = parts[0].strip()
                state = ""
            
            # Make request to Agmarknet API
            response = requests.get(
                self.base_url,
                params={
                    "commodity": crop_name,
                    "state": state,
                    "market": city
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                if data and len(data) > 0:
                    # Calculate trend
                    if len(data) >= 2:
                        current_price = float(data[0].get("Model Prize", 0))
                        previous_price = float(data[1].get("Model Prize", 0))
                        change_percentage = ((current_price - previous_price) / previous_price) * 100 if previous_price > 0 else 0
                        trend = "upward" if change_percentage > 0 else "downward" if change_percentage < 0 else "stable"
                    else:
                        change_percentage = 0
                        trend = "stable"
                    
                    # Format historical data
                    historical_data = []
                    for item in data[:7]:  # Last 7 days
                        historical_data.append({
                            "date": item.get("Date", ""),
                            "price": float(item.get("Model Prize", 0))
                        })
                    
                    return {
                        "trend": trend,
                        "change_percentage": round(change_percentage, 2),
                        "historical_data": historical_data,
                        "forecast": {
                            "next_week": "stable" if trend == "stable" else trend,
                            "next_month": "upward" if trend == "upward" else "downward" if trend == "downward" else "stable",
                            "confidence": 0.85
                        }
                    }
                else:
                    return {
                        "error": "No trend data available for this commodity and region",
                        "commodity": crop_name,
                        "region": region
                    }
            else:
                return {
                    "error": f"Failed to fetch data: {response.status_code}",
                    "commodity": crop_name,
                    "region": region
                }
        except Exception as e:
            # Fallback to dummy data if API fails
            today = datetime.now()
            return {
                "trend": "upward",
                "change_percentage": 5.2,
                "historical_data": [
                    {
                        "date": (today - timedelta(days=i)).isoformat(),
                        "price": 45.50 - (i * 0.5)
                    } for i in range(7)
                ],
                "forecast": {
                    "next_week": "stable",
                    "next_month": "upward",
                    "confidence": 0.85
                },
                "error": str(e)
            } 