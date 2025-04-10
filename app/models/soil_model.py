import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

class SoilModel:
    def __init__(self):
        self.model_path = 'models/soil_analysis.pkl'
        self.scaler_path = 'models/soil_scaler.pkl'
        self.model = self._load_model()
        self.scaler = self._load_scaler()
    
    def _load_model(self):
        """Load the trained soil analysis model"""
        if os.path.exists(self.model_path):
            return joblib.load(self.model_path)
        return None
    
    def _load_scaler(self):
        """Load the feature scaler"""
        if os.path.exists(self.scaler_path):
            return joblib.load(self.scaler_path)
        return StandardScaler()
    
    def analyze_soil(self, ph, nitrogen, phosphorus, potassium, temperature, humidity, rainfall):
        """Analyze soil parameters and provide recommendations"""
        # For now, return dummy analysis
        # In production, you would use the trained model
        analysis = {
            'soil_health': {
                'score': 75,
                'status': 'Good',
                'recommendations': [
                    'Maintain current pH levels',
                    'Consider adding organic matter',
                    'Monitor potassium levels'
                ]
            },
            'nutrient_levels': {
                'nitrogen': {
                    'value': nitrogen,
                    'status': 'Optimal',
                    'recommendation': 'No additional nitrogen needed'
                },
                'phosphorus': {
                    'value': phosphorus,
                    'status': 'Low',
                    'recommendation': 'Add phosphorus-rich fertilizers'
                },
                'potassium': {
                    'value': potassium,
                    'status': 'Moderate',
                    'recommendation': 'Monitor potassium levels'
                }
            },
            'environmental_factors': {
                'temperature': {
                    'value': temperature,
                    'impact': 'Favorable',
                    'recommendation': 'Current temperature is suitable for most crops'
                },
                'humidity': {
                    'value': humidity,
                    'impact': 'Moderate',
                    'recommendation': 'Maintain current irrigation schedule'
                },
                'rainfall': {
                    'value': rainfall,
                    'impact': 'Adequate',
                    'recommendation': 'No additional irrigation needed'
                }
            }
        }
        return analysis
    
    def get_fertilizer_recommendations(self, crop_type, soil_analysis):
        """Get fertilizer recommendations based on soil analysis"""
        # For now, return dummy recommendations
        recommendations = {
            'organic_fertilizers': [
                {
                    'name': 'Compost',
                    'amount': '2-3 tons per hectare',
                    'frequency': 'Every 3 months',
                    'benefits': ['Improves soil structure', 'Adds organic matter']
                },
                {
                    'name': 'Vermicompost',
                    'amount': '1-2 tons per hectare',
                    'frequency': 'Every 2 months',
                    'benefits': ['Rich in nutrients', 'Improves soil fertility']
                }
            ],
            'inorganic_fertilizers': [
                {
                    'name': 'NPK 19:19:19',
                    'amount': '50 kg per hectare',
                    'frequency': 'Every 45 days',
                    'benefits': ['Balanced nutrition', 'Quick absorption']
                },
                {
                    'name': 'Urea',
                    'amount': '25 kg per hectare',
                    'frequency': 'Every 30 days',
                    'benefits': ['High nitrogen content', 'Cost-effective']
                }
            ],
            'application_schedule': [
                {
                    'stage': 'Pre-planting',
                    'fertilizers': ['Compost', 'NPK 19:19:19'],
                    'timing': '2 weeks before planting'
                },
                {
                    'stage': 'Vegetative growth',
                    'fertilizers': ['Urea', 'Vermicompost'],
                    'timing': 'Every 30 days'
                }
            ]
        }
        return recommendations 