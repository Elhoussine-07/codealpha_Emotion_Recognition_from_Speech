from features.extract_features import extract_mfcc
import numpy as np

def preprocess_audio(file_path):
    return extract_mfcc(file_path)