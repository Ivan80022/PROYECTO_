import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter

# Función para contar aminoácidos en una secuencia de proteína
def calcular_aminacidos(proteina):
    return Counter(proteina)

st.markdown("<h3 style='color: red;'>Este sitio web es para saber como identificar aminoacidos de unas proteinas del ser humano ademas tenemos varias porteinas para que tu elijas.</h3>", unsafe_allow_html=True)
# Diccionario ampliado de proteínas con sus secuencias
proteinas = {
    "Hemoglobina": "VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHF",
    "Insulina": "FVNQHLCGSHLVEALYLVCGERGFFYTPKA",
    "Colágeno": "GPPGPPGPPGPPGPPGPPGPPGPPGPPGPP",
    "Mioglobina": "GLSDGEWQQVLNVWGKVEADIPGHGQEVLIRLFKSHPETLEKFDR",
    "Actina": "MDDDIAALVVDNGSGMCKAGFAGDDAPRAVFPSIVGRPRHQGVMVGMGQKDSYVGDEAQSKRGILTLKYPIEHGIVTNWDDMEKIWHHTFYNELRVAPEEHPVLLTEAPLNPKANREKMTQIMFETFNVPAMYVAIQAVLSLYASGRTTGIVMDSGDGVTHTVPIYEGYALPHAIMRLVDEFARKKF",
    "Queratina": "MDKVLKRLKKILRDFGLAKTGCCVPVSGLCYVKNMDVTQGLCKRLE",
    "Tripsina": "IVGGYTCGANTVPYQVSLNSGYHFCGGSLINSQWVVSAAHCYKSRI",
    "Lisozima": "KVFERCELARTLKRLGMDGYRGISLANWMCLAKWESGYNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPC",
    "Elastina": "VPGVGVPGLGVPGVGVPGLGVPGVGVPGLGVPGVGVPGLGVPGVGVPGLGVPGV",
    "Pepsina": "VLGIVLFLVVAAQGSKKDGDQVKIFQNRWTQYPIAGWGEEGVALPQEA",
}

# Diccionario con nombres completos de los aminoácidos
aminoacidos_info = {
    "A": "Alanina",
    "R": "Arginina",
    "N": "Asparagina",
    "D": "Aspartato",
    "C": "Cisteína",
    "E": "Glutamato",
    "Q": "Glutamina",
    "G": "Glicina",
    "H": "Histidina",
    "I": "Isoleucina",
    "L": "Leucina",
    "K": "Lisina",
    "M": "Metionina",
    "F": "Fenilalanina",
    "P": "Prolina",
    "S": "Serina",
    "T": "Treonina",
    "W": "Triptófano",
    "Y": "Tirosina",
    "V": "Valina"
}

# Configurar título con estilo
st.markdown("<h1 style='color: teal;'>Cálculo de Aminoácidos de una Proteína</h1>", unsafe_allow_html=True)

# Barra lateral para elegir la proteína
st.sidebar.header("Selecciona una proteína")
opcion = st.sidebar.selectbox("Proteínas disponibles:", list(proteinas.keys()))

# Mostrar nombre de la proteína seleccionada con estilo
st.markdown(f"<h2 style='color: darkblue;'>Proteína seleccionada: {opcion}</h2>", unsafe_allow_html=True)

# Obtener secuencia de la proteína
secuencia = proteinas[opcion]

# Calcular la cantidad de aminoácidos
conteo = calcular_aminacidos(secuencia)

# Crear DataFrame con los datos
df = pd.DataFrame(
    {
        "Aminoácido (1 letra)": list(conteo.keys()),
        "Nombre completo": [aminoacidos_info[aa] for aa in conteo.keys()],
        "Cantidad": list(conteo.values()),
    }
)

# Ordenar el DataFrame por cantidad de aminoácidos
df = df.sort_values(by="Cantidad", ascending=False)

# Mostrar la secuencia y tabla de aminoácidos
st.markdown("<h3 style='color: orange;'>Secuencia de la proteína:</h3>", unsafe_allow_html=True)
st.text(secuencia)

st.markdown("<h3 style='color: green;'>Conteo de aminoácidos:</h3>", unsafe_allow_html=True)
st.dataframe(df)

# Generar gráfica interactiva usando Plotly
st.markdown("<h3 style='color: purple;'>Gráfica de aminoácidos:</h3>", unsafe_allow_html=True)
fig = px.bar(
    df,
    x="Aminoácido (1 letra)",
    y="Cantidad",
    text="Cantidad",
    color="Cantidad",
    color_continuous_scale="viridis",
    title=f"Distribución de aminoácidos en {opcion}",
    labels={"Cantidad": "Frecuencia", "Aminoácido (1 letra)": "Aminoácido"},
)
fig.update_layout(title_x=0.5)
st.plotly_chart(fig)
st.markdown("<h3 style='color: yellow;'>Integrantes: Alcantara Leal Ariadne y Pedro Borbon Aguirre.</h3>", unsafe_allow_html=True)
