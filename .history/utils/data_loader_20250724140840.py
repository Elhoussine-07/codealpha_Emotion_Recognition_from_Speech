import os
import pandas as pd
from features.extract_features import extract_mfcc

def load_data_from_folder(folder):
    data = []
    labels = []
    for filename in os.listdir(folder):
        if filename.endswith('.wav'):
            path = os.path.join(folder, filename)
            label = filename[5]  # 6ème caractère pour EMO-DB
            mfcc = extract_mfcc(path)
            data.append(mfcc)
            labels.append(label)
    return pd.DataFrame(data), labels