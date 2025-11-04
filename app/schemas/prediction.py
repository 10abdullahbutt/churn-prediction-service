from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    
    Gender: str = Field(..., description="Customer gender (Male/Female)")
    SeniorCitizen: int = Field(..., ge=0, le=1, description="Whether customer is a senior citizen (0/1)")
    Partner: str = Field(..., description="Whether customer has a partner (Yes/No)")
    Dependents: str = Field(..., description="Whether customer has dependents (Yes/No)")
    Tenure: int = Field(..., ge=0, description="Number of months customer has been with company")
    PhoneService: str = Field(..., description="Whether customer has phone service (Yes/No)")
    MultipleLines: str = Field(..., description="Whether customer has multiple lines (Yes/No/No phone service)")
    InternetService: str = Field(..., description="Type of internet service (DSL/Fiber optic/No)")
    OnlineSecurity: str = Field(..., description="Whether customer has online security (Yes/No/No internet service)")
    OnlineBackup: str = Field(..., description="Whether customer has online backup (Yes/No/No internet service)")
    DeviceProtection: str = Field(..., description="Whether customer has device protection (Yes/No/No internet service)")
    TechSupport: str = Field(..., description="Whether customer has tech support (Yes/No/No internet service)")
    StreamingTV: str = Field(..., description="Whether customer has streaming TV (Yes/No/No internet service)")
    StreamingMovies: str = Field(..., description="Whether customer has streaming movies (Yes/No/No internet service)")
    Contract: str = Field(..., description="Contract type (Month-to-month/One year/Two year)")
    PaperlessBilling: str = Field(..., description="Whether customer has paperless billing (Yes/No)")
    PaymentMethod: str = Field(..., description="Payment method (Electronic check/Mailed check/Bank transfer (automatic)/Credit card (automatic))")
    MonthlyCharges: float = Field(..., ge=0, description="Monthly charges amount")
    TotalCharges: str = Field(..., description="Total charges (as string to handle empty values)")

    class Config:
        json_schema_extra = {
            "example": {
                "Gender": "Female",
                "SeniorCitizen": 0,
                "Partner": "Yes",
                "Dependents": "No",
                "Tenure": 12,
                "PhoneService": "Yes",
                "MultipleLines": "No",
                "InternetService": "DSL",
                "OnlineSecurity": "No",
                "OnlineBackup": "Yes",
                "DeviceProtection": "No",
                "TechSupport": "No",
                "StreamingTV": "No",
                "StreamingMovies": "No",
                "Contract": "Month-to-month",
                "PaperlessBilling": "Yes",
                "PaymentMethod": "Electronic check",
                "MonthlyCharges": 53.85,
                "TotalCharges": "646.2"
            }
        }


class PredictionResponse(BaseModel):
    
    churn_prediction: str = Field(..., description="Predicted churn status (Yes/No)")
    probability: float = Field(..., description="Probability of churn", ge=0, le=1)
    confidence: str = Field(..., description="Confidence level of prediction")

