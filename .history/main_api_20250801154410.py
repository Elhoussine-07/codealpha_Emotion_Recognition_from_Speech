from fastapi import FastAPI, UploadFile, File
from predictions.predict import predict_emotion
import tempfile
import numpy as np
import json

# Charge dynamiquement les labels depuis le fichier JSON
try:
    with open("models/labels.json", "r", encoding="utf-8") as f:
        EMOTIONS = json.load(f)
except FileNotFoundError:
    # Fallback si le fichier n'existe pas encore
    EMOTIONS = ["colere", "degout", "peur", "joie", "tristesse", "surprise", "neutre"]

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(await file.read())
    temp.close()
    pred = predict_emotion(temp.name)
    return {"prediction": pred, "label": EMOTIONS[pred]}