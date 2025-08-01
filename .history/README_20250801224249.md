# 🎤 Reconnaissance des Émotions par la Voix

Un système de reconnaissance d'émotions basé sur l'analyse de la voix utilisant l'apprentissage profond et l'API FastAPI avec interface Streamlit.

## 🚀 Fonctionnalités

- **Analyse audio** : Extraction de caractéristiques MFCC
- **Modèle CNN-BiLSTM** : Architecture hybride pour la classification d'émotions
- **API REST** : Interface FastAPI pour les prédictions
- **Interface web** : Application Streamlit pour l'upload et la visualisation
- **Support EMO-DB** : Compatible avec le corpus Berlin Database of Emotional Speech

## 📋 Prérequis

- Python 3.8+
- pip
- Git

## 🛠️ Installation

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/emotion-voice-recognition.git
cd emotion-voice-recognition
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l'environnement virtuel

**Windows :**

```bash
venv\Scripts\activate
```

**Linux/Mac :**

```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 🎯 Utilisation

### 1. Entraîner le modèle

```bash
python train.py
```

### 2. Lancer l'API FastAPI

```bash
uvicorn main_api:app --reload
```

L'API sera accessible sur : http://localhost:8000

### 3. Lancer l'interface Streamlit

```bash
streamlit run app.py
```

L'interface sera accessible sur : http://localhost:8501

## 📁 Structure du projet

```
├── app.py                 # Interface Streamlit
├── main_api.py           # API FastAPI
├── train.py              # Script d'entraînement
├── requirements.txt      # Dépendances Python
├── README.md            # Documentation
├── .gitignore           # Fichiers à ignorer
├── data/
│   └── emodb/           # Données audio EMO-DB
├── features/
│   └── extract_features.py  # Extraction des caractéristiques
├── models/
│   ├── model_cnn_bilstm.py  # Architecture du modèle
│   ├── saved_model.h5       # Modèle entraîné
│   └── labels.json          # Mapping des labels
├── predictions/
│   └── predict.py           # Fonction de prédiction
└── utils/
    ├── audio_utils.py       # Utilitaires audio
    └── data_loader.py       # Chargement des données
```

## 🎵 Format des données

Le système utilise le corpus EMO-DB avec le mapping suivant :

- **W** = Wut (colère)
- **L** = Langeweile (ennui)
- **E** = Ekel (dégoût)
- **A** = Angst (peur)
- **F** = Freude (joie)
- **T** = Traurigkeit (tristesse)
- **N** = Neutral (neutre)

## 🔧 API Endpoints

### POST /predict

Upload un fichier audio (.wav) pour obtenir la prédiction d'émotion.

**Exemple de réponse :**

```json
{
  "prediction": 3,
  "label": "joie"
}
```

## 📊 Performance

- **Accuracy d'entraînement** : ~78%
- **Accuracy de validation** : ~66%
- **Architecture** : CNN + BiLSTM
- **Features** : MFCC (40 coefficients)

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Votre Nom** - [votre-email@example.com](mailto:votre-email@example.com)

## 🙏 Remerciements

- [EMO-DB](http://emodb.bilderbar.info/) pour le corpus de données
- [Librosa](https://librosa.org/) pour l'analyse audio
- [TensorFlow](https://tensorflow.org/) pour l'apprentissage profond
- [FastAPI](https://fastapi.tiangolo.com/) pour l'API
- [Streamlit](https://streamlit.io/) pour l'interface
