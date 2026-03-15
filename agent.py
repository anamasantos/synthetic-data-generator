
import os
from dotenv import load_dotenv

from Classes.ConsumerAPI.AgentApi import GenerateRequestAgent
from Classes.Pipeline.PipelineExec import GenVisionEngine


def main():
    load_dotenv()
    
    # Escolhemos a estratégia (Poderia ser trocada facilmente)
    strategy = GenerateRequestAgent(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Instanciamos a Fachada
    engine = GenVisionEngine("configs/settings.yaml", strategy)
    
    # Executamos o projeto
    engine.run_pipeline()

if __name__ == "__main__":
    main()
