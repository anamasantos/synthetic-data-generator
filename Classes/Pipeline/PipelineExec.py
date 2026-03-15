import random
import time
import os
from dotenv import load_dotenv
from Classes.ConsumerAPI.AgentApi import GenerationStrategy
from Classes.DataPocessor.datasetProcessor import DatasetProcessor

class GenVisionEngine:
    def __init__(self, config_path, strategy: GenerationStrategy):
        self.processor = DatasetProcessor(config_path)
        self.strategy = strategy

def run_pipeline(self):
    sources = self.processor.get_sources()
    destination = self.processor.get_destination_folder()
    project_name = self.processor.get_project_name()

    for source in sources:
        folder = source['folder_name']
        path = source['images_source']
        prompts = source['prompts']
        
        print(f"Processando pasta {folder} em {path} com {len(prompts)} variações.")
        
        # Aqui você faria o loop nas imagens desta pasta específica
        for image_name in os.listdir(path):
            image_path = os.path.join(path, image_name)
            selected_prompt = random.choice(prompts)
            result = self.strategy.generate(image_path, selected_prompt)

