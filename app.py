import streamlit as st  # Importa la librería Streamlit con el alias st.
inicio = st.Page("inicio.py", title="Inicio", icon="🏠", default=True)  # Define la página principal.
datos = st.Page("datos.py", title="Datos", icon="📊")  # Define la página que demostrará el uso de caché.
pagina = st.navigation([inicio, datos])  # Registra las páginas de la aplicación multipágina.
pagina.run()  # Ejecuta la página seleccionada por el usuario.
