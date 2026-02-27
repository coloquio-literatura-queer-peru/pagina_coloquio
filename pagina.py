# Página del 1er Coloquio de Literatura Queer Peruana

import streamlit as st
import pandas as pd
import folium 
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Literatura Peruana Queer",
    page_icon="📖🌈",
    layout="wide"
)

paginas = ["Presentación", "Sobre nosotrxs", "Calendario", "​Invitados"]
pagina_seleccionada = st.sidebar.selectbox('Selecciona una sección', paginas)

st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
}

img {
    margin-bottom: 5px !important;
}
</style>
""", unsafe_allow_html=True)

if pagina_seleccionada == "Presentación":
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.image("fotos/logo.png", width=1600)

    lema_1 = """
    Memoria desde los márgenes
    """
    st.markdown(f"<div style='text-align: center; font-size: 35px; color: #a256d6; font-weight: bold'>{lema_1}</div>", unsafe_allow_html=True)
    lema_2 = """
    Voces queer en la literatura peruana
    """
    st.markdown(f"<div style='text-align: center; font-size: 35px; color: #e65f46; font-weight: bold'>{lema_2}</div>", unsafe_allow_html=True)
    texto_1 = """
    El I Coloquio de Literatura Peruana Queer nace como un espacio de encuentro entre la investigación, la creación literaria y las experiencias artísticas de personas LGBTIQ+, con un énfasis en la literatura producida en el Perú. El coloquio busca visibilizar autorías disidentes, compartir miradas críticas y tejer redes entre escritorxs, investigadorxs y lectorxs, apostando por la construcción de una comunidad literaria más diversa, accesible e inclusiva.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_1}</div>", unsafe_allow_html=True)

elif pagina_seleccionada == "Sobre nosotrxs":
    st.markdown("""
    <h1 style="
        font-size:65px;
        color:#a050f2;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Equipo organizador
    </h1>
    """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3, gap="small")

    with col4:
        st.image("fotos/foto_julia.png", width=260)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:800;'>Julia Castillo</div>",unsafe_allow_html=True)
        st.markdown("Coordinación General")
        st.markdown("castillo.julia@pucp.edu.pe")
 
    with col5:
        st.image("fotos/foto_andre.png", width=260)
        st.markdown("<div style='width:260px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:800;'>André Mere Rivera</div>",unsafe_allow_html=True)
        st.markdown("Coordinación de Comunicaciones y Experiencias del Público")
        st.markdown("andremererivera@gmail.com")
        
    with col6:
        st.image("fotos/foto_alan.jpeg", width=260)
        st.markdown("<div style='width:260px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:800;'>Alan Concepción</div>",unsafe_allow_html=True)
        st.markdown("Coordinación de producción y logísticas")
        st.markdown("alan.concepcion@pucp.pe")
        
    # Segunda fila
    col7, col8 = st.columns(2)
    
    with col7:
        st.image("fotos/foto_serggio.png", width=260)
        st.markdown("<div style='width:280px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:800;'>Serggio Juarez</div>",unsafe_allow_html=True)
        st.markdown("Coordinación académica")
        st.markdown("serggioart@gmail.com")
        
    with col8:
        st.image("fotos/foto_luisa.jpeg", width=280)
        st.markdown("<div style='width:260px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:800;'>Luisa Gomez</div>",unsafe_allow_html=True)
        st.markdown("Coordinación de difusión y prensa")
        st.markdown("luisa.gomez@pucp.edu.pe")
    
 

st.markdown("""
<hr style="margin-top:60px; margin-bottom:20px;">

<div style="
    text-align:center;
    font-size:16px;
    color:#555;
    padding-bottom:20px;
">
    📩 coloquio.literatura.queer.pe@gmail.com <br>
    📷 <a href="https://instagram.com/literaturaperuqueer/" 
          target="_blank" 
          style="text-decoration:none; color:#d9307f; font-weight:600;">
          @literaturaperuqueer
    </a>
</div>
""", unsafe_allow_html=True)
