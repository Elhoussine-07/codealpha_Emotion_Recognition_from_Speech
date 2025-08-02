# Guide de Contribution

## 🚀 Démarrage rapide

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/emotion-voice-recognition.git
cd emotion-voice-recognition
```

### 2. Configuration automatique

```bash
python scripts/setup.py
```

### 3. Environnement virtuel

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 4. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 5. Télécharger les données

Suivez les instructions dans `data/emodb/README.md` pour télécharger le dataset EMO-DB.

## 📁 Structure du projet

### Organisation des dossiers

- **`config.py`** : Configuration centralisée du projet
- **`data/`** : Données et datasets
  - `emodb/` : Fichiers audio EMO-DB (non inclus dans Git)
  - `sample_data.json` : Données d'exemple
- **`models/`** : Modèles entraînés et architecture
  - `model_cnn_bilstm.py` : Architecture du modèle
  - `saved_model.h5` : Modèle entraîné (généré)
- **`features/`** : Extraction de caractéristiques
- **`utils/`** : Utilitaires et helpers
- **`scripts/`** : Scripts de maintenance
  - `setup.py` : Configuration automatique
  - `cleanup.py` : Nettoyage du projet
  - `prepare_for_github.py` : Préparation pour GitHub
- **`predictions/`** : Logique de prédiction
- **`logs/`** : Fichiers de logs (créé automatiquement)
- **`.cache/`** : Cache (créé automatiquement)

### Fichiers de configuration

- **`.gitignore`** : Exclut les fichiers volumineux et temporaires
- **`config.py`** : Configuration centralisée
- **`.env.example`** : Exemple de variables d'environnement

## 🔧 Développement

### Ajouter une nouvelle fonctionnalité

1. Créer une branche feature :
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   ```

2. Développer la fonctionnalité

3. Tester localement :
   ```bash
   python scripts/cleanup.py
   python train.py  # Si vous modifiez l'entraînement
   ```

4. Commiter les changements :
   ```bash
   git add .
   git commit -m "feat: ajouter nouvelle fonctionnalité"
   ```

### Modifier la configuration

Toutes les configurations sont centralisées dans `config.py`. Modifiez ce fichier pour :

- Changer les paramètres audio
- Modifier l'architecture du modèle
- Ajuster les chemins
- Configurer l'API

### Ajouter de nouveaux scripts

Placez les nouveaux scripts dans le dossier `scripts/` et suivez la convention :

```python
#!/usr/bin/env python3
"""
Description du script
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.append(str(Path(__file__).parent.parent))

from config import *

def main():
    """Fonction principale"""
    pass

if __name__ == "__main__":
    main()
```

## 🧹 Maintenance

### Nettoyage régulier

```bash
python scripts/cleanup.py
```

Ce script supprime :
- Fichiers de cache Python
- Logs temporaires
- Fichiers de sauvegarde
- Features extraites (peuvent être régénérées)

### Avant chaque commit

```bash
python scripts/cleanup.py
git add .
git commit -m "votre message"
```

## 📊 Tests

### Tests manuels

1. **Test de l'API** :
   ```bash
   python main_api.py
   # Dans un autre terminal
   curl -X POST "http://localhost:8000/predict" -F "file=@test.wav"
   ```

2. **Test de l'interface** :
   ```bash
   streamlit run app.py
   ```

3. **Test d'entraînement** :
   ```bash
   python train.py
   ```

### Tests automatisés (à implémenter)

Créez un dossier `tests/` avec :
- `test_models.py` : Tests des modèles
- `test_features.py` : Tests d'extraction de features
- `test_api.py` : Tests de l'API

## 🚀 Déploiement

### Préparation pour GitHub

```bash
python scripts/prepare_for_github.py
```

Ce script :
- Nettoie le projet
- Vérifie la taille des fichiers
- Crée les workflows GitHub Actions
- Crée les templates d'issues

### Déploiement local

1. **API** :
   ```bash
   uvicorn main_api:app --host 0.0.0.0 --port 8000
   ```

2. **Interface** :
   ```bash
   streamlit run app.py --server.port 8501
   ```

## 📝 Documentation

### Mise à jour du README

Le `README.md` principal contient :
- Installation et configuration
- Utilisation de base
- Structure du projet
- API endpoints

### Documentation spécifique

- `data/emodb/README.md` : Instructions pour les données
- `models/README.md` : Instructions pour les modèles
- `CONTRIBUTING.md` : Ce guide

## 🐛 Dépannage

### Problèmes courants

1. **Erreur de module non trouvé** :
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   ```

2. **Fichiers audio manquants** :
   - Vérifiez `data/emodb/README.md`
   - Téléchargez depuis http://emodb.bilderbar.info/

3. **Modèle non trouvé** :
   ```bash
   python train.py
   ```

4. **Problèmes de mémoire** :
   - Réduisez `BATCH_SIZE` dans `config.py`
   - Utilisez moins d'époques

### Logs

Les logs sont dans `logs/app.log`. Vérifiez ce fichier pour diagnostiquer les problèmes.

## 🤝 Pull Requests

1. Fork le repository
2. Créer une branche feature
3. Développer et tester
4. Nettoyer avec `python scripts/cleanup.py`
5. Créer une Pull Request avec description détaillée

### Template de Pull Request

```markdown
## Description
Brève description des changements

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Amélioration de la documentation
- [ ] Refactoring

## Tests
- [ ] Tests locaux passés
- [ ] API testée
- [ ] Interface testée

## Checklist
- [ ] Code commenté
- [ ] Documentation mise à jour
- [ ] Nettoyage effectué
```

## 📞 Support

Pour toute question ou problème :
1. Vérifiez la documentation
2. Consultez les issues existantes
3. Créez une nouvelle issue avec le template approprié 