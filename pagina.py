"""
Módulo: pagina.py
Descripción: Página web del I Coloquio de Literatura Queer Peruana
Autora: https://github.com/4591526 (luisa.gomez@pucp.edu.pe)
Fecha de creación: febrero 2026
"""

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
    col32, col33, col34, col35 = st.columns([0.8,0.8,0.8,0.8])
    with col35:
        st.image("fotos/logo_mincul.png")
    
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
            font-size:35px;
            color:#3F8C68;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        SEDES
        </h2>
    """, unsafe_allow_html=True)
    
    col19, col20, col21 = st.columns([1, 3, 1])
    with col20:
        subcol1, subcol2 = st.columns(2)
        with subcol1:
            st.image("fotos/sede_caslit.png")
        with subcol2:
            st.image("fotos/sede_mali.png")
        
    st.markdown("""
        <h2 style="
            font-size:35px;
            color:#dc2f82;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        EN ALIANZA CON
        </h2>
    """, unsafe_allow_html=True)
    
    col22, col23, col24, col25 = st.columns(4)
    with col22:
        st.image("fotos/logo_tengo_dos_mamas.png")
    with col23:
        st.image("fotos/logo_demus.png")
    with col24:
        st.image("fotos/logo_justicia_arcoiris.png")
    with col25:
        st.image("fotos/logo_mhol.png")
        
    col26, col27, col28 = st.columns([0.8,0.8,0.8])
    with col26:
        st.image("fotos/logo_impulse.png", use_container_width=True)
    with col27:
        st.image("fotos/logo_ahf.png", use_container_width=True)
    with col28:
        st.image("fotos/logo_promsex.png", use_container_width=True)

    st.markdown("""
        <h2 style="
            font-size:35px;
            color:#73579d;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        EDITORIALES ALIADAS
        </h2>
    """, unsafe_allow_html=True)
    
    col29, col30, col31 = st.columns([1, 3, 1])
    with col30:
        subcol3, subcol4 = st.columns(2)
        with subcol3:
            st.image("fotos/logo_fce.png")
        with subcol4:
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
    
    col4, col5, col6 = st.columns([1,1,1])
    
    with col4:
        st.image("fotos/foto_julia.png", width=400)
        st.markdown("<div style='width:180px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Julia Castillo</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación General</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:240px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>castillo.julia@pucp.edu.pe</div>",unsafe_allow_html=True)
     
    with col5:
        st.image("fotos/foto_andre.png", width=400)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>André Mere Rivera</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:280px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Comunicaciones</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>y Experiencias del Público</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:240px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>andremererivera@gmail.com</div>",unsafe_allow_html=True)
            
    with col6:
        st.image("fotos/foto_alan.png", width=400)
        st.markdown("<div style='width:210px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Alan Concepción</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:250px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Producción</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:130px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'> y Logística</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:220px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>alan.concepcion@pucp.pe</div>",unsafe_allow_html=True)
    
    st.write("")
        
    # Segunda fila
    col7, col8, col9 = st.columns([1,1,1])
    with col7:
        st.image("fotos/foto_serggio.png", width=400)
        st.markdown("<div style='width:180px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Serggio Juarez</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:230px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación Académica</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:205px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>serggioart@gmail.com</div>",unsafe_allow_html=True)
           
    with col8:
        st.image("fotos/foto_luisa.png", width=400)
        st.markdown("<div style='width:180px; margin:auto; text-align:left; font-size:24px; color:#dc2f82; font-weight:bold;'>Luisa Gomez</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:290px; margin:auto; text-align:left; font-size:18px; color:#3c8d6b; font-weight:bold;'>Coordinación de Difusión y Prensa</div>",unsafe_allow_html=True)
        st.markdown("<div style='width:230px; margin:auto; text-align:left; font-size:18px; color:#a154d6;'>luisa.gomez@pucp.edu.pe</div>",unsafe_allow_html=True)
    
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
    <div style="text-align: justify; font-size:18px; line-height:1.6;">
    
    <p>
    El <b>I Coloquio de Literatura Peruana Queer</b> se llevará a cabo los días 
    <b>19, 20 y 21 de junio de 2026</b> en las siguientes sedes y horarios:
    </p>
    
    <p>
    📅 <b>19 y 20 de junio</b><br>
    📍 Casa de la Literatura Peruana<br>
    🕒 3:00 p. m. – 8:30 p. m.
    </p>
    
    <p>
    📅 <b>21 de junio</b><br>
    📍 Museo de Arte de Lima (MALI)<br>
    🕒 2:00 p. m. – 6:00 p. m.
    </p>
    
    <p>
    <b>El evento se realizará en modalidad presencial, por lo que se dará preferencia 
    a los ponentes que cuenten con disponibilidad para participar en las fechas y horarios programados.</b>
    </p>
    
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
        | Apertura de convocatoria | Sábado 28 de febrero del 2026 |
        | Ampliación de convocatoria | Lunes 30 de marzo del 2026 |
        | Cierre de convocatoria | Lunes 13 de abril del 2026 (hasta las 11:59 pm) |
        | Confirmación de resultados | A partir del 4 de mayo del 2026 |
        | Envío de diapositivas (personas seleccionadas)| Hasta el 12 de junio del 2026|
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
    <b>La convocatoria para el envío de sumillas ha sido cerrada. Agradecemos el interés y la participación de todos los postulantes.</b>
    </p>
    </div>
    """, unsafe_allow_html=True)
        
    #col10, col11, col12 = st.columns(3)

else: 
    st.markdown("""
        <h2 style="
            font-size:45px;
            color:#DC2F82;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        CRONOGRAMA DE ACTIVIDADES
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .boton-centro {
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    
    .boton-centro a {
        background-color: #9A62A5;
        color: #F4E9E2;
        padding: 18px 35px;
        text-decoration: none;
        border-radius: 10px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        width: 500px;
    }
    
    .boton-centro a:hover {
        background-color: #885394;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
    """
    <div style="
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #9A62A5;">
        📢 Todas las actividades son de acceso libre y gratuito.
    </div>
    """,
    unsafe_allow_html=True
    )
    
    st.markdown("""
    <div class="boton-centro">
        <a href="https://forms.gle/hBszmpvcGnG1hvcSA" target="_blank">
            🎟️ Inscribirse aquí
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    
    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#DC2F82;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        VIERNES 19 DE JUNIO (CASA DE LA LITERATURA)
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            font-size:25px;
            color:#DC2F82;
            text-align:justify;
            margin-bottom:20px;
        ">
            El primer día del coloquio estará enfocado en la investigación académica sobre literatura
            peruana queer. La programación incluye dos mesas de ponencias dedicadas, por un lado, a
            las representaciones de feminidades queer en la literatura peruana contemporánea y, por
            otro, a relecturas queer de autores canónicos como Mario Vargas Llosa, José Diez Canseco
            y Oswaldo Reynoso. Asimismo, se presentarán muestras audiovisuales de investigación y se
            cerrará la jornada con un conversatorio sobre la historia de las disidencias sexuales y de
            género en el Perú, abordando sus representaciones, silencios y memorias antes de la
            consolidación de las categorías identitarias contemporáneas.
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    
    # Recepción
    st.markdown("""
    <div style="
        background-color: #E57A07;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>3:00 PM - 3:10 PM</strong><br> 
        Recepción de asistentes
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    #
    st.markdown("""
    <div style="
        background-color: #3C8E6C;
        color: #FAE9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>03:10 PM - 03:40 PM</strong><br> 
        Inauguración
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    #
    st.markdown("""
    <div style="
        background-color: #775aa4;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>03:50 PM - 04:05 PM / 06:55 PM - 07:05 PM</strong><br> 
        <div style="margin-top:10px;">
        MUESTRA AUDIOVISUAL
        </div>
        <div style="margin-top:10px;">
            <b><i>Lo queer en los Andes: entre la representación y el silencio en las ruralidades peruanas</i></b>
        </div>
        <div style="margin-top:10px;">
            Participa: Fátima Denisse Córdova Luna
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta investigación analiza las representaciones queer en los Andes peruanos y reflexiona
            sobre las formas de resistencia, memoria y diversidad sexual que emergen fuera de los
            espacios urbanos hegemónicos.
        </div>
    </div>
        """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #FFC88A;
        color: #dc2982;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>04:10 PM - 05:20 PM</strong><br> 
        <div style="margin-top:10px;">
        MESA DE PONENCIAS:
        <i>Feminidades queer en la literatura peruana contemporánea</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa reúne investigaciones en torno a las representaciones de feminidades queer en
            la literatura peruana contemporánea, atendiendo a las relaciones entre cuerpo, deseo,
            memoria y disidencia. A partir del análisis de narrativas y poéticas escritas por mujeres,
            las ponencias reflexionan sobre las formas en que las subjetividades lésbicas y queer se
            construyen en tensión con la violencia, la regulación social y las normas heteropatriarcales,
            así como sobre las estrategias de resistencia íntima y afirmación identitaria que emergen
            desde la escritura.
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>El egoísmo del cuerpo: poéticas del repliegue y disidencia en Matrioska de Valeria Román Marroquín</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Jimena Sofía Velarde Vera
        <a href="https://www.instagram.com/velarde_jimena/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@velarde_jimena)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>Estética queer y política del cuerpo en la narrativa de Doris Moromisato</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Judith Mavila Paredes Morales
        <a href="https://www.instagram.com/judithparedesmorales/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@judithparedesmorales)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>«Compórtense como señoritas» de K. Luy de Aliaga: formación de la subjetividad lésbica entre violencia y deseo</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Karol Nicol Sialas Rosas
        <a href="https://www.instagram.com/karol_sialas/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@karol_sialas)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            Modera: Camila Arizaca
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #FFC88A;
        color: #dc2982;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>05:40 PM - 06:50 PM</strong><br> 
        <div style="margin-top:10px;">
        MESA DE PONENCIAS:
        <i>Relecturas queer del canon peruano</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa propone revisitar el canon de la literatura peruana desde perspectivas queer
            contemporáneas, poniendo en discusión las formas en que el deseo, las sexualidades
            disidentes y las subjetividades no heteronormativas aparecen —muchas veces de manera
            ambigua, silenciada o marginal— en obras consideradas fundamentales de la tradición
            literaria peruana. A través de nuevas aproximaciones críticas a autores como Mario Vargas
            Llosa, José Diez Canseco y Oswaldo Reynoso, las ponencias exploran cómo el canon
            literario contiene tensiones, cuerpos y afectos que desestabilizan las lecturas hegemónicas
            de la sexualidad y la identidad.
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>El escándalo como motivo estructurante. Una relectura necesariamente ¿queer? de Vargas Llosa</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Fabio Venero Figueroa
        <a href="https://www.instagram.com/qvispe.ynca/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@qvispe.ynca)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>La representación de la bisexualidad en Duque (1934) de José Diez Canseco</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Natalia Regina Ángeles Enciso
        <a href="https://www.instagram.com/regi_ae07/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@regi_ae07)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>El deseo de la abyección: una lectura de la prostitución masculina desde la perrería del amor en «El triunfo» (2006) de Oswaldo Reynoso”</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Giancarlos Nathanael Peralta Luis
        <a href="https://www.instagram.com/nathanael.peralta.luis/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@nathanael.peralta.luis)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            Modera: Flavia Cabrera
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #dc2982;
        color: #fae9e2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>07:15 PM - 08:15 PM</strong><br> 
        <div style="margin-top:10px;">
        CONVERSATORIO:
        <i>Archivos y disidencias sexuales en la historia del Perú</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa propone una aproximación histórica a la diversidad sexual y de género en el
            Perú, a partir del análisis de expresiones literarias, artísticas y periodísticas que han
            representado formas de disidencia sexo-genérica en distintos momentos. Asimismo, busca
            reflexionar sobre cómo estas experiencias fueron nombradas, reguladas o silenciadas antes
            de la consolidación de las categorías contemporáneas de identidad.
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            Javier Lucierno/ Javi Vargas
        <a href="https://www.instagram.com/javi_vargas_st/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@javi_vargas_st)
        </a>
        </div>
        <div style="margin-top:10px;">
            Magally Alegre Henderson
        </div>
        <div style="margin-top:10px;">
            Hélard Fuentes
        <a href="https://www.instagram.com/helard.fuentes/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@helard.fuentes)
        </a>
        </div>
        <div style="margin-top:10px;">
            Modera: Giancarlo Mori Bolo
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    #############################
    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#e55940;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        SÁBADO 20 DE JUNIO (CASA DE LA LITERATURA)
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            font-size:25px;
            color:#e55940;
            text-align:justify;
            margin-bottom:20px;
        ">
            El segundo día del coloquio estará centrado en las representaciones contemporáneas de
            las disidencias sexo-genéricas en la literatura y la cultura. La programación incluye una
            mesa de ponencias dedicada a las escrituras trans y travestis como espacios de memoria,
            resistencia y construcción de archivo, así como un conversatorio sobre las representaciones
            de la diversidad sexual y de género en la literatura infantil y juvenil. Asimismo, se
            presentarán muestras audiovisuales de investigación y se realizará la proyección de la
            película No se lo digas a nadie (1998), seguida de un conversatorio que reflexionará sobre
            su lugar en la historia de las representaciones queer en el Perú y su vigencia dentro de los
            debates actuales sobre memoria, visibilidad y diversidad sexual.
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Recepción
    st.markdown("""
    <div style="
        background-color: #3C8E6C;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>3:00 PM - 3:05 PM</strong><br> 
        Recepción de asistentes
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    #
    st.markdown("""
    <div style="
        background-color: #FFC88A;
        color: #dc2982;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>03:05 PM - 04:15 PM</strong><br> 
        <div style="margin-top:10px;">
        MESA DE PONENCIAS:
        <i>Poéticas trans y travestis: memoria, cuerpo y resistencia</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa aborda las escrituras trans y travestis como espacios de memoria, resistencia y
            construcción de archivo frente a las violencias de la heteronormatividad y la colonialidad
            de género. A través del análisis de propuestas autobiográficas, poéticas y performáticas,
            las ponencias examinan cómo las narrativas trans contemporáneas articulan experiencias
            de exclusión, activismo, espiritualidad y autoafirmación, contribuyendo a la configuración
            de archivos alternativos y nuevas formas de representación de las disidencias sexogenéricas
            en el Perú y América Latina.
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>Del infierno al paraíso: espiritualidad y memoria trans en En el valle de las Onassis de Salò Tomoe</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Alejandra Romi Vargas Rojas
        <a href="https://www.instagram.com/scarlett.rza/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@scarlett.rza)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>«La Miss» de Lesly Quispe: el proceso de escritura de la primera autobiografía trans peruana</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: Ernesto Cuba
        <a href="https://www.instagram.com/ernesto.cuba/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@ernesto.cuba)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>Heterogeneidad marica: lenguaje queer como resistencia en Campuzano y Frau Diamanda</i></b>
        </div>
        <div style="margin-top:10px; color:#9a48d5">
            Participa: José Antonio Arias Bernal
        <a href="https://www.instagram.com/jaba94_/" target="_blank"
              style="text-decoration:none; color:#dc2982; font-weight:600;"> (@jaba94_)
        </a>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            Modera: Luis León Santos
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #775aa4;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>04:20 PM - 04:30 PM / 05:40 PM - 05:55 PM</strong><br> 
        <div style="margin-top:10px;">
        MUESTRA AUDIOVISUAL
        </div>
        <div style="margin-top:10px;">
            <b><i>Desprogramar el género: hyperpoesía, futurismo andino y subjetividades queer en la literatura digital peruana</i></b>
        </div>
        <div style="margin-top:10px;">
            Participa: Lisa Carrasco La Cruz
        <a href="https://www.instagram.com/fuegodecumbia/" target="_blank"
              style="text-decoration:none; color:#F4E9E2; font-weight:600;"> (@fuegodecumbia)
        </a>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta investigación analiza la literatura electrónica y la poesía digital como formas de
            experimentación estética que replantean las relaciones entre tecnología, lenguaje e
            identidades queer.
        </div>
    </div>
        """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #dc2982;
        color: #fae9e2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>04:35 PM - 05:35 PM</strong><br> 
        <div style="margin-top:10px;">
        CONVERSATORIO:
        <i>Infancia y diversidad: representaciones queer en la literatura infantil</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa propone reflexionar sobre la literatura queer dirigida a niños, niñas y
            adolescentes, atendiendo a sus formas de representación, circulación y recepción, y su
            papel en la construcción de imaginarios sobre la diversidad desde edades tempranas.
            Asimismo, busca problematizar el lugar de la diversidad sexual y de género en la literatura
            infantil y juvenil, así como los debates en torno a su visibilidad, mediación pedagógica y
            tensiones con discursos sociales contemporáneos.
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            Amanda Meza
        <a href="https://www.instagram.com/amanda_meza1/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@amanda_meza1)
        </a>
        </div>
        <div style="margin-top:10px;">
            Vero Ferrari
        <a href="https://www.instagram.com/veroferrarig/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@veroferrarig)
        </a>
        </div>
        <div style="margin-top:10px;">
            Lakita
        <a href="https://www.instagram.com/lakitatheartist/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@lakitatheartist)
        </a>
        </div>
        <div style="margin-top:10px;">
            Modera: Alan Concepción
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #E57A07;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>06:00 PM - 08:00 PM</strong><br> 
        <div style="margin-top:10px;">
        PROYECCIÓN DE PELÍCULA
        </div>
        <div style="margin-top:10px;">
            <b><i>No se lo digas a nadie (1998)</i></b>
        </div>
        <div style="margin-top:10px;">
            Dir. Francisco Lombardi
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #3c8e6c;
        color: #fae9e2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>08:00 PM - 08:30 PM</strong><br> 
        <div style="margin-top:10px;">
        CONVERSATORIO:
        <i>Memoria y representación queer a partir de No se lo digas a nadie (1998) de Francisco Lombardi</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            El conversatorio busca reflexionar sobre No se lo digas a nadie como obra cinematográfica
            (basada en una obra literaria) dentro de la historia de las representaciones queer en el
            Perú, considerando tanto su impacto cultural como las formas en que aborda la diversidad
            sexual, el deseo, la masculinidad y las tensiones sociales de su contexto. Asimismo, se busca
            poner en diálogo la película con las discusiones contemporáneas sobre memoria queer,
            visibilidad y representación en el Perú.
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            Fabs Reyna
        <a href="https://www.instagram.com/transudaka/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@transudaka)
        </a>
        </div>
        <div style="margin-top:10px;">
            Alberto Castro Antezana
        <a href="https://www.instagram.com/mc_zorro/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@mc_zorro)
        </a>
        </div>
        <div style="margin-top:10px;">
            Modera: Fer Wong
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    #########################################
    st.markdown("""
        <h2 style="
            font-size:30px;
            color:#775aa4;
            font-weight:bold;
            text-align:center;
            margin-bottom:20px;
        ">
        DOMINGO 21 DE JUNIO (MUSEO DE ARTE DE LIMA)
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            font-size:25px;
            color:#775aa4;
            text-align:justify;
            margin-bottom:20px;
        ">
            El último día del coloquio, que se desarrollará en el MALI, estará enfocado en la literatura
            y memorias queer contemporáneas en el Perú. Tendremos un conversatorio sobre literatura
            peruana queer emergente y nuevas voces actuales; luego, una presentación de libros
            vinculados a memorias y derechos LGTBIQ+ en el Perú; y, finalmente, un recital de poesía
            y narrativa queer como cierre artístico y literario de la jornada.
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Recepción
    st.markdown("""
    <div style="
        background-color: #E57A07;
        color: #F4E9E2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>02:00 PM - 02:10 PM</strong><br> 
        Recepción de asistentes
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    #
    st.markdown("""
    <div style="
        background-color: #dc2982;
        color: #fae9e2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>02:10 PM - 03:10 PM</strong><br> 
        <div style="margin-top:10px;">
        CONVERSATORIO:
        <i>Literatura peruana queer emergente: ¿qué se escribe hoy?</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Esta mesa propone un diálogo entre creación y crítica en torno a las nuevas voces de la
            literatura queer en el Perú, reuniendo a escritorxs y académicxs para reflexionar sobre las
            formas contemporáneas de representación de la diversidad sexual y de género, así como
            sobre los cruces entre producción literaria, lectura crítica y campo cultural.
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            Javier Suárez Trejo
        <a href="https://www.instagram.com/javisuarez888/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@javisuarez888)
        </a>
        </div>
        <div style="margin-top:10px;">
            Alexandra Arana Blas
        </div>
        <div style="margin-top:10px;">
            Salò Tomoe
        <a href="https://www.instagram.com/salotomoe/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@salotomoe)
        </a>
        </div>
        <div style="margin-top:10px;">
            Modera: Gustavo Ochoa Morán
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #FFC88A;
        color: #dc2982;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>03:30 PM - 04:15 PM</strong><br> 
        <div style="margin-top:10px;">
        PRESENTACIÓN DE LIBROS:
        <i>Voces queer en el Perú: historias no contadas</i>
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Espacio de diálogo en torno a publicaciones que recuperan memorias, experiencias y luchas
            de las comunidades LGTBIQ+ en el Perú. A partir de la presentación de estas obras, se
            reflexionará sobre la construcción de archivos, la defensa de derechos y la importancia de
            preservar y difundir historias que han sido tradicionalmente silenciadas.
        </div>
       <div style="margin-top:10px; color:#775aa4">
            <b><i>Resistimos porque recordamos. Relatoría del encuentro por las memorias LGTBIQ+ del Perú</i></b>
        </div>
        <div style="margin-top:10px; color:#775aa4">
            Autores: WikiAcción Perú y Archivo de la Memoria Marica del Perú
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            <b><i>¡No discriminarás! Crissthian Olivera Fuentes vs Perú</i></b>
        </div>
        <div style="margin-top:10px; color:#3c8e6c">
            Autor: Estudio para la Defensa de los Derechos de la Mujer (Demus)
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            André Mere Rivera
        <a href="https://www.instagram.com/andre.mere.rivera/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@andre.mere.rivera)
        </a>
        <div style="margin-top:10px;">
            Crissthian Manuel Olivera Fuentes
        </div>
        <div style="margin-top:10px;">
            Modera: Enrique León
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="
        background-color: #775aa4;
        color: #fae9e2;
        padding: 1rem 1.25rem;
        border-radius: 0.5rem;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 2px 6px;
        font-size: 25px;
        font-weight: bold;
    ">
        <strong>04:30 PM - 05:45 PM</strong><br> 
        <div style="margin-top:10px;">
        RECITAL DE POESÍA Y NARRATIVA QUEER
        </div>
        <div style="margin-top:10px; text-align:justify; font-weight: normal;">
            Espacio de lectura y encuentro dedicado a poetxs y escritorxs disidentes, orientado a la
            difusión de sus obras y al acercamiento del público a las diversas expresiones de la
            literatura queer contemporánea.
        </div>
        <div style="margin-top:10px;">
            Participan:
        </div>
        <div style="margin-top:10px;">
            Melissa Ghezzi
        <a href="https://www.instagram.com/amanda_meza1/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@amanda_meza1)
        </a>
        </div>
        <div style="margin-top:10px;">
            Gabs Valdivia
        <a href="https://www.instagram.com/veroferrarig/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@veroferrarig)
        </a>
        </div>
        <div style="margin-top:10px;">
            Lakita
        <a href="https://www.instagram.com/lakitatheartist/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@lakitatheartist)
        </a>
        </div>
        <div style="margin-top:10px;">
            Daniboi
        <a href="https://www.instagram.com/amanda_meza1/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@amanda_meza1)
        </a>
        </div>
        <div style="margin-top:10px;">
            María Paz
        <a href="https://www.instagram.com/veroferrarig/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@veroferrarig)
        </a>
        </div>
        <div style="margin-top:10px;">
            Lakita
        <a href="https://www.instagram.com/lakitatheartist/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@lakitatheartist)
        </a>
        </div>
        <div style="margin-top:10px;">
            Amanda Meza
        <a href="https://www.instagram.com/amanda_meza1/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@amanda_meza1)
        </a>
        </div>
        <div style="margin-top:10px;">
            Vero Ferrari
        <a href="https://www.instagram.com/veroferrarig/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@veroferrarig)
        </a>
        </div>
        <div style="margin-top:10px;">
            Lakita
        <a href="https://www.instagram.com/lakitatheartist/" target="_blank"
              style="text-decoration:none; color:#fae9e2; font-weight:600;"> (@lakitatheartist)
        </a>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    st.image("fotos/flyer_coloquio.png", width=1800)
       
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
