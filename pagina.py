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
    st.markdown("""
    <style>
    .titulo-container {
        text-align: center;
        line-height: 0.9;
        font-weight: 900;
    }
    
    .titulo1 {
        color: #3f8c68;
        font-size: 80px;
        margin-bottom: -20px;
        position: relative;
        z-index: 1;
    }
    
    .titulo2 {
        color: #d9307f;
        font-size: 75px;
        margin-bottom: -25px;
        position: relative;
        z-index: 2;
    }
    
    .titulo3 {
        color: #f250c7;
        font-size: 68px;
        position: relative;
        z-index: 3;
    }
    </style>
    
    <div class="titulo-container">
        <div class="titulo1">I Coloquio de</div>
        <div class="titulo2">Literatura Peruana</div>
        <div class="titulo3">Queer</div>
    </div>
    """, unsafe_allow_html=True)
    texto_1 = """
    El I Coloquio de Literatura Peruana Queer nace como un espacio de encuentro entre la investigación, la creación literaria y las experiencias artísticas de personas LGBTIQ+, con un énfasis en la literatura producida en el Perú. El coloquio busca visibilizar autorías disidentes, compartir miradas críticas y tejer redes entre escritorxs, investigadorxs y lectorxs, apostando por la construcción de una comunidad literaria más diversa, accesible e inclusiva.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_1}</div>", unsafe_allow_html=True)
