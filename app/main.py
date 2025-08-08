import os
import json
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
import xgboost as xgb
import pandas as pd
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Path to saved model
MODEL_FILE = os.path.join(os.path.dirname(__file__), "data", "model.json")

GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
GCS_BLOB_NAME = os.getenv("GCS_BLOB_NAME")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

app = FastAPI()


class Island(str, Enum):
    Torgersen = "Torgersen"
    Biscoe = "Biscoe"
    Dream = "Dream"

class Sex(str, Enum):
    male = "Male"
    female = "Female"


class PenguinFeatures(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    year: int
    sex: Sex
    island: Island


# Loading Model
def load_model():
    """
    Try to load model from GCS using service account.
    If that fails (no creds/env/bucket), fall back to local file.
    """
    model = xgb.XGBClassifier()

    # First, try GCS if env vars look present
    can_try_gcs = all([GCS_BUCKET_NAME, GCS_BLOB_NAME, GOOGLE_APPLICATION_CREDENTIALS])
    if can_try_gcs:
        try:
            logging.info("Attempting to load model from GCS: bucket=%s blob=%s",
                         GCS_BUCKET_NAME, GCS_BLOB_NAME)
            client = storage.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
            bucket = client.bucket(GCS_BUCKET_NAME)
            blob = bucket.blob(GCS_BLOB_NAME)

            # Download to memory, then load into XGBoost
            model_json_bytes = blob.download_as_bytes()
            model_json_str = model_json_bytes.decode("utf-8")
            model.load_model(bytearray(model_json_str, "utf-8"))  # XGB can load JSON from bytes
            logging.info("Model loaded from GCS successfully")
            return model
        except Exception as e:
            logging.exception("Failed to load model from GCS, will fall back to local file. Reason: %s", e)

    # Fallback: local file
    try:
        logging.info("Loading model from local file: %s", MODEL_FILE)
        model.load_model(MODEL_FILE)
        logging.info("Model loaded from local file successfully")
        return model
    except Exception:
        logging.exception("Failed to load model from local file.")
        raise


model = load_model()


# Preprocessing Data
def preprocess_input(features: PenguinFeatures) -> pd.DataFrame:
    logger.info("Preprocessing feature input %s", features)
    try:
        input_dict = features.model_dump()
        X_input = pd.DataFrame([input_dict]) 
        X_input = pd.get_dummies(X_input, columns=["sex", "island"]) 
        expected_cols = [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
            "sex_Female",
            "sex_Male",
            "island_Biscoe",
            "island_Dream",
            "island_Torgersen",
        ]
        X_input = X_input.reindex(columns=expected_cols, fill_value=0)
        X_input = X_input.astype(float)
        logger.info("Feature preprocessing completed successfully.")
        return X_input
    except Exception as e:
        logger.exception("Error during preprocessing.")
        raise e


# Creating the Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/predict")
async def predict(features: PenguinFeatures):
    logger.info("Received prediction request")
    try:
        X_input = preprocess_input(features)
        pred = model.predict(X_input.values)
        logger.info("Prediction successful. Result: %d", int(pred[0]))
        return {"prediction": int(pred[0])}
    except Exception as e:
        logger.exception("Prediction failed.")
        raise HTTPException(status_code=500, detail="Prediction error")
    

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
