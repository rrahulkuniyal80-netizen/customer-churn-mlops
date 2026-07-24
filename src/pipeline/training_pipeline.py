from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.config.configuration import ConfigurationManager
from src.logger import logger

class TrainingPipeline:
    
    def run_pipeline(self):
        config_manager = ConfigurationManager()

        #Data_Ingestion
        logger.info("data_ingestion_pipeline_started")

        data_ingestion_config = config_manager.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
        logger.info("data_ingestion_pipeline_completed")

        #Data Validation
        logger.info("data_validation_pipeline_started")
        data_validation_config = config_manager.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.initiate_data_validation()

        logger.info("data_validation_pipeline_completed")

        #Data Transformation

        
        logger.info("data_Transformation_pipeline_started")

        data_transformation_config = config_manager.get_data_transformation_config()

        data_transformation = DataTransformation(
            data_transformation_config
        )

        X_train, X_test, y_train, y_test = (
            data_transformation.initiate_data_transformation()
        )

        logger.info("data_transformation_pipeline_completed")


        #Model Trainer
        logger.info("Model_trainer_pipeline_started")
        model_trainer_config = config_manager.get_model_trainer_config()

        model_trainer = ModelTrainer(model_trainer_config)

        model_trainer.initiate_model_trainer(
            X_train,
            X_test,
            y_train,
            y_test
        )

        logger.info("Model_trainer_pipeline_completed")
        
        
    


        