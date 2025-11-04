# Churn Prediction Service

A FastAPI-based microservice for predicting customer churn using machine learning.

## 🚀 Features

- RESTful API for churn predictions
- Minimal data transformation (type conversion and column ordering)
- Comprehensive input validation
- Health check endpoint
- Interactive API documentation (Swagger UI)
- Structured microservice architecture

## 📁 Project Structure

```
churn-prediction-service/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py          # API routes
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── prediction.py      # Pydantic models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── preprocessing.py   # Data preprocessing
│   │   └── prediction.py      # Prediction logic
│   └── config.py              # Configuration
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables example
└── README.md                  # This file
```

## 🛠️ Installation

1. **Clone the repository** (if applicable)

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure your model file is present:**
   - Place `random_forest_model.joblib` in the root directory

5. **Configure environment (optional):**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

## 🚦 Running the Service

### Development Mode

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The service will be available at:
- API: `http://localhost:8000`
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📡 API Endpoints

### 1. Predict Churn
**POST** `/api/v1/predict`

Predicts whether a customer will churn based on their characteristics.

**Request Body:**
```json
{
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
```

**Response:**
```json
{
  "churn_prediction": "No",
  "probability": 0.15,
  "confidence": "High"
}
```

### 2. Health Check
**GET** `/api/v1/health`

Returns the health status of the service.

**Response:**
```json
{
  "status": "healthy",
  "service": "churn-prediction-service",
  "model_loaded": true
}
```

## 📝 Input Field Descriptions

- **Gender**: Customer gender (Male/Female)
- **SeniorCitizen**: Whether customer is a senior citizen (0/1)
- **Partner**: Whether customer has a partner (Yes/No)
- **Dependents**: Whether customer has dependents (Yes/No)
- **Tenure**: Number of months customer has been with company (>= 0)
- **PhoneService**: Whether customer has phone service (Yes/No)
- **MultipleLines**: Whether customer has multiple lines (Yes/No/No phone service)
- **InternetService**: Type of internet service (DSL/Fiber optic/No)
- **OnlineSecurity**: Whether customer has online security (Yes/No/No internet service)
- **OnlineBackup**: Whether customer has online backup (Yes/No/No internet service)
- **DeviceProtection**: Whether customer has device protection (Yes/No/No internet service)
- **TechSupport**: Whether customer has tech support (Yes/No/No internet service)
- **StreamingTV**: Whether customer has streaming TV (Yes/No/No internet service)
- **StreamingMovies**: Whether customer has streaming movies (Yes/No/No internet service)
- **Contract**: Contract type (Month-to-month/One year/Two year)
- **PaperlessBilling**: Whether customer has paperless billing (Yes/No)
- **PaymentMethod**: Payment method (Electronic check/Mailed check/Bank transfer (automatic)/Credit card (automatic))
- **MonthlyCharges**: Monthly charges amount (>= 0)
- **TotalCharges**: Total charges (string, can handle empty values)

## 🔧 Configuration

The service can be configured via environment variables or a `.env` file:

- `APP_NAME`: Application name
- `APP_VERSION`: Application version
- `DEBUG`: Enable debug mode (true/false)
- `MODEL_PATH`: Path to the model file
- `LOG_LEVEL`: Logging level (DEBUG/INFO/WARNING/ERROR)

## ⚠️ Important Notes

1. **Model Compatibility**: The service performs minimal data transformation (type conversion and column ordering). Ensure your trained model can handle the input data format directly.

2. **Production**: For production deployment, consider:
   - Setting up proper CORS origins
   - Using environment variables for sensitive configuration
   - Adding authentication/authorization
   - Setting up logging and monitoring
   - Using a reverse proxy (nginx)
   - Deploying with Docker

## 🧪 Testing

You can test the API using curl:

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

## 📦 Docker Support (Optional)

Create a `Dockerfile` for containerization:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```


