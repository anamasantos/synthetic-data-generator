
import os
from dotenv import load_dotenv

from Classes.ConsumerAPI.AgenApi import GeminiRequestAgent

if __name__ == "__main__":

    load_dotenv()
    api_key_gen = os.getenv("GOOGLE_API_KEY")
    print(api_key_gen)
    # Verifica se o arquivo .env existe
    if not os.path.exists(".env"):
        print("❌ Erro: Arquivo .env não encontrado no caminho ../../.env")
    else:
        print("✅ Arquivo .env encontrado com sucesso!")
    gmniAgent = GeminiRequestAgent(api_key=api_key_gen)
