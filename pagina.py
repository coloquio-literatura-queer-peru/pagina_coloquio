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

    st.markdown("""
    <style>
    .grid-card {
        text-align: center;
        padding: 12px;
    }
    
    .grid-card img {
        width: 100%;
        height: 260px;          /* Ajusta aquí el tamaño */
        object-fit: cover;
        border-radius: 12px;
    }
    
    .nombre {
        font-weight: 600;
        margin-top: 10px;
    }
    
    .rol {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 6px;
    }
    
    .descripcion {
        font-size: 0.85rem;
        color: #444;
    }
    </style>
    """, unsafe_allow_html=True)

    equipo = [
    {
        "nombre": "Julia Castillo",
        "rol": "Coordinación General",
        "descripcion": "Investigadora en literatura peruana contemporánea y estudios queer.",
        "foto": "https://revistakametsa.wordpress.com/wp-content/uploads/2024/01/image.png?w=484"
    },
    {
        "nombre": "André Mere",
        "rol": "Coordinación de comunicaciones y experiencias del público",
        "descripcion": "Gestor cultural especializado en proyectos interdisciplinarios.",
        "foto": "https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg"
    },
    {
        "nombre": "Alan Concepción",
        "rol": "Coordinación de producción y logísticas",
        "descripcion": "Especialista en difusión cultural y estrategias digitales.",
        "foto": "https://www.revistaotlet.com/wp-content/uploads/Alan_Concepcion-600x600.jpg"
    },
    {
        "nombre": "Serggio Juarez",
        "rol": "Coordinación académica",
        "descripcion": "Especialista en difusión cultural y estrategias digitales.",
        "foto": "https://indiehoy.com/wp-content/uploads/2023/01/bella-ramsey-.jpg"
    },
    {
        "nombre": "Luisa Gomez",
        "rol": "Coordinación de difusión y prensa",
        "descripcion": "Especialista en difusión cultural y estrategias digitales.",
        "foto": "fotos/me.jpg"
    }
    ]

  

    # Primera fila (3)
    cols = st.columns(3)
    
    for col, persona in zip(cols, equipo[:3]):
        with col:
            st.markdown(f"""
            <div class="grid-card">
                <img src="{persona['foto']}">
                <div class="nombre">{persona['nombre']}</div>
                <div class="rol">{persona['rol']}</div>
                <div class="descripcion">{persona['descripcion']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Segunda fila centrada (2)
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        persona = equipo[3]
        st.markdown(f"""
        <div class="grid-card">
            <img src="{persona['foto']}">
            <div class="nombre">{persona['nombre']}</div>
            <div class="rol">{persona['rol']}</div>
            <div class="descripcion">{persona['descripcion']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        persona = equipo[4]
        st.image(persona["foto"], width=250)
        st.markdown(f"""
        <div class="nombre">{persona['nombre']}</div>
        <div class="rol">{persona['rol']}</div>
        <div class="descripcion">{persona['descripcion']}</div>
        """, unsafe_allow_html=True)
    with col3:
        st.empty()



