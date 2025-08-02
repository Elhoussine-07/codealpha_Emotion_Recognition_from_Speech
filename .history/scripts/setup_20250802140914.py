#!/usr/bin/env python3
"""
Script de configuration automatique du projet de reconnaissance d'émotions vocales
"""

import os
import sys
import zipfile
import requests
from pathlib import Path
import shutil

# Ajouter le répertoire parent au path pour importer config
sys.path.append(str(Path(__file__).parent.parent))

from config import *

def download_emodb_dataset():
    """
    Télécharger le dataset EMO-DB (simulation - URL fictive)
    En réalité, vous devrez télécharger manuellement depuis http://emodb.bilderbar.info/
    """
    print("📥 Téléchargement du dataset EMO-DB...")
    
    # Créer un fichier README pour expliquer comment obtenir les données
    readme_data = """# Données EMO-DB

Ce dossier contient les fichiers audio du corpus Berlin Database of Emotional Speech (EMO-DB).

## Comment obtenir les données

1. Visitez http://emodb.bilderbar.info/
2. Téléchargez le corpus complet
3. Extrayez les fichiers .wav dans ce dossier

## Structure attendue

```
data/emodb/
├── 03a01Fa.wav
├── 03a01Nc.wav
├── 03a01Wa.wav
└── ... (autres fichiers .wav)
```

## Format des noms de fichiers

Les noms de fichiers suivent le format : `XXaYYZz.wav`
- XX : Numéro de session
- a : Sexe du locuteur (a=male, b=female)
- YY : Numéro d'énoncé
- Z : Émotion (W=colère, L=ennui, E=dégoût, A=peur, F=joie, T=tristesse, N=neutre)
- z : Intensité (a=forte, b=moyenne, c=faible, d=très faible)

## Note

Les fichiers audio ne sont pas inclus dans ce repository pour des raisons de taille.
"""
    
    with open(EMODB_DIR / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_data)
    
    print("✓ Fichier README créé dans data/emodb/")
    print("⚠️  Veuillez télécharger manuellement les données depuis http://emodb.bilderbar.info/")

def create_sample_data():
    """Créer des données d'exemple pour les tests"""
    print("📝 Création de données d'exemple...")
    
    # Créer un fichier d'exemple
    sample_data = {
        "emotions": ["colère", "ennui", "dégoût", "peur", "joie", "tristesse", "neutre"],
        "sample_files": [
            "03a01Fa.wav",  # joie forte
            "03a01Nc.wav",  # neutre faible
            "03a01Wa.wav",  # colère forte
        ],
        "total_files": 535,
        "sample_rate": 16000,
        "duration": 3.0
    }
    
    import json
    with open(DATA_DIR / "sample_data.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, indent=2, ensure_ascii=False)
    
    print("✓ Données d'exemple créées")

def setup_project():
    """Configuration complète du projet"""
    print("🚀 Configuration du projet de reconnaissance d'émotions vocales...")
    
    # Créer les répertoires
    create_directories()
    
    # Créer le dossier logs
    log_dir = PROJECT_ROOT / "logs"
    log_dir.mkdir(exist_ok=True)
    
    # Créer le dossier cache
    CACHE_DIR.mkdir(exist_ok=True)
    
    # Créer le dossier scripts s'il n'existe pas
    scripts_dir = PROJECT_ROOT / "scripts"
    scripts_dir.mkdir(exist_ok=True)
    
    # Télécharger les données
    download_emodb_dataset()
    
    # Créer des données d'exemple
    create_sample_data()
    
    # Créer un fichier .env.example
    env_example = """# Configuration de l'environnement
# Copiez ce fichier vers .env et modifiez les valeurs selon vos besoins

# Configuration de l'API
API_HOST=0.0.0.0
API_PORT=8000

# Configuration de la base de données (si applicable)
DATABASE_URL=sqlite:///./emotion_db.sqlite

# Configuration des logs
LOG_LEVEL=INFO

# Clés API (si nécessaire)
API_KEY=your_api_key_here
"""
    
    with open(PROJECT_ROOT / ".env.example", "w", encoding="utf-8") as f:
        f.write(env_example)
    
    print("✓ Fichier .env.example créé")
    
    print("\n🎉 Configuration terminée !")
    print("\n📋 Prochaines étapes :")
    print("1. Téléchargez les données EMO-DB depuis http://emodb.bilderbar.info/")
    print("2. Placez les fichiers .wav dans data/emodb/")
    print("3. Installez les dépendances : pip install -r requirements.txt")
    print("4. Entraînez le modèle : python train.py")
    print("5. Lancez l'API : python main_api.py")
    print("6. Lancez l'interface : streamlit run app.py")

if __name__ == "__main__":
    setup_project() 