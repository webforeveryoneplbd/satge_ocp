import streamlit as st
import pandas as pd

# Interface Streamlit
st.title('Gestion des Badges')

# Ajouter une option pour télécharger le fichier Excel
uploaded_file = st.file_uploader("Téléchargez le fichier Excel contenant les informations sur les badges", type="xlsx")

if uploaded_file is not None:
    # Charger le fichier Excel
    df = pd.read_excel(uploaded_file)

    # Identifier les numéros de badge disponibles
    tous_les_badges = set(range(32000, 46000))  # Remplacez 10000 par le nombre total de badges possibles
    badges_utilises = set(df['Numéro de badge'].unique())
    badges_disponibles = tous_les_badges - badges_utilises

    # Compter le nombre de fois où chaque agent a changé de badge
    changement_badges = df.groupby('Matricule')['Numéro de badge'].nunique()

    st.header('Numéros de badge disponibles')
    st.write(f"Il y a {len(badges_disponibles)} badges disponibles.")

    # Affichage des badges disponibles
    st.markdown("<ul>", unsafe_allow_html=True)
    for badge in badges_disponibles:
        st.markdown(f"<li>{badge}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.header('Nombre de changements de badge par agent')

    # Affichage du nombre de changements de badges
    st.markdown("<ul>", unsafe_allow_html=True)
    for matricule, nb_changements in changement_badges.items():
        st.markdown(f"<li>{matricule}: {nb_changements}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
else:
    st.warning("Veuillez télécharger un fichier Excel pour continuer.")
