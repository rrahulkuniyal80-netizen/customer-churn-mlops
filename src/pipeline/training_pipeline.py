from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager

class TrainingPipeline:
    
    def run_pipeline(self):
        config_manager = ConfigurationManager()

        #Data_Ingestion
        data_ingestion_config = config_manager.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
        