import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 📌 1️⃣ Evaluation Savoir-Être PFE
st.title("📝 Formulaire d'Évaluation & Diagramme Radar 📊")
st.write("Veuillez remplir le formulaire ci-dessous. Un diagramme radar sera généré en fonction de vos réponses.")

# 📌 2️⃣ Formulaire avec 5 critères
st.sidebar.header("📋 Répondez aux questions")
categories = ["Communication", "Travail d'équipe", "Gestion du stress", "Adaptabilité", "Compétences techniques"]
scores = []

with st.sidebar.form("Formulaire d'évaluation"):
    for category in categories:
        score = st.slider(f"{category} (0-10)", min_value=0, max_value=10, value=5)
        scores.append(score)
    submitted = st.form_submit_button("🔍 Générer le diagramme")

# 📌 3️⃣ Génération du diagramme radar si le formulaire est soumis
if submitted:
    # Convertir les données en format radar
    scores.append(scores[0])  # Boucle pour fermer le radar
    categories.append(categories[0])
    
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=True)

    # Création du diagramme radar
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'projection': 'polar'})
    ax.fill(angles, scores, color='blue', alpha=0.3)
    ax.plot(angles, scores, color='blue', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_yticklabels([])
    ax.set_ylim(0, 10)

    # Affichage du radar dans Streamlit
    st.subheader("📊 Résultat : Diagramme Radar")
    st.pyplot(fig)
