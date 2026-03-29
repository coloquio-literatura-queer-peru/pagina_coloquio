# Página del 1er Coloquio de Literatura Queer Peruana

import streamlit as st
import pandas as pd
import folium 
import streamlit.components.v1 as components
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Coloquio Literatura PE",
    page_icon="🌈",
    layout="wide"
)

st.markdown("""
    <style>
    /* Texto dentro del selectbox */
    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        font-size: 18px !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown(
    "<p style='font-size:18px; font-weight:bold;'>Selecciona una sección</p>",
    unsafe_allow_html=True
)

paginas = ["Presentación", "Equipo organizador", "Convocatoria de sumillas", "Programa"]

with st.sidebar:
    pagina_seleccionada = option_menu(
        menu_title=None,
        options=paginas,
        icons=['house','person','file-earmark-arrow-up','calendar'],
        default_index=0
    )

 
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
    
    st.write("")
        
    texto_1 = """
    El I Coloquio de Literatura Peruana Queer nace como un espacio de encuentro entre la investigación, la creación literaria y las representaciones artísticas de personas LGBTIQ+. 
    Este coloquio busca visibilizar autorías disidentes, compartir miradas críticas y tejer redes entre escritores, investigadores y lectores, apostando por la construcción de una comunidad literaria más diversa, accesible e inclusiva.
    El evento se desarrollará el 19, 20 y 21 de junio de 2026.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 22px'>{texto_1}</div>", unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#9a62a5;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        ORGANIZADORES
        </h2>
    """, unsafe_allow_html=True)
        
    col13, col14, col15, col16, col17 = st.columns(5)
    with col13:
        st.image("fotos/logo_redlit.png")
    with col14:
        st.image("fotos/logo_archivo.png")
    with col15:
        st.image("fotos/logo_fuego.png")
    with col16:
        st.image("fotos/logo_capricornios.png")
    with col17:
        st.image("fotos/logo_bibliotecas_con_orgullo.png")
    
    st.write("")
    
    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#3F8C68;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        ALIADOS
        </h2>
    """, unsafe_allow_html=True)
    
    col18, col19, col20, col21 = st.columns(4)
    with col18:
        st.image("fotos/logo_tengo_dos_mamas.png")
    with col19:
        st.image("fotos/logo_demus.png")
    with col20:
        st.image("fotos/logo_justicia_arcoiris.png")
    with col21:
        st.image("fotos/logo_mhol.png")
        
    col22, col23, col24 = st.columns([0.8,0.8,0.8])
    with col22:
        st.image("fotos/logo_impulse.png", use_container_width=True)
    with col23:
        st.image("fotos/logo_ahf.png", use_container_width=True)
    with col24:
        st.image("fotos/logo_promsex.png", use_container_width=True)

    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#dc2f82;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        EDITORIALES ALIADAS
        </h2>
    """, unsafe_allow_html=True)
    
    col26, col27, col28 = st.columns([0.8,0.5,0.68])
    with col26:
        st.image("fotos/logo_fce.png")
    with col28:
        st.image("fotos/logo_gafas_moradas.png")
        
elif pagina_seleccionada == "Equipo organizador":
    st.markdown("""
        <h1 style="
            font-size:65px;
            color:#9a62a5;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        Equipo organizador
        </h1>
    """, unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.image("fotos/foto_julia.png", width=300)
        st.markdown("<div style='width:300px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Julia Castillo</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:340px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación General</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:360px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>castillo.julia@pucp.edu.pe</div>",unsafe_allow_html=True)
     
    with col5:
        st.image("fotos/foto_andre.png", width=300)
        st.markdown("<div style='width:380px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>André Mere Rivera</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:420px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Comunicaciones</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:380px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>y Experiencias del Público</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:400px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>andremererivera@gmail.com</div>",unsafe_allow_html=True)
            
    with col6:
        st.image("fotos/foto_alan.png", width=300)
        st.markdown("<div style='width:340px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Alan Concepción</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:380px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Producción</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:280px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'> y Logística</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:350px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>alan.concepcion@pucp.pe</div>",unsafe_allow_html=True)
    
    st.write("")
        
    # Segunda fila
    col7, col8, col9 = st.columns([1,1,1])
    with col7:
        st.image("fotos/foto_serggio.png", width=400)
        st.markdown("<div style='width:180px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Serggio Juarez</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:210px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación Académica</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>serggioart@gmail.com</div>",unsafe_allow_html=True)
           
    with col8:
        st.image("fotos/foto_luisa.png", width=400)
        st.markdown("<div style='width:200px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Luisa Gomez</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:440px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Difusión y Prensa</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:380px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>luisa.gomez@pucp.edu.pe</div>",unsafe_allow_html=True)
    
elif pagina_seleccionada == "Convocatoria de sumillas":
    st.markdown("""
        <h1 style="
            font-size:60px;
            color:#9a62a5;
            font-weight:900;
            text-align:center;
            margin-bottom:20px;
        ">
        Convocatoria de sumillas
        </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:40px;
            color:#3f8c68;
            font-weight:900;
            text-align:center;
            margin-bottom:20px;
        ">
        Bases para el envío de sumillas
        </h2>
    """, unsafe_allow_html=True)
        
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p> A pesar del crecimiento de eventos académicos y culturales en el Perú, persisten importantes vacíos en la programación vinculada a las disidencias sexuales y de género, particularmente en el ámbito literario. 
        Las propuestas existentes suelen estar marcadas por enfoques generalistas, sin una atención sostenida a las voces queer ni a las escrituras que tensionan los marcos heteronormativos de representación. 
        Asimismo, la programación cultural tiende a concentrarse en autores y temas ya legitimados, dejando de lado producciones que emergen desde los márgenes, muchas veces autoeditadas, comunitarias o vinculadas a experiencias de precariedad, exclusión y violencia.
        
        Además, cuando se abordan temas de diversidad sexual o queer en eventos académicos, suelen hacerse desde un enfoque externo, desvinculado de las trayectorias de personas, activistas, escritores/as disidentes o colectivos culturales. 
        Esto contribuye a una circulación parcial, fragmentaria o exotizada de las literaturas queer.
        
        En ese contexto, el I Coloquio de Literatura Peruana Queer, proyecto ganador de los Estímulos Económicos para el Libro y Fomento de la Lectura 2025 del Ministerio de Cultura, busca atender estas limitaciones mediante una programación que, si bien parte de la investigación académica, la combina con  producciones literarias y experiencias artísticas de sujetos LGBTIQ+ o queer, con un énfasis específico en la literatura peruana, manejando el concepto amplio de “literatura” (que considera las publicaciones independientes, fanzines, novelas gráficas y todo texto “no canónico”). 
        Este primer coloquio crea un espacio interdisciplinario y descentralizado dentro de los circuitos hegemónicos, promoviendo las memorias y reflexiones, la visibilidad de autorías disidentes, la difusión de estudios críticos y la articulación de redes entre creadores/as, investigadores/as y lectores/as. Al hacerlo, contribuye a democratizar el acceso y la representación en el campo literario, desde una mirada situada y plural en el contexto peruano. 
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#d92958;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Objetivos
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <ul>
        <li>Analizar críticamente obras literarias peruanas que abordan experiencias, identidades y subjetividades queer desde diversas perspectivas teóricas y metodológicas. </li>
        <li>Fomentar el encuentro entre investigadores/as, estudiantes, escritores/as y público general interesados en la literatura y las disidencias sexuales y de género. </li>
        <li>Promover la difusión de estudios académicos y propuestas artísticas vinculadas a la literatura LGBTIQ+ en el Perú.</li>
        <li>Impulsar la visibilidad de autorías disidentes y la circulación de sus obras en espacios culturales y académicos.</li>
        <li>Contribuir a la construcción de redes de colaboración entre iniciativas literarias, culturales y comunitarias que trabajan desde perspectivas queer.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#73579d;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Comité Académico
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Entre las distintas actividades del I Coloquio de Literatura Peruana Queer, contaremos con mesas de investigación, en las que estudiantes de pregrado, posgrado e investigadores independientes compartirán sus proyectos de investigación.
        Cada participante enviará una sumilla (resumen) de su ponencia. 
        Nuestro comité académico revisará todas las sumillas enviadas y habrá un proceso de selección. 
        Las personas seleccionadas para las mesas de investigación serán notificadas anticipadamente para que puedan confirmar su participación en el evento.
        
        Nuestro comité académico está compuesto por
        </p>
        <ul>
        <li>Dra. Barrientos Silva, Aurea Violeta (Universidad de París VIII)</li>
        <li>Dr. Leonardo Loayza, Richard Angelo (Universidad Nacional Mayor de San Marcos)</li>
        <li>Dr. Suárez Trejo, Javier Teófilo (Universidad de Harvard)</li>
        <li>Lic. Juarez Garcia, Serggio Arturo (Pontificia Universidad Católica del Perú)</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#e55940;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Participantes
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        La convocatoria del I Coloquio de Literatura Peruana Queer está abierta a alumnos de pregrado, bachilleres, tesistas, licenciados, estudiantes de posgrado de cualquier universidad, así como también investigadores independientes (sin alguna filiación académica).
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#a154d6;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Ejes temáticos
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Las sumillas enviadas pueden abordar los siguientes temas. 
        Sin embargo, esta lista no es excluyente: si la ponencia aborda algún otro tema relacionado dentro del enfoque del coloquio, pasará a revisión.
        </p>
        <ol>
        <li>Construcción de identidades sexuales y de género</li>
        <li>Memorias disidentes y subjetividades marginales</li>
        <li>Literatura infantil queer</li>
        <li>Erotismo, poéticas del cuerpo y del deseo</li>
        <li>Amor y afectividad queer en la literatura</li>
        <li>Adaptaciones audiovisuales de obras literarias queer</li>
        <li>Campo editorial de literatura queer en el Perú</li>
        <li>Moral, control y censura frente a temáticas queer</li>
        <li>Lo marica antes de lo queer (escrituras disidentes antes de la existencia del concepto queer y de las disidencias sexo-genéricas)</li>
        <li>Literatura, feminismo y disidencias sexo-genéricas</li>
        <li>Literatura disidente en entornos digitales, entre otros</li>
        </ol>
        <p> Si bien se trata de un coloquio de literatura, el evento busca ser interdisciplinario, por lo que también se aceptarán investigaciones desde ramas afines (e.g. humanidades, sociología, antropología, entre otros), cuyo objeto de estudio sea la literatura.
        </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#3f8c68;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Lineamientos
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        Las sumillas que sean enviadas deben cumplir con los siguientes criterios:
        </p>
        <ul>
        <li>Formato Word o PDF a espacio 1.5 con fuente Times New Roman tamaño 12.</li>
        <li>El título de la ponencia debe ir centrado en negrita y en mayúsculas</li>
        <li>Debajo del título y centrado, se debe señalar 
        <ol>
        <li> Nombre del autor/a </li>
        <li> Programa de pregrado o posgrado al que pertenece </li> 
        <li> Nombre del centro de estudios </li>
        <li> Correo institucional </li> 
        </ol>
        Cada dato en una línea. Si el participante no tiene un vínculo académico, puede colocar el nombre de la institución a la que pertenezca o, en su defecto, no colocar nada. 
        Asimismo, en vez del correo institucional académico puede colocar el correo de preferencia (personal o de alguna otra institución). 
        En ese caso serían tres (03) líneas.</li>
        <li>La sumilla debe tener hasta 350 palabras y debe consignar la información principal de la investigación (el objeto de estudio, el tema, la hipótesis, el objetivo, el método y, de ser posible, las conclusiones). Además, cada persona podrá presentar una (01) sola sumilla.</li>
        <li>Señalar hasta cinco (05) palabras clave.</li>
        <li>Señalar cinco (05) fuentes académicas utilizadas en formato APA o MLA.</li>
        <li>De ser escogida, la extensión de la ponencia en el evento será de quince (15) minutos. Se le pedirá a los ponentes que manden sus diapositivas hasta una semana antes del evento.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#d92958;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Fechas y horarios
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p> El I Coloquio de Literatura Peruana Queer se llevará a cabo los días 19, 20 y 21 de junio del 2026. 
        Los días viernes 19 y sábado 20 de junio se desarrollará en el horario de 03:00 pm a 08:30 pm, mientras que el domingo 21 de junio el evento se desarrollará desde las 02:00 pm hasta las 06:00 pm.
        </p>
        <b>El evento será presencial, por lo que se dará preferencia a ponentes que tengan disponibilidad para dicha modalidad en las fechas y horarios indicados.
        </b>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#e55940;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Plazos
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        | EVENTO | FECHA |
        |-------|------------|
        | Apertura de convocatoria | Sábado 28 de Febrero del 2026 |
        | Cierre de convocatoria | Domingo 29 de Marzo del 2026 (hasta las 11:59 pm) |
        | Confirmación de resultados | A partir del 13 de Abril del 2026 |
        | Envío de diapositivas (personas seleccionadas)| Hasta el 12 de Junio |
    """)
    
    st.markdown("""
        <h2 style="
            font-size:38px;
            color:#a154d6;
            font-weight:900;
            text-align:justify;
            margin-bottom:20px;
        ">
        Modo de envío
        </h2>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: justify; font-size:18px;">
        <p>
        El envío de sumillas se hará a través del siguiente formulario: 
        </p>
        </div>
    """, unsafe_allow_html=True)
        
    col10, col11, col12 = st.columns(3)
    
    with col11:
        st.link_button(
            "Envia aquí tu sumilla",
            "https://docs.google.com/forms/d/e/1FAIpQLSeyzQjEVs7TLXRyZw8-D2AvKf2Hz9FzV-0iYmXaZ3CZG_ynAg/viewform?usp=dialog"
        )
        
st.markdown("""
<hr style="margin-top:60px; margin-bottom:20px;">

<div style="
    text-align:center;
    font-size:18px;
    color:#555;
    padding-bottom:20px;
">
    <p> Más información y consultas: </p>
    📩 coloquio.literatura.queer.pe@gmail.com <br>
    📷 <a href="https://instagram.com/literaturaperuqueer/" 
          target="_blank" 
          style="text-decoration:none; color:#d9307f; font-weight:600;">
          @literaturaperuqueer
    </a>
</div>
""", unsafe_allow_html=True)
