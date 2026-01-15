# Página del 1er Coloquio de Literatura Queer Peruana

import streamlit as st
import pandas as pd
import folium 
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Coloquio de Literatura Queer Peruana",
    page_icon="📖🌈",
    layout="wide"
)

paginas = ["Presentación", "Calendario", "​Invitados"]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una sección', paginas)

if pagina_seleccionada == "Presentación":
    st.markdown("<h1 style='text-align: center; color:purple;'>1er Coloquio de Literatura Queer Peruana</h1>", unsafe_allow_html=True)

    texto_1 = """
    El I Coloquio de Literatura Queer Peruana nace como un espacio de encuentro entre la investigación, la creación literaria y las experiencias artísticas de personas LGBTIQ+, con un enfoque en la literatura peruana. El coloquio busca visibilizar autorías disidentes, compartir miradas críticas y tejer redes entre escritoras/es, investigadoras/es y lectoras/es, apostando por una escena literaria más diversa, accesible y plural.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_1}</div>", unsafe_allow_html=True)
