from typing import Dict, Any
from .structure_agent import StructureAgent
from .development_agent import DevelopmentAgent

class BlogOrchestrator:
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa el orquestador con los agentes necesarios.
        
        Args:
            config: Diccionario con la configuración de los agentes
        """
        self.structure_agent = StructureAgent(config['agents']['structure'])
        self.development_agent = DevelopmentAgent(config['agents']['content'])

    async def generate_blog(self, topic: str) -> Dict[str, Any]:
        """
        Genera un borrador completo del blog.
        
        Args:
            topic: Tema del blog
            
        Returns:
            Dict con el blog completo estructurado
        """
        try:
            # Paso 1: Generar estructura
            structure = await self.structure_agent.generate_structure(topic)
            
            # Paso 2: Desarrollar contenido
            content = await self.development_agent.generate_content(
                title=structure['title'],
                subtitles=structure['subtitles'],
                keywords=structure['keywords']
            )
            
            # Paso 3: Ensamblar resultado final
            return {
                'title': structure['title'],
                'keywords': structure['keywords'],
                'content': content['sections']
            }
            
        except Exception as e:
            import traceback
            raise Exception(f"Error generando el blog: {str(e)}\n\nTraceback completo:\n{traceback.format_exc()}") 