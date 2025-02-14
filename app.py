import streamlit as st
import fitz  # PyMuPDF pour lire les PDF
import numpy as np
import matplotlib.pyplot as plt

# 📌 1️⃣ Titre de l'application
st.title("📋 Évaluation des Facteurs Humains")
st.write("Téléversez un questionnaire rempli pour générer un diagramme radar.")

# 📌 2️⃣ Upload du fichier PDF
uploaded_file = st.file_uploader("📂 Téléversez le fichier PDF", type=["pdf"])

# 📌 3️⃣ Fonction pour extraire les réponses des champs du PDF
def extract_pdf_data(pdf_bytes):
    doc = fitz.open("pdf", pdf_bytes)  # Ouvrir le PDF depuis les données en mémoire
    fields = {}  # Stocker les réponses

    # 📌 Lire les champs de formulaire
    for page in doc:
        for widget in page.widgets():
            if widget.field_name and widget.text:
                fields[widget.field_name] = widget.text  # Associer champ et valeur

    return fields

# 📌 4️⃣ Génération du diagramme radar
def generate_radar_chart(data):
    labels = list(data.keys())
    values = [int(v) for v in data.values()]

    # Fermer la boucle du radar
    values.append(values[0])
    labels.append(labels[0])
    
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=True)

    # Création du radar chart
    fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'projection': 'polar'})
    ax.fill(angles, values, color='blue', alpha=0.3)
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticklabels([])
    ax.set_ylim(0, 4)  # Car les réponses vont de 1 à 4

    return fig

# 📌 5️⃣ Exécuter si un fichier est téléversé
if uploaded_file:
    # Extraire les réponses
    extracted_data = extract_pdf_data(uploaded_file.read())

    if extracted_data:
        # Afficher les réponses extraites
        st.subheader("📊 Données extraites")
        st.write(extracted_data)

        # Générer et afficher le radar chart
        st.subheader("📌 Diagramme Radar des Compétences")
        fig = generate_radar_chart(extracted_data)
        st.pyplot(fig)
    else:
        st.error("❌ Aucune donnée trouvée dans le PDF. Assurez-vous qu'il contient des réponses.")

