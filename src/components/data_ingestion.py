import pandas as pd
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataIngestionConfig
from src.logger import logger

class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        self.config.root_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Reading The Dataset")
        df = pd.read_csv(self.config.source_path)
       
        logger.info("Splitting The Dataset")
        train_df, test_df = train_test_split(df, test_size= self.config.test_size, random_state=self.config.random_state )
       
        logger.info("Saving train and test datasets")
        train_df.to_csv(self.config.train_data_path, index = False)
        test_df.to_csv(self.config.test_data_path, index = False)
       
        logger.info("Data Ingestion Completed")
