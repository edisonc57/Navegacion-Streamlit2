import streamlit as st  # Importa Streamlit para crear la página inicial.
st.title("Uso de caché")  # Muestra el título principal de la página.
st.write("La siguiente página reutiliza datos calculados previamente.")  # Explica de forma simple el propósito de st.cache_data.
st.page_link("datos.py", label="Ver ejemplo de caché", icon="📊")  # Añade un acceso visible hacia la página del ejemplo.
