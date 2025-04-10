from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from app.routes.crop_routes import CropRoutes
from app.routes.weather_routes import WeatherRoutes
from app.routes.soil_routes import SoilRoutes
from app.routes.market_routes import MarketRoutes
from app.routes.disease_routes import DiseaseRoutes

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    
    # Initialize API
    api = Api(app)
    
    # Register routes
    api.add_resource(CropRoutes, '/api/crops')
    api.add_resource(WeatherRoutes, '/api/weather')
    api.add_resource(SoilRoutes, '/api/soil')
    api.add_resource(MarketRoutes, '/api/market')
    api.add_resource(DiseaseRoutes, '/api/disease')
    
    return app 