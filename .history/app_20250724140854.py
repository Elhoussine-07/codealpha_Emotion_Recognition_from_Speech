import streamlit as st
import requests

st.title("🎤 Reconnaissance des Émotions par la Voix")

uploaded_file = st.file_uploader("Choisissez un fichier .wav", type=["wav"])

if uploaded_file is not None:
    st.audio(uploaded_file)
    if st.button("Prédire l'émotion"):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("http://localhost:8000/predict", files=files)
        st.write("Résultat de la prédiction :", res.json())