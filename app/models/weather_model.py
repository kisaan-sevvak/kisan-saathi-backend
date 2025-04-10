import requests
import os
import json
from datetime import datetime, timedelta

class WeatherModel:
    def __init__(self):
        self.api_key = os.environ.get('WEATHER_API_KEY', 'your_api_key_here')
        self.base_url = 'https://api.openweathermap.org/data/2.5'
    
    def get_forecast(self, latitude, longitude):
        """Get weather forecast based on location"""
        # For now, return dummy forecast data
        # In production, you would call the OpenWeatherMap API
        current_date = datetime.now()
        forecast = {
            'current': {
                'temperature': 28.5,
                'humidity': 65,
                'wind_speed': 5.2,
                'description': 'Partly cloudy',
                'icon': '04d'
            },
            'daily': []
        }
        
        # Generate 5 days of forecast
        for i in range(5):
            date = current_date + timedelta(days=i)
            forecast['daily'].append({
                'date': date.strftime('%Y-%m-%d'),
                'temperature': {
                    'min': 20 + i,
                    'max': 30 + i
                },
                'humidity': 60 + i,
                'wind_speed': 5.0 + i * 0.5,
                'description': 'Sunny',
                'icon': '01d'
            })
        
        return forecast
    
    def get_alerts(self, latitude, longitude):
        """Get weather alerts for a specific location"""
        # For now, return dummy alerts
        alerts = [
            {
                'type': 'rain',
                'severity': 'moderate',
                'description': 'Moderate rain expected in the next 24 hours',
                'time': (datetime.now() + timedelta(hours=12)).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'type': 'wind',
                'severity': 'light',
                'description': 'Light winds expected throughout the day',
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        ]
        return alerts 