from src.utils.common import read_yaml
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig


class ConfigurationManager:

    def __init__(self):
        self.config = read_yaml(Path("config/config.yaml"))
        self.params = read_yaml(Path("params/params.yaml"))

    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]
        params = self.params["data_ingestion"]
        return DataIngestionConfig(
            root_dir = Path(config["root_dir"]),
            source_path=Path(config["source_path"]),
            train_data_path= Path(config["train_data_path"]),
            test_data_path=Path(config["test_data_path"]),
            test_size = params["test_size"],
            random_state = params["random_state"]
        )
    
    def get_data_validation_config(self):
        config = self.config["data_validation"]

        return DataValidationConfig(
            root_dir= Path(config["root_dir"]),
            train_data_path = Path(self.config["data_ingestion"]["train_data_path"]),
            test_data_path = Path(self.config["data_ingestion"]["test_data_path"]),
            schema_path= Path(config["schema_path"]),
            status_file= Path(config["status_file"])
            

        )
    
    def get_data_transformation_config(self):
        config = self.config["data_transformation"]

        return DataTransformationConfig(
            root_dir= Path(config["root_dir"]),
            train_data_path= Path(self.config["data_ingestion"]["train_data_path"]),
            test_data_path= Path(self.config["data_ingestion"]["test_data_path"]),
            preprocessor_obj_file_path= Path(config["preprocessor_obj_file_path"])
        )