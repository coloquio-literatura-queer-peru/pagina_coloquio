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

    st.markdown("""
    <style>
    .miembro {
    display: flex;
    flex-direction: column;
    align-items: center;   /* centra TODO horizontalmente */
    justify-content: center;
    margin-bottom: 7px; 
    }
    
    .miembro img {
        width: 240px;
        height: 300px;   /* proporción 4:5 */
        object-fit: cover;
        display: block;
        border-radius: 14px;
    }
    
    .nombre {
    font-weight: 900;       /* más bold */
    font-size: 1.4rem;      /* más grande */
    margin-top: 14px;
    text-align: center;
    }
    
    .rol {
        font-size: 1rem;
        color: #2E5AAC;         /* azul elegante */
        margin-top: 6px;
        text-align: center;
    }
    
    .correo {
        font-size: 0.9rem;
        color: #777777;         /* gris suave */
        margin-top: 4px;
        text-align: center;
    }
    
    </style>
    """, unsafe_allow_html=True)

    equipo = [
    {
        "nombre": "Julia Castillo",
        "rol": "Coordinación General",
        "correo": "castillo.julia@pucp.edu.pe",
        "foto": "fotos/foto_julia.png"
    },
    {
        "nombre": "André Mere",
        "rol": "Coordinación de comunicaciones y experiencias del público",
        "correo": "andremererivera@gmail.com",
        "foto": "fotos/foto_andre.png"
    },
    {
        "nombre": "Alan Concepción",
        "rol": "Coordinación de producción y logísticas",
        "correo": "alan.concepcion@pucp.pe",
        "foto": "fotos/foto_alan.jpeg"
    },
    {
        "nombre": "Serggio Juarez",
        "rol": "Coordinación académica",
        "correo": "serggioart@gmail.com",
        "foto": "fotos/foto_serggio.png"
    },
    {
        "nombre": "Luisa Gomez",
        "rol": "Coordinación de difusión y prensa",
        "correo": "luisa.gomez@pucp.edu.pe",
        "foto": "fotos/foto_luisa.jpg"
    }
    ]

    # Primera fila (3)
    cols = st.columns(3, gap="small") 

    for col, persona in zip(cols, equipo[:3]):
        with col:
            st.image(persona["foto"], width=260)
            st.markdown(f"""
            <div style="text-align:center; margin-bottom:40px;">
                <div class="nombre">{persona['nombre']}</div>
                <div class="rol">{persona['rol']}</div>
                <div class="correo">{persona['correo']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Segunda fila centrada (2)
    cols2 = st.columns([1,2,2,1])

    for col, persona in zip(cols2[1:3], equipo[3:]):
        with col:
            st.image(persona["foto"], width=260)
            st.markdown(f"""
            <div style="text-align:center; margin-bottom:40px;">
                <div class="nombre">{persona['nombre']}</div>
                <div class="rol">{persona['rol']}</div>
                <div class="correo">{persona['correo']}</div>
            </div>
            """, unsafe_allow_html=True)


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
