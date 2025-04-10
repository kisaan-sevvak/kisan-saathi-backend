import os
import json
from datetime import datetime, timedelta
import random

async def get_market_info() -> str:
    # This is a placeholder function that returns dummy market data
    # In production, this would fetch real market data from a market API
    
    crops = [
        {"name": "Wheat", "min_price": 2000, "max_price": 2500},
        {"name": "Rice", "min_price": 3000, "max_price": 3500},
        {"name": "Cotton", "min_price": 5000, "max_price": 6000},
        {"name": "Sugarcane", "min_price": 350, "max_price": 400},
        {"name": "Soybean", "min_price": 4500, "max_price": 5000}
    ]
    
    # Select 3 random crops for the response
    selected_crops = random.sample(crops, 3)
    
    # Format the response
    response = "Current market prices:\n\n"
    for crop in selected_crops:
        current_price = random.randint(crop["min_price"], crop["max_price"])
        price_change = random.randint(-100, 100)
        trend = "↑" if price_change > 0 else "↓" if price_change < 0 else "→"
        
        response += f"{crop['name']}:\n"
        response += f"Price: ₹{current_price}/quintal {trend}\n"
        response += f"Change: ₹{abs(price_change)} ({trend})\n\n"
    
    return response 