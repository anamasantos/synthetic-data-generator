import os
from PIL import Image
from google import genai  # Novo pacote
# Carrega as variáveis de ambiente


class GeminiRequestAgent:
    """
    Classe responsável pela comunicação com a API do Google Gemini.
    Gerencia o envio de imagens e prompts para geração de dados sintéticos.
    """
    
    def __init__(self, model_name: str = "gemini-1.5-flash",api_key: str = None):
        self.api_key = api_key
        if not self.api_key:
            raise ValueError("❌ Chave não encontrada! Verifique se o arquivo .env está na raiz do projeto.")
        
        # No novo SDK, criamos um Client em vez de usar configure()
        self.client = genai.Client(api_key=self.api_key)
        self.model_id = model_name
        print(f"✅ Cliente Gemini ({self.model_id}) instanciado.")
    def process_image_variation(self, image_path: str, prompt: str):
        """
        Envia uma imagem e um prompt para o modelo e retorna a resposta.
        
        Args:
            image_path (str): Caminho para a imagem original.
            prompt (str): Instrução de alteração para a IA.
            
        Returns:
            str: Resposta textual ou confirmação do processamento da imagem.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")

        try:
            # Abre a imagem usando PIL
            img = Image.open(image_path)
            
            # Chamada multimodal (Texto + Imagem)
            # Nota: O retorno do Gemini 1.5 varia conforme o prompt (descrição ou geração)
            response = self.model.generate_content([prompt, img])
            
            return response.text
        
        except Exception as e:
            return f"⚠️ Erro ao processar imagem: {str(e)}"

# Bloco de teste
if __name__ == "__main__":
    agent = GeminiRequestAgent()