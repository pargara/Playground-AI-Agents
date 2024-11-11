from typing import Dict, Any
from langchain.chat_models import ChatOpenAI
import json
import os
from dotenv import load_dotenv

class BaseAgent:
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa el agente base.
        
        Args:
            config: Diccionario con la configuración del agente
        """
        load_dotenv()
        
        self.config = config
        self.llm = ChatOpenAI(
            model=config['model']['name'],
            temperature=config['temperature'],
            max_tokens=config['max_tokens'],
            api_key=os.getenv('OPENAI_API_KEY')
        )
        self.prompt_template = config['prompt']

    async def process(self, **kwargs) -> Dict[str, Any]:
        """
        Procesa la entrada usando el modelo LLM.
        
        Args:
            kwargs: Variables para el template del prompt
            
        Returns:
            Dict: Respuesta procesada en formato diccionario
        """
        try:
            # Formatea el prompt con los argumentos proporcionados
            formatted_prompt = self.prompt_template.format(**kwargs)
            
            # Obtiene la respuesta del modelo
            response = await self.llm.apredict(formatted_prompt)
            
            # Parsea la respuesta JSON
            return json.loads(response)
            
        except Exception as e:
            raise Exception(f"Error procesando la solicitud: {str(e)}") 