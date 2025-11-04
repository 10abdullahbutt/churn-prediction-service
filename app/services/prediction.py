"""
Prediction service for churn prediction.
"""
import joblib
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class PredictionService:
   
    
    def __init__(self, model_path: str = "random_forest_model.joblib"):
       
        self.model_path = Path(model_path)
        self.model: Optional[Any] = None
        self._model_loaded = False
    
    def _load_model(self):
        
        if self._model_loaded:
            return
        
        try:
            if not self.model_path.exists():
                raise FileNotFoundError(f"Model file not found at {self.model_path}")
            
            logger.info(f"Loading model from {self.model_path}...")
            self.model = joblib.load(self.model_path)
            self._model_loaded = True
            logger.info(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    def predict(self, preprocessed_data) -> Dict[str, Any]:
        
        if not self._model_loaded:
            self._load_model()
        
        if self.model is None:
            raise RuntimeError("Model not loaded")
        
        try:
            
            if hasattr(self.model, 'predict_proba'):
                probabilities = self.model.predict_proba(preprocessed_data)[0]
                churn_probability = float(probabilities[1])
            else:
                
                prediction = self.model.predict(preprocessed_data)[0]
                churn_probability = 0.5 if prediction == 1 else 0.5
            
            
            prediction = self.model.predict(preprocessed_data)[0]
            churn_status = "Yes" if prediction == 1 else "No"
            
            
            confidence = self._get_confidence_level(churn_probability)
            
            return {
                "churn_prediction": churn_status,
                "probability": churn_probability,
                "confidence": confidence
            }
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            raise RuntimeError(f"Failed to make prediction: {e}")
    
    def _get_confidence_level(self, probability: float) -> str:
        
        if probability >= 0.8 or probability <= 0.2:
            return "High"
        elif probability >= 0.6 or probability <= 0.4:
            return "Medium"
        else:
            return "Low"

