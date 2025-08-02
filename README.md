# Reconnaissance des Émotions par la Voix

Un système de reconnaissance d'émotions basé sur l'analyse de la voix utilisant l'apprentissage profond et l'API FastAPI avec interface Streamlit.

## Fonctionnalités

- **Analyse audio** : Extraction de caractéristiques MFCC
- **Modèle CNN-BiLSTM** : Architecture hybride pour la classification d'émotions
- **API REST** : Interface FastAPI pour les prédictions
- **Interface web** : Application Streamlit pour l'upload et la visualisation
- **Support EMO-DB** : Compatible avec le corpus Berlin Database of Emotional Speech

## Structure du projet

```
├── app.py                 # Interface Streamlit
├── main_api.py           # API FastAPI
├── train.py              # Script d'entraînement
├── config.py             # Configuration centralisée
├── requirements.txt      # Dépendances Python
├── README.md            # Documentation
├── .gitignore           # Fichiers à ignorer
├── .env.example         # Exemple de configuration
├── data/
│   ├── emodb/           # Données audio EMO-DB (non incluses)
│   │   ├── README.md    # Instructions de téléchargement
│   │   └── .gitkeep     # Maintient le dossier dans Git
│   └── sample_data.json # Données d'exemple
├── features/
│   └── extract_features.py  # Extraction des caractéristiques
├── models/
│   ├── model_cnn_bilstm.py  # Architecture du modèle
│   ├── README.md        # Instructions pour les modèles
│   └── .gitkeep         # Maintient le dossier dans Git
├── predictions/
│   └── predict.py           # Fonction de prédiction
├── scripts/
│   ├── setup.py         # Script de configuration
│   └── cleanup.py       # Script de nettoyage
├── utils/
│   ├── audio_utils.py       # Utilitaires audio
│   └── data_loader.py       # Chargement des données
├── logs/                # Fichiers de logs (créé automatiquement)
└── .cache/              # Cache (créé automatiquement)



