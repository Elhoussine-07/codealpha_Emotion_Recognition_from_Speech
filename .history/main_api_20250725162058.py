from fastapi import FastAPI, UploadFile, File
from predictions.predict import predict_emotion
import tempfile
import numpy as np

EMOTIONS = [
    "colère",    # 0
    "dégoût",    # 1
    "peur",      # 2
    "joie",      # 3
    "tristesse", # 4
    "surprise",  # 5
    "neutre"     # 6
]

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(..)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(await file.read())
    temp.close()
    pred = predict_emotion(temp.name)
    return {"prediction": pred, "label": EMOTIONS[pred]}