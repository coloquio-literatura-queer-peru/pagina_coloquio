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
    st.markdown(f"<div style='text-align: justify; font-size: 70px; color: #a256d6;'>{lema_1}</div>", unsafe_allow_html=True)
    lema_2 = """
    Voces Queer en la Literatura Peruana
    """
    st.markdown(f"<div style='text-align: justify; font-size: 70px; color: #e65f46;'>{lema_2}</div>", unsafe_allow_html=True)
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
    .grid-card {
        text-align: center;
        padding: 12px;
    }
    
    .grid-card img {
        width: 100%;
        height: 260px;          /* Ajustar aquí el tamaño */
        object-fit: cover;
        border-radius: 12px;
    }
    
    .nombre {
    font-weight: 800;      /* Más negrita */
    font-size: 1.3rem;     /* Más grande */
    margin-top: 10px;
    }
    
    .rol {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 6px;
    }
    
    .correo {
        font-size: 0.85rem;
        color: #444;
    }
    </style>
    """, unsafe_allow_html=True)

    equipo = [
    {
        "nombre": "Julia Castillo",
        "rol": "Coordinación General",
        "correo": "castillo.julia@pucp.edu.pe",
        "foto": "https://revistakametsa.wordpress.com/wp-content/uploads/2024/01/image.png?w=484"
    },
    {
        "nombre": "André Mere",
        "rol": "Coordinación de comunicaciones y experiencias del público",
        "correo": "andremererivera@gmail.com",
        "foto": "https://ugc.production.linktr.ee/e3caa7b4-66b7-4f5f-b518-d3617ceb4440_IMG-20250117-231652.jpeg?io=true&size=avatar-v3_0"
    },
    {
        "nombre": "Alan Concepción",
        "rol": "Coordinación de producción y logísticas",
        "correo": "alan.concepcion@pucp.pe",
        "foto": "https://www.revistaotlet.com/wp-content/uploads/Alan_Concepcion-600x600.jpg"
    },
    {
        "nombre": "Serggio Juarez",
        "rol": "Coordinación académica",
        "correo": "serggioart@gmail.com",
        "foto": "https://w0.peakpx.com/wallpaper/216/720/HD-wallpaper-the-last-of-us-2-ellie-tlou.jpg"
    },
    {
        "nombre": "Luisa Gomez",
        "rol": "Coordinación de difusión y prensa",
        "correo": "luisa.gomez@pucp.edu.pe",
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
                <div class="correo">{persona['correo']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Segunda fila centrada (2)
    col4, col5, col6 = st.columns([1,1,1])
    
    with col4:
        persona = equipo[3]
        st.markdown(f"""
        <div class="grid-card">
            <img src="{persona['foto']}">
            <div class="nombre">{persona['nombre']}</div>
            <div class="rol">{persona['rol']}</div>
            <div class="correo">{persona['correo']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        persona = equipo[4]
    
        c1, c2, c3 = st.columns([1,2,1])
    
        with c2:
            st.image(persona["foto"], width=260)
            st.markdown(f"""
            <div class="grid-card">
                <div class="nombre">{persona['nombre']}</div>
                <div class="rol">{persona['rol']}</div>
                <div class="correo">{persona['correo']}</div>
            </div>
            """, unsafe_allow_html=True)

        
    with col6:
        st.empty()


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
