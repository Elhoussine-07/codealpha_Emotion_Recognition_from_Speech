"""
Configuration du projet de reconnaissance d'émotions vocales
"""

import os
from pathlib import Path

# Chemins du projet
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
FEATURES_DIR = PROJECT_ROOT / "features"
UTILS_DIR = PROJECT_ROOT / "utils"
PREDICTIONS_DIR = PROJECT_ROOT / "predictions"

# Configuration des données
EMODB_DIR = DATA_DIR / "emodb"
EMODB_URL = "http://emodb.bilderbar.info/download/download.zip"  # URL fictive pour l'exemple
EMODB_FILENAME = "emodb.zip"

# Configuration du modèle
MODEL_PATH = MODELS_DIR / "saved_model.h5"
LABELS_PATH = MODELS_DIR / "labels.json"
MODEL_CONFIG_PATH = MODELS_DIR / "model_config.json"

# Configuration des features
FEATURE_EXTRACTOR_PATH = FEATURES_DIR / "extract_features.py"
MFCC_FEATURES_PATH = FEATURES_DIR / "mfcc_features.npy"
LABELS_FEATURES_PATH = FEATURES_DIR / "labels.npy"

# Configuration audio
SAMPLE_RATE = 16000
DURATION = 3.0  # secondes
N_MFCC = 40
HOP_LENGTH = 512
N_FFT = 2048

# Configuration du modèle CNN-BiLSTM
INPUT_SHAPE = (None, N_MFCC)
NUM_CLASSES = 7
EMBEDDING_DIM = 128
LSTM_UNITS = 64
DROPOUT_RATE = 0.3

# Mapping des émotions
EMOTION_MAPPING = {
    'W': 'colère',      # Wut
    'L': 'ennui',       # Langeweile
    'E': 'dégoût',      # Ekel
    'A': 'peur',        # Angst
    'F': 'joie',        # Freude
    'T': 'tristesse',   # Traurigkeit
    'N': 'neutre'       # Neutral
}

# Configuration de l'API
API_HOST = "0.0.0.0"
API_PORT = 8000
API_RELOAD = True

# Configuration Streamlit
STREAMLIT_PORT = 8501

# Configuration d'entraînement
BATCH_SIZE = 32
EPOCHS = 50
VALIDATION_SPLIT = 0.2
LEARNING_RATE = 0.001

# Créer les répertoires s'ils n'existent pas
def create_directories():
    """Créer tous les répertoires nécessaires"""
    directories = [
        DATA_DIR,
        EMODB_DIR,
        MODELS_DIR,
        FEATURES_DIR,
        UTILS_DIR,
        PREDICTIONS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✓ Répertoire créé/vérifié: {directory}")

# Configuration des logs
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = PROJECT_ROOT / "logs" / "app.log"

# Configuration de sécurité
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'.wav', '.mp3', '.flac', '.m4a'}

# Configuration de cache
CACHE_DIR = PROJECT_ROOT / ".cache"
CACHE_TTL = 3600  # 1 heure

if __name__ == "__main__":
    create_directories() 