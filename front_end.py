import streamlit as st
from app import *

st.markdown('**Bienvenid@**')
url = st.text_input('Link Zona Prop')
file_name = st.text_input('Nombre para la ficha')

if st.button('Generar ficha'):
    with st.status('Creando ficha...'):
        create_file(url,file_name)

    with open(f"{file_name}.pdf", "rb") as file:
        btn = st.download_button(
                label="Descargar ficha",
                data=file,
                file_name=f"{file_name}.pdf",
                mime="application/pdf"
            )