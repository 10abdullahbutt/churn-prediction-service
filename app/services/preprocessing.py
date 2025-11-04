import pandas as pd
from typing import Dict, Any, Tuple


class PreprocessingService:
    

    def __init__(self):
        
        self.feature_columns = [
            'Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'Tenure',
            'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
            'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
            'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
            'MonthlyCharges', 'TotalCharges'
        ]

        self.binary_mappings = {
            'Gender': {'Female': 0, 'Male': 1},
            'Partner': {'No': 0, 'Yes': 1},
            'Dependents': {'No': 0, 'Yes': 1},
            'PhoneService': {'No': 0, 'Yes': 1},
            'PaperlessBilling': {'No': 0, 'Yes': 1}
        }

        self.multiclass_mappings = {
            'MultipleLines': {'No phone service': 0, 'No': 1, 'Yes': 2},
            'InternetService': {'No': 0, 'DSL': 1, 'Fiber optic': 2},
            'OnlineSecurity': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'OnlineBackup': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'DeviceProtection': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'TechSupport': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'StreamingTV': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'StreamingMovies': {'No internet service': 0, 'No': 1, 'Yes': 2},
            'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
            'PaymentMethod': {
                'Electronic check': 0,
                'Mailed check': 1,
                'Bank transfer (automatic)': 2,
                'Credit card (automatic)': 3
            }
        }

    def preprocess(self, data: Dict[str, Any]) -> pd.DataFrame:
        
        df = pd.DataFrame([data])

        
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

        
        df['TotalCharges'] = df['TotalCharges'].fillna(0)

     
        for col, mapping in self.binary_mappings.items():
            if col in df.columns:
                df[col] = df[col].map(mapping)

        
        for col, mapping in self.multiclass_mappings.items():
            if col in df.columns:
                df[col] = df[col].map(mapping)

        
        df = df[self.feature_columns]

        return df
    
    def validate_input(self, data: Dict[str, Any]) -> Tuple[bool, str]:
        
        missing_fields = set(self.feature_columns) - set(data.keys())
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"
        
        if data.get('SeniorCitizen') not in [0, 1]:
            return False, "SeniorCitizen must be 0 or 1"
        
        if data.get('Tenure', -1) < 0:
            return False, "Tenure must be >= 0"
        
        if data.get('MonthlyCharges', -1) < 0:
            return False, "MonthlyCharges must be >= 0"
        
        return True, ""

