import streamlit as st
from transformers import pipeline

# Configuración de la página
st.set_page_config(page_title="IA Summarizer Pro", page_icon="🤖")

st.title("🤖 Resumidor de Textos con IA")
st.markdown("Este proyecto utiliza el modelo **DistilBART** para crear resúmenes inteligentes.")

# Cargar el modelo (se guarda en caché para que sea rápido)
@st.cache_resource
def cargar_modelo():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = cargar_modelo()

# Interfaz de usuario
texto_entrada = st.text_area("Pega aquí el texto que quieras resumir:", height=200)

if st.button("Generar Resumen"):
    if texto_entrada:
        with st.spinner('La IA está pensando...'):
            resumen = summarizer(texto_entrada, max_length=130, min_length=30, do_sample=False)
            st.success("¡Resumen completado!")
            st.subheader("Resultado:")
            st.write(resumen[0]['summary_text'])
    else:
        st.warning("Por favor, introduce algún texto.")