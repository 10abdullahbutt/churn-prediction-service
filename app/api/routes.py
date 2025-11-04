
from fastapi import APIRouter, HTTPException, status
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.preprocessing import PreprocessingService
from app.services.prediction import PredictionService
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["predictions"])

preprocessing_service = PreprocessingService()
prediction_service = PredictionService()


@router.post("/predict", response_model=PredictionResponse, status_code=status.HTTP_200_OK)
async def predict_churn(request: PredictionRequest):

    try:
        
        data_dict = request.model_dump()
        
        
        is_valid, error_message = preprocessing_service.validate_input(data_dict)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_message
            )
        
        
        preprocessed_data = preprocessing_service.preprocess(data_dict)
        
        
        prediction_result = prediction_service.predict(preprocessed_data)
        
        return PredictionResponse(**prediction_result)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Prediction endpoint error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process prediction: {str(e)}"
        )


@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():

    model_file_exists = prediction_service.model_path.exists()
    
    return {
        "status": "healthy",
        "service": "churn-prediction-service",
        "model_file_exists": model_file_exists,
        "model_loaded": prediction_service._model_loaded
    }

