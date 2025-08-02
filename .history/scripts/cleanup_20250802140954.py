#!/usr/bin/env python3
"""
Script de nettoyage du projet
"""

import os
import shutil
from pathlib import Path
import sys

# Ajouter le répertoire parent au path
sys.path.append(str(Path(__file__).parent.parent))

from config import *

def cleanup_cache():
    """Nettoyer les fichiers de cache"""
    print("🧹 Nettoyage des fichiers de cache...")
    
    cache_dirs = [
        CACHE_DIR,
        PROJECT_ROOT / "__pycache__",
        PROJECT_ROOT / ".pytest_cache",
        PROJECT_ROOT / ".mypy_cache",
    ]
    
    for cache_dir in cache_dirs:
        if cache_dir.exists():
            shutil.rmtree(cache_dir)
            print(f"✓ Supprimé: {cache_dir}")
    
    # Nettoyer les fichiers .pyc
    for pyc_file in PROJECT_ROOT.rglob("*.pyc"):
        pyc_file.unlink()
        print(f"✓ Supprimé: {pyc_file}")

def cleanup_logs():
    """Nettoyer les fichiers de logs"""
    print("📝 Nettoyage des logs...")
    
    log_dir = PROJECT_ROOT / "logs"
    if log_dir.exists():
        for log_file in log_dir.glob("*.log"):
            log_file.unlink()
            print(f"✓ Supprimé: {log_file}")

def cleanup_temp():
    """Nettoyer les fichiers temporaires"""
    print("🗑️ Nettoyage des fichiers temporaires...")
    
    temp_patterns = [
        "*.tmp",
        "*.temp",
        "*.bak",
        "*.backup",
        "*.old",
        "*.swp",
        "*.swo",
        "*~"
    ]
    
    for pattern in temp_patterns:
        for temp_file in PROJECT_ROOT.rglob(pattern):
            temp_file.unlink()
            print(f"✓ Supprimé: {temp_file}")

def cleanup_features():
    """Nettoyer les features extraites"""
    print("🎵 Nettoyage des features extraites...")
    
    feature_files = [
        MFCC_FEATURES_PATH,
        LABELS_FEATURES_PATH,
    ]
    
    for feature_file in feature_files:
        if feature_file.exists():
            feature_file.unlink()
            print(f"✓ Supprimé: {feature_file}")

def main():
    """Nettoyage complet du projet"""
    print("🚀 Nettoyage du projet de reconnaissance d'émotions vocales...")
    
    cleanup_cache()
    cleanup_logs()
    cleanup_temp()
    cleanup_features()
    
    print("\n🎉 Nettoyage terminé !")
    print("Le projet est maintenant prêt pour un commit propre.")

if __name__ == "__main__":
    main() 