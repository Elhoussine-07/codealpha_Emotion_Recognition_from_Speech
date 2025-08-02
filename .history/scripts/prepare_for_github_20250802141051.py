#!/usr/bin/env python3
"""
Script pour préparer le projet pour l'importation sur GitHub
"""

import os
import shutil
import subprocess
from pathlib import Path
import sys

# Ajouter le répertoire parent au path
sys.path.append(str(Path(__file__).parent.parent))

from config import *

def check_git_status():
    """Vérifier le statut Git"""
    print("🔍 Vérification du statut Git...")
    
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ Git est initialisé")
            return True
        else:
            print("⚠️ Git n'est pas initialisé")
            return False
    except FileNotFoundError:
        print("❌ Git n'est pas installé")
        return False

def initialize_git():
    """Initialiser Git si nécessaire"""
    if not check_git_status():
        print("🚀 Initialisation de Git...")
        subprocess.run(['git', 'init'])
        print("✓ Git initialisé")

def cleanup_before_commit():
    """Nettoyer avant le commit"""
    print("🧹 Nettoyage avant commit...")
    
    # Exécuter le script de nettoyage
    cleanup_script = PROJECT_ROOT / "scripts" / "cleanup.py"
    if cleanup_script.exists():
        subprocess.run([sys.executable, str(cleanup_script)])
    
    print("✓ Nettoyage terminé")

def check_file_sizes():
    """Vérifier la taille des fichiers"""
    print("📊 Vérification de la taille des fichiers...")
    
    large_files = []
    for file_path in PROJECT_ROOT.rglob("*"):
        if file_path.is_file() and not file_path.name.startswith('.'):
            size_mb = file_path.stat().st_size / (1024 * 1024)
            if size_mb > 50:  # Plus de 50MB
                large_files.append((file_path, size_mb))
    
    if large_files:
        print("⚠️ Fichiers volumineux détectés:")
        for file_path, size_mb in large_files:
            print(f"  - {file_path}: {size_mb:.1f}MB")
        print("Ces fichiers peuvent causer des problèmes sur GitHub.")
    else:
        print("✓ Aucun fichier volumineux détecté")

def create_github_workflow():
    """Créer un workflow GitHub Actions"""
    print("⚙️ Création du workflow GitHub Actions...")
    
    workflow_dir = PROJECT_ROOT / ".github" / "workflows"
    workflow_dir.mkdir(parents=True, exist_ok=True)
    
    workflow_content = """name: Tests et déploiement

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Configuration Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Installation des dépendances
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Configuration du projet
      run: |
        python scripts/setup.py
    
    - name: Tests (si disponibles)
      run: |
        echo "Tests à implémenter"
        # python -m pytest tests/
    
    - name: Vérification de la structure
      run: |
        python -c "from config import *; create_directories(); print('Structure OK')"
"""
    
    workflow_file = workflow_dir / "ci.yml"
    with open(workflow_file, "w", encoding="utf-8") as f:
        f.write(workflow_content)
    
    print("✓ Workflow GitHub Actions créé")

def create_issue_templates():
    """Créer des templates d'issues GitHub"""
    print("📝 Création des templates d'issues...")
    
    templates_dir = PROJECT_ROOT / ".github" / "ISSUE_TEMPLATE"
    templates_dir.mkdir(parents=True, exist_ok=True)
    
    # Template de bug
    bug_template = """---
name: 🐛 Bug report
about: Signaler un bug
title: '[BUG] '
labels: ['bug']
assignees: ''
---

## Description du bug
Une description claire et concise du bug.

## Étapes pour reproduire
1. Aller à '...'
2. Cliquer sur '...'
3. Faire défiler jusqu'à '...'
4. Voir l'erreur

## Comportement attendu
Une description claire de ce qui devrait se passer.

## Captures d'écran
Si applicable, ajoutez des captures d'écran pour expliquer votre problème.

## Environnement
- OS: [ex: Windows 10]
- Python: [ex: 3.9.0]
- Version du projet: [ex: 1.0.0]

## Informations supplémentaires
Ajoutez tout autre contexte sur le problème ici.
"""
    
    # Template de feature
    feature_template = """---
name: ✨ Feature request
about: Suggérer une nouvelle fonctionnalité
title: '[FEATURE] '
labels: ['enhancement']
assignees: ''
---

## Description de la fonctionnalité
Une description claire et concise de la fonctionnalité souhaitée.

## Problème résolu
Une description claire du problème que cette fonctionnalité résoudrait.

## Solution proposée
Une description claire de la solution souhaitée.

## Alternatives considérées
Une description claire de toutes les solutions alternatives que vous avez considérées.

## Informations supplémentaires
Ajoutez tout autre contexte ou captures d'écran sur la demande de fonctionnalité ici.
"""
    
    with open(templates_dir / "bug_report.md", "w", encoding="utf-8") as f:
        f.write(bug_template)
    
    with open(templates_dir / "feature_request.md", "w", encoding="utf-8") as f:
        f.write(feature_template)
    
    print("✓ Templates d'issues créés")

def main():
    """Préparation complète pour GitHub"""
    print("🚀 Préparation du projet pour GitHub...")
    
    # Initialiser Git si nécessaire
    initialize_git()
    
    # Nettoyer avant commit
    cleanup_before_commit()
    
    # Vérifier la taille des fichiers
    check_file_sizes()
    
    # Créer le workflow GitHub Actions
    create_github_workflow()
    
    # Créer les templates d'issues
    create_issue_templates()
    
    print("\n🎉 Préparation terminée !")
    print("\n📋 Prochaines étapes pour GitHub :")
    print("1. Ajouter tous les fichiers : git add .")
    print("2. Faire le premier commit : git commit -m 'Initial commit'")
    print("3. Créer un repository sur GitHub")
    print("4. Ajouter l'origin : git remote add origin <URL_GITHUB>")
    print("5. Pousser vers GitHub : git push -u origin main")
    print("\n⚠️  N'oubliez pas de télécharger les données EMO-DB après avoir cloné le repository !")

if __name__ == "__main__":
    main() 