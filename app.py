import streamlit as st
import pandas as pd

# Titre de votre application
st.title("Gestionnaire de Patients")

# Chargement du fichier
df = pd.read_excel("Liste_Patients_Test.xlsx")

# Affichage des données
st.write("Voici la liste de vos patients :")
st.dataframe(df)

# Petit bouton pour tester l'interactivité
if st.button("Afficher un message"):
    st.success("L'application fonctionne parfaitement !")
