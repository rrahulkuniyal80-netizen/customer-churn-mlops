from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_path: Path
    train_data_path: Path
    test_data_path: Path
    test_size: float
    random_state: int
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    train_data_path: Path
    test_data_path: Path
    schema_path: Path
    status_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_path : Path
    test_data_path : Path
    preprocessor_obj_file_path: Path
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_path: Path
    C: float
    max_iter: int 
    random_state: int
    experiment_name: str
    
