import os
import pandas as pd
from features.extract_features import extract_mfcc

def extract_label_from_filename(filename):
    # Prend la 6ème lettre majuscule du nom de fichier EMO-DB
    code = filename[5].upper()  # ex: 'F' dans '03a01Fa.wav'
    mapping = {
        'W': 'colere',
        'L': 'ennui',
        'E': 'degout',
        'A': 'peur',
        'F': 'joie',
        'T': 'tristesse',
        'N': 'neutre'
    }
    return mapping.get(code, 'inconnu')

def load_data_from_folder(folder):
    data = []
    labels = []
    for filename in os.listdir(folder):
        if filename.endswith('.wav'):
            path = os.path.join(folder, filename)
            label = extract_label_from_filename(filename)  # Mapping EMO-DB vers labels texte
            mfcc = extract_mfcc(path)
            data.append(mfcc)
            labels.append(label)
    return pd.DataFrame(data), labels