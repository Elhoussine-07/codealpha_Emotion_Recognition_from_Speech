from utils.data_loader import load_data_from_folder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from models.model_cnn_bilstm import create_model
import numpy as np
import os

# Load data uniquement depuis emo
# db
data_emodb, labels_emodb = load_data_from_folder("data/emodb")

X = data_emodb.values
y = labels_emodb

le = LabelEncoder()
y_encoded = le.fit_transform(y)
print("Ordre des labels utilisé par le modèle :", list(le.classes_))
y_cat = to_categorical(y_encoded)

X_train, X_test, y_train, y_test = train_test_split(X, y_cat, test_size=0.2)

# Train model
model = create_model((X.shape[1],), num_classes=y_cat.shape[1])
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_test, y_test))
model.save("models/saved_model.h5")
