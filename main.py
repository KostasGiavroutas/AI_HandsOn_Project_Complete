from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model.joblib")
preprocessor = joblib.load("preprocessor.joblib")

class PurchaseData(BaseModel):
    Price: float
    Quantity: int
    Customer_Rating: float
    Discount_Applied: int
    Product_Category: str
    Payment_Method: str
    gender: str
    age_category: str
    size: str
    Delivery_Time_Days: int
    Previous_Purchases: int
    Category_Tops: int
    Category_Bottoms: int
    Category_Accessories: int

@app.post("/predict")
def predict(data: PurchaseData):
    try:
        X = pd.DataFrame([data.dict()])
        X_processed = preprocessor.transform(X)
        prediction = model.predict(X_processed)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

