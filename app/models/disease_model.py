import os
import json
from datetime import datetime
from typing import Dict, Any, List

class DiseaseModel:
    def __init__(self):
        self.temp_dir = "temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
    
    def save_image(self, image_file) -> str:
        """Save uploaded image temporarily"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"plant_{timestamp}.jpg"
        filepath = os.path.join(self.temp_dir, filename)
        
        with open(filepath, "wb") as buffer:
            content = image_file.file.read()
            buffer.write(content)
        
        return filepath
    
    def cleanup_image(self, image_path: str):
        """Delete temporary image file"""
        if os.path.exists(image_path):
            os.remove(image_path)
    
    def detect_disease(self, image_path: str, crop_name: str) -> Dict[str, Any]:
        """Detect plant diseases from image"""
        # TODO: Implement actual disease detection using ML model
        # For now, return dummy data
        return {
            "disease_name": "Leaf Blight",
            "confidence": 0.85,
            "severity": "Moderate",
            "treatment": {
                "chemical": ["Fungicide A", "Fungicide B"],
                "organic": ["Neem oil spray", "Garlic extract"],
                "cultural": ["Remove infected leaves", "Improve air circulation"]
            },
            "prevention": [
                "Plant resistant varieties",
                "Maintain proper spacing",
                "Regular monitoring"
            ]
        }
    
    def get_common_diseases(self, crop_name: str) -> List[Dict[str, Any]]:
        """Get common diseases for a specific crop"""
        # TODO: Implement database query
        # For now, return dummy data
        return [
            {
                "name": "Leaf Blight",
                "symptoms": ["Brown spots on leaves", "Yellowing", "Wilting"],
                "severity": "High",
                "season": "Monsoon"
            },
            {
                "name": "Root Rot",
                "symptoms": ["Stunted growth", "Yellow leaves", "Soft roots"],
                "severity": "Medium",
                "season": "All year"
            }
        ] 