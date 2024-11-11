from typing import Dict, Any
from .base_agent import BaseAgent

class StructureAgent(BaseAgent):
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa el agente de estructuración.
        
        Args:
            config: Diccionario con la configuración del agente
        """
        super().__init__(config)

    async def generate_structure(self, topic: str) -> Dict[str, Any]:
        """
        Genera la estructura del blog basada en el tema proporcionado.
        
        Args:
            topic: Tema del blog
            
        Returns:
            Dict con la estructura del blog (título, subtítulos, palabras clave)
        """
        return await self.process(topic=topic) 