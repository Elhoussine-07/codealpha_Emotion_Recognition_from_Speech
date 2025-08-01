from fastapi import FastAPI, UploadFile, File
from predictions.predict import predict_emotion
import tempfile
import numpy as np
import json

with open("models/labels.json", "r", encoding="utf-8") as f:
    EMOTIONS = json.load(f)

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(await file.read())
    temp.close()
    pred = predict_emotion(temp.name)
    return {"prediction": pred, "label": EMOTIONS[pred]}