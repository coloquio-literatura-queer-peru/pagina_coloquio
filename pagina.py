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
    st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_1}</div>", unsafe_allow_html=True)

elif pagina_seleccionada == "Sobre nosotrxs":
    st.markdown("""
    <h1 style="
        font-size:75px;
        color:#a050f2;
        font-weight:900;
        text-align:center;
        margin-bottom:20px;
    ">
    Sobre Nosotrxs
    </h1>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg", use_container_width=True)
        st.markdown("""
        <div class="card">
            <div class="nombre">Julia Castillo</div>
            <div class="rol">Coordinación General</div>
            <p>Investigadora en literatura peruana contemporánea y estudios queer.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg", use_container_width=True)
        st.markdown("""
        <div class="card">
            <div class="nombre">André Mere</div>
            <div class="rol">Coordinación de comunicaciones y experiencias del público</div>
            <p>Gestor cultural especializada en proyectos interdisciplinarios.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.image("https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg", use_container_width=True)
        st.markdown("""
        <div class="card">
            <div class="nombre">Alan Concepción</div>
            <div class="rol">Coordinación de producción y logísticas</div>
            <p>Especialista en difusión cultural y estrategias digitales.</p>
        </div>
        """, unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.image("https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg", use_container_width=True)
        st.markdown("""
        <div class="card">
            <div class="nombre">Serggio Juarez</div>
            <div class="rol">Coordinación académica</div>
            <p>Especialista en difusión cultural y estrategias digitales.</p>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.image("fotos/me.jpg", width=100, use_container_width=True)
        st.markdown("""
        <div class="card">
            <div class="nombre">Luisa Gomez</div>
            <div class="rol">Coordinación de difusión y prensa</div>
            <p>Especialista en difusión cultural y estrategias digitales.</p>
        </div>
        """, unsafe_allow_html=True)
