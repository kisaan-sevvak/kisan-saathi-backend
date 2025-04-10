import os
import json
from datetime import datetime, timedelta
import random

async def get_weather_info() -> str:
    # This is a placeholder function that returns dummy weather data
    # In production, this would fetch real weather data from a weather API
    
    current_time = datetime.now()
    temperatures = [25, 26, 27, 28, 29, 30]
    conditions = ["sunny", "partly cloudy", "cloudy", "light rain", "moderate rain"]
    
    current_temp = random.choice(temperatures)
    current_condition = random.choice(conditions)
    
    # Generate forecast for next 3 days
    forecast = []
    for i in range(3):
        date = current_time + timedelta(days=i)
        forecast.append({
            "date": date.strftime("%Y-%m-%d"),
            "temp": random.choice(temperatures),
            "condition": random.choice(conditions)
        })
    
    # Format the response
    response = f"Current weather: {current_temp}°C, {current_condition}\n\n"
    response += "3-day forecast:\n"
    for day in forecast:
        response += f"{day['date']}: {day['temp']}°C, {day['condition']}\n"
    
    return response 