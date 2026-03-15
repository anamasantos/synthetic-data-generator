import os
from PIL import Image
from google import genai
from google.genai import types
from abc import ABC, abstractmethod

class GenerationStrategy(ABC):
    @abstractmethod
    def generate(self, image_path, prompt):
        pass

class GenerateRequestAgent(GenerationStrategy):

    def __init__(self, model_name: str = "gemini-2.0-flash", api_key: str = None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("❌ API Key não fornecida.")
        
        self.client = genai.Client(api_key=self.api_key)
        self.model_id = model_name
        print(f"✅ Cliente Gemini ({self.model_id}) instanciado.")

    def generate(self, image_path, prompt):
        if not os.path.exists(image_path):
            return f"❌ Arquivo não encontrado: {image_path}"

        try:
            # 1. Abre a imagem original
            img = Image.open(image_path)
            
            # 2. Faz a chamada de geração (Usando o modelo para criar a imagem baseada na original)
            # Nota: Para o Gemini gerar uma NOVA imagem baseada em outra, 
            # usamos o recurso de Image-to-Image se disponível ou instruímos via prompt.
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=[prompt, img]
            )
            return response.generated_images[0].image
        except Exception as e:
            return f"⚠️ Erro ao gerar variação: {str(e)}"