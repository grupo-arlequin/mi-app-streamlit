# Crear el archivo app.py
with open('app.py', 'w') as f:
    f.write("""
import streamlit as st

st.title("Convertidor a Mayúsculas")

# Caja de texto para la entrada del usuario
texto_usuario = st.text_input("Escribe tu texto aquí:", "")

# Procesar el texto si hay contenido
texto_procesado = texto_usuario.upper()

# Caja de texto para mostrar el resultado (deshabilitada para que sea solo de lectura)
st.text_input("Texto en mayúsculas:", value=texto_procesado, disabled=True)
""")
