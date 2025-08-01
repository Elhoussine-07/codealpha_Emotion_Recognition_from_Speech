from tensorflow.keras.models import load_model
from utils.audio_utils import preprocess_audio
import numpy as np
import json

def predict_emotion(audio_file, model_path="models/saved_model.h5"):
    model = load_model(model_path)
    features = preprocess_audio(audio_file)
    prediction = model.predict(np.expand_dims(features, axis=0))
    return prediction

# 🧠 train.py
from utils.data_loader import load_data_from_folder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from models.model_cnn_bilstm import create_model
import numpy as np
import os