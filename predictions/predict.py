from tensorflow.keras.models import load_model
from utils.audio_utils import preprocess_audio
import numpy as np
import json

def predict_emotion(audio_file, model_path="models/saved_model.h5"):
    model = load_model(model_path)
    features = preprocess_audio(audio_file)
    prediction = model.predict(np.expand_dims(features, axis=0))
    predicted_index = int(np.argmax(prediction))
    return predicted_index
