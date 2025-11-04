from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    
    APP_NAME: str = "Churn Prediction Service"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    MODEL_PATH: str = "random_forest_model.joblib"
    
    API_PREFIX: str = "/api/v1"
    
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

