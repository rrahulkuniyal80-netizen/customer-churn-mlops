from src.config.configuration import ConfigurationManager
from src.entity.config_entity import DataValidationConfig
from src.utils.common import read_yaml
import pandas as pd
from src.logger import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config 

    def initiate_data_validation(self):
        logger.info("Data_validation_started")
        self.config.root_dir.mkdir(parents=True, exist_ok=True)
        
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)
        schema = read_yaml(self.config.schema_path)
        expected_columns = list(schema["columns"].keys())
        train_status = all(col in train_df.columns for col in expected_columns)
        test_status = all(col in test_df.columns for col in expected_columns)

        logger.info("Checking Validation")
        validation_status = train_status and test_status
        

        with open(self.config.status_file, "w") as f:
            f.write(f"Validation status: {validation_status}")
        logger.info(f"Validation status: {validation_status}")

        logger.info("Validation_completed")


