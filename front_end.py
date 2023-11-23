import streamlit as st
from app import *
import os

st.markdown('**Bienvenid@**')
url = st.text_input('Link Zona Prop')
file_name = st.text_input('Nombre para la ficha')

if st.button('Generar ficha'):
    with st.status('Creando ficha...'):
        information = None
        create_real_estate_pdf(file_name,information)

    with open(f"{file_name}.pdf", "rb") as file:
        btn = st.download_button(
                label="Descargar ficha",
                data=file,
                file_name=f"{file_name}.pdf",
                mime="application/pdf"
            )
        os.system(f"rm {file_name}.pdf")  
