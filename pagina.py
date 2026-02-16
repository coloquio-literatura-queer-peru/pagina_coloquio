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

    st.markdown("<h1 style='text-align: center; color:#3f8c68;'>I Coloquio de</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:#d9307f;'>Literatura Peruana</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color:#f250c7;'> Queer</h1>", unsafe_allow_html=True)
    texto_1 = """
    El I Coloquio de Literatura Peruana Queer nace como un espacio de encuentro entre la investigación, la creación literaria y las experiencias artísticas de personas LGBTIQ+, con un énfasis en la literatura producida en el Perú. El coloquio busca visibilizar autorías disidentes, compartir miradas críticas y tejer redes entre escritorxs, investigadorxs y lectorxs, apostando por la construcción de una comunidad literaria más diversa, accesible e inclusiva.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_1}</div>", unsafe_allow_html=True)
