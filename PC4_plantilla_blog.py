# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.

# Primero, debes abrir el folder donde se encuentra tu archivo de Python en la terminal de tu computadora.
# Para hacerlo, debes escribir el siguiente comando en la terminal de tu computadora
# cd ruta_de_tu_carpeta
# o desde Visual Studio Code, seleccionas Open Folder y seleccionas la carpeta 
# donde se encuentra tu archivo de Python

# Segundo, debes instalar un entorno virtual en tu computadora.
# python -m venv .venv
# Este comando crea un entorno virtual en la carpeta actual con el nombre .venv.

# Para activar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# .venv\Scripts\activate
# Para desactivar el entorno virtual, debes escribir el siguiente comando en la terminal de tu computadora
# deactivate

# Tercero, debes instalar Streamlit en tu entorno virtual.
# pip install Streamlit 

# Cuarto, puedes abrir el tutorial de Streamlit en tu navegador.
# streamlit hello o python -m streamlit hello

# Quinto, debes abrir el archivo de Python en la terminal de tu computadora.
# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py o python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Programando mi historia</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("foto.jpg", caption='Foto feliz en un día feliz.', width=300)

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

texto = """
¡Hola! Mi nombre es Abi Camavilca y soy estudiante de quinto ciclo de la carrera de Publicidad en la PUCP, y estoy profundamente apasionada por el mundo de la creatividad y la comunicación. Una de las cosas que más me entusiasma de mi carrera es la capacidad de utilizar ideas innovadoras para entender y conectar de manera auténtica con el público objetivo, generando mensajes que resuenan y dejan huella. Me gusta explorar cómo la publicidad puede ir más allá de la venta, ayudando a construir relaciones de valor entre marcas y personas, y promoviendo experiencias que se sienten genuinas y memorables. Mirando hacia el futuro, mi sueño profesional es desarrollarme en una agencia de publicidad donde pueda experimentar la intensidad creativa y estratégica del trabajo en equipo. Más adelante, me gustaría dar el siguiente paso y unirme al área de marketing de una empresa, donde pueda aplicar mi experiencia para generar impacto directo en el posicionamiento y crecimiento de una marca en específico. En mi tiempo libre, me gusta hacer un poco de todo. Dependeiendo del mood disfruto leer, bordar, pintar, hacer bisutería, y hacer scrapbook, ya que cada uno de estos pasatiempos me permite expresar mi creatividad y relajarme. También me encanta andar en bicicleta, escuchar música y hornear, actividades que me ayudan a encontrar un balance y a recargar energías. Además, algo muy importante para mí es mi fe cristiana. Dedico una parte de mi tiempo a mi comunión con Dios, a apoyar en actividades de la iglesia y servir, lo cual me permite dar lo mejor de mí a los demás. Dios siempre me acompaña por lo que siempre está dentro de mis planes presentes y futuros, lo que me permite descansar en su voluntad.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 11px;'>{texto}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.

# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.

# Agregar un  texto para la respuesta
texto_2 = """
Al comenzar este curso y a aprender programación, sentí mucha emoción y una gran satisfacción porque estaba entendiendo todo lo que nos enseñaban. Me sentía confiada y muy motivada por la claridad con la que las ideas se iban conectando. Sin embargo, cuando llegó la primera PC, las cosas se complicaron. La falta de tiempo para terminar esta pc me costó procesar bastante que incluso, por un momento, llegué a pensar que quizá el curso era demasiado fuerte para mí. A pesar de los desafíos, la programación me ha enseñado mucho. He aprendido que, en la mayoría de los casos, hay formas más fáciles de resolver situaciones si se tiene la paciencia y creatividad para encontrarlas. También descubrí que es importante enfocarse primero en que el código funcione y luego buscar formas más eficientes de lograrlo, esto también puede ser aplicable en otros contextos. :) Una de las cosas que más me gusta de programar es ver los códigos de colores, me encantan los colores y verlos en ese entorno es satisfactorio. También, como mencionaba antes, me agradan las distintas maneras en que una situación puede resolverse, me gusta el reto de pensar y encontrar soluciones para que algo funcione. Sin embargo, lo que no disfruto tanto son los momentos en que aparecen errores complejos y requieren de ayuda para solucionarlos, o cuando, a pesar de mis intentos, no consigo resolverlos tan fácilmente. Con la programación, me gustaría en el futuro poder crear páginas web que puedan ayudar a personas en áreas relacionadas con mi ámbito laboral. Además, me motiva pensar en desarrollar algo que genere un impacto positivo y beneficie realmente a quienes lo necesitan, pero desde el rubro en el que me estoy formando.
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Explicación de un tema de las clases 📚") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
#st.video("Ejercicio _2.mp4")
#st.video("Ejercicio_5.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.


# Agregamos un enlace a la página web donde está el video.
 enlace = f'<a href="https://drive.google.com/file/d/1pD2CCRNvarmJx04TaEXsya6_AmO80QuE/view?usp=sharing" target="_blank"><button>sI TE GUSTA EL CHISME HAZ CLICK AQUÍ :V</button></a>'
# st.markdown(enlace, unsafe_allow_html=True)
# f'<a href="URL" target="_blank"><button>Nombre</button></a>':
# La etiqueta <a> se utiliza para crear un enlace en HTML.
# El atributo href se utiliza para especificar la URL de destino del enlace.
# El atributo target="_blank" se utiliza para abrir el enlace en una nueva pestaña del navegador.
# La etiqueta <button> se utiliza para crear un botón en HTML.
# El texto dentro de las etiquetas <button> ("Nombre creativo para el botón") es el contenido del botón.
# La variable enlace contiene la cadena de código HTML para el enlace y el botón.


# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Datos y colores</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Los análisis de Ellie</h1>: Esta es una cadena de código HTML.
# La etiqueta <h1> se utiliza para el encabezado principal de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h1> ("Los análisis de Ellie") es el contenido del encabezado.

# Creamos una lista de gráficos
graficos = ['"A donde va el viento"-Julieta Venegas', 'Tarjetas rojas en la liga italiana', 'Juventus: goles anotados']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)
# El cuadro de selección se crea con la función selectbox.
# El primer argumento es el texto que se muestra en el cuadro de selección.
# El segundo argumento es una lista de opciones que se pueden seleccionar.
# En este caso, las opciones son los elementos de la lista graficos.
# La opción seleccionada se asigna a la variable grafico_seleccionado.
# La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
# La función selectbox se utiliza para crear un cuadro de selección en la barra lateral.

# Mostramos el gráfico seleccionado
if grafico_seleccionado == '"A donde va el viento"-Julieta Venegas':
    sidebar.markdown("<div style='text-align: justify; font-size: 20px;'>Este gráfico fue hecho con la librería WordCloud y muestra las palabras de un texto en diversos tamaños, el tamaño de cada una depende de la cantidad de veces que se repitió en el texto. Es decir, mientras más grande sea la palabra, más veces se repitió en el texto.</div>", unsafe_allow_html=True)
    sidebar.image("nube_palabras_Julieta_Venegas.png", caption='"A donde va el viento"', width=500)
    pass
elif grafico_seleccionado == 'Tarjetas rojas en la liga italiana':
    sidebar.markdown("<div style='text-align: justify'>Este gráfico de pastel también fue hecho con la librería Matlotlib y la misma base de datos de la liga italiana (serie A). El gráfico representa los promedios de tarjetas rojas recibidas como visitante para todos los equipos de esta liga.</div>", unsafe_allow_html=True)
    sidebar.image("Promedio_tarjetas_rojas.png", caption='Promedio de tarjetas rojas', width=500)
    pass
elif grafico_seleccionado == 'Juventus: goles anotados':
    sidebar.markdown("<div style='text-align: justify'>Estos gráficos de barras fueron hechos con la librería Matlotlib. La base de datos con la que se trabajó es la primera división de la liga italiana (serie A). Se escogió un equipo, en este caso la Juventus, y se calculó la frecuencia de los goles anotados como equipo local y como visitante.</div>", unsafe_allow_html=True)
    sidebar.image("goles_juve.png", caption='', width=500)
    pass

# if grafico_seleccionado == 'Gráfico de Macroareas': Esta línea verifica si la opción seleccionada es 'Gráfico de Macroareas'.
# Si es así, se ejecuta el código dentro del bloque if.
# En este caso, se muestra un texto y una imagen correspondientes al gráfico de Macroareas.
# El texto y la imagen se muestran en la barra lateral.
# La función markdown se utiliza para mostrar el texto en la barra lateral.
# La función image se utiliza para mostrar la imagen en la barra lateral.
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen.
# El argumento width se utiliza para especificar el ancho de la imagen.
# La palabra clave pass se utiliza para indicar que no se debe hacer nada en caso de que la opción seleccionada no sea 'Gráfico de Macroareas'.
