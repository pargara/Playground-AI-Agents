from typing import Dict, Any, List
from .base_agent import BaseAgent

class DevelopmentAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa el agente de desarrollo de contenido.
        
        Args:
            config: Diccionario con la configuración del agente
        """
        super().__init__(config)

    async def generate_content(
        self, 
        title: str, 
        subtitles: List[str], 
        keywords: List[str]
    ) -> Dict[str, Any]:
        """
        Genera el contenido detallado para cada sección del blog.
        
        Args:
            title: Título del blog
            subtitles: Lista de subtítulos
            keywords: Lista de palabras clave
            
        Returns:
            Dict con el contenido desarrollado para cada sección
        """
        return await self.process(
            title=title,
            subtitles=subtitles,
            keywords=keywords
        ) 