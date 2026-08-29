import streamlit as st  # Importa Streamlit para utilizar la interfaz y el sistema de caché.
import pandas as pd  # Importa Pandas para crear un pequeño conjunto de datos de ejemplo.
@st.cache_data  # Indica que Streamlit debe guardar y reutilizar el resultado de esta función.
def cargar_datos():  # Define una función que simula la carga o preparación de información.
    return pd.DataFrame({"SG": [0.80, 0.85, 0.90]})  # Devuelve un DataFrame que quedará almacenado en caché.
st.title("Datos con caché")  # Muestra el título de la página.
df = cargar_datos()  # Ejecuta la función o recupera directamente su resultado guardado en caché.
df["API"] = (141.5 / df["SG"]) - 131.5  # Calcula el grado API para cada gravedad específica.
st.dataframe(df, use_container_width=True)  # Presenta el DataFrame completo en la interfaz.
