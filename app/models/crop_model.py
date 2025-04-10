import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import pickle

class CropModel:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'crop_recommendation.pkl')
        self.model = self._load_model()
        self.crop_data = self._load_crop_data()
    
    def _load_model(self):
        """Load the trained model or create a dummy one for now"""
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                return pickle.load(f)
        else:
            # Create a dummy model for now
            model = RandomForestClassifier()
            # Save the model
            os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
            with open(self.model_path, 'wb') as f:
                pickle.dump(model, f)
            return model
    
    def _load_crop_data(self):
        """Load crop data or create dummy data for now"""
        data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'crop_data.csv')
        if os.path.exists(data_path):
            return pd.read_csv(data_path)
        else:
            # Create dummy data
            data = pd.DataFrame({
                'crop_name': ['Rice', 'Wheat', 'Maize', 'Sugarcane', 'Cotton'],
                'soil_type': ['Clay', 'Sandy', 'Loamy', 'Black', 'Red'],
                'region': ['North', 'South', 'East', 'West', 'Central'],
                'season': ['Kharif', 'Rabi', 'Summer', 'Winter', 'Monsoon']
            })
            # Save the data
            os.makedirs(os.path.dirname(data_path), exist_ok=True)
            data.to_csv(data_path, index=False)
            return data
    
    def get_recommendations(self, crop_name, soil_type, region, season):
        """Get crop recommendations based on parameters"""
        # For now, return dummy recommendations
        recommendations = {
            'crop_name': crop_name,
            'soil_type': soil_type,
            'region': region,
            'season': season,
            'sowing_time': 'June-July',
            'harvesting_time': 'October-November',
            'water_requirement': 'Medium',
            'fertilizer_recommendation': {
                'N': '100 kg/ha',
                'P': '50 kg/ha',
                'K': '50 kg/ha'
            },
            'pest_control': [
                'Use neem-based pesticides',
                'Practice crop rotation',
                'Maintain field hygiene'
            ]
        }
        return recommendations
    
    def add_crop(self, crop_name, soil_type, region, season):
        """Add a new crop to the database"""
        # For now, just return success
        return {
            'crop_name': crop_name,
            'soil_type': soil_type,
            'region': region,
            'season': season,
            'status': 'added'
        } 