import yaml
import os

class DatasetProcessor:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)


    def get_sources(self):
        return self.config.get('sources_folder', [])
    
    def get_project_name(self):
        return self.config.get('project_name', 'epi_project')

    def get_destination_folder(self):
        return self.config.get('destination_folder', 'destination_folder')
    