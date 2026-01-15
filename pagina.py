# Página del 1er Coloquio de Literatura Queer Peruana

import streamlit as st
import pandas as pd
import folium 
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Coloquio de Literatura Queer Peruana",
    page_icon="📖🌈🇵🇪",
    layout="wide"
)

paginas = ["Presentación", "Calendario", "​Invitados"]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una sección', paginas)

if pagina_seleccionada == "Presentación":
    st.markdown("<h1 style='text-align: center; color:purple;'>1er Coloquio de Literatura Queer Peruana</h1>", unsafe_allow_html=True)
