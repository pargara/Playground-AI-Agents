import streamlit as st
import yaml
import asyncio
from agents.orchestrator import BlogOrchestrator

def load_config():
    """Carga la configuración desde el archivo YAML"""
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

def initialize_app():
    """Inicializa la aplicación y el orquestador"""
    if 'orchestrator' not in st.session_state:
        config = load_config()
        st.session_state.orchestrator = BlogOrchestrator(config)

def display_blog_content(blog_data):
    """Muestra el contenido del blog generado"""
    st.title(blog_data['title'])
    
    # Mostrar palabras clave
    st.subheader("Palabras Clave SEO")
    st.write(", ".join(blog_data['keywords']))
    
    # Mostrar contenido
    st.subheader("Contenido del Blog")
    for section in blog_data['content']:
        st.markdown(f"### {section['subtitle']}")
        st.write(section['content'])

async def generate_blog_content(topic):
    """Genera el contenido del blog usando el orquestador"""
    return await st.session_state.orchestrator.generate_blog(topic)

def main():
    st.set_page_config(
        page_title="Generador de Blogs SEO",
        page_icon="📝",
        layout="wide"
    )
    
    initialize_app()
    
    st.title("Generador de Blogs Optimizados para SEO")
    st.write("Ingresa un tema y generaré un blog completo optimizado para SEO")
    
    # Input del usuario
    topic = st.text_input("Tema del Blog", placeholder="Ej: Los beneficios de la inteligencia artificial en los negocios")
    
    if st.button("Generar Blog"):
        if topic:
            with st.spinner("Generando contenido..."):
                # Ejecutar generación de manera asíncrona
                blog_data = asyncio.run(generate_blog_content(topic))
                display_blog_content(blog_data)
        else:
            st.warning("Por favor, ingresa un tema para el blog")

if __name__ == "__main__":
    main()