from src.entity.config_entity import DataTransformationConfig
from src.utils.common import read_yaml
import pandas as pd
from src.logger import logger
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from src.utils.common import save_object
import pickle


class DataTransformation:
    def __init__ (self, config: DataTransformationConfig):
        self.config = config


    def clean_data(self,train_df, test_df):
        train_df["TotalCharges"] = pd.to_numeric(train_df["TotalCharges"], errors="coerce")
        test_df["TotalCharges"] = pd.to_numeric(test_df["TotalCharges"], errors="coerce")
        train_df = train_df.dropna()
        test_df = test_df.dropna()

        return train_df, test_df

    def get_preprocessor(self, X_train):

        num_columns = X_train.select_dtypes(include=['number'])
        cat_columns = X_train.select_dtypes(include=['object'])

        num_pipeline = Pipeline(
            steps= [
                ("scaler", StandardScaler())
            ]
        ).columns

        cat_pipeline = Pipeline(
            steps=[
                ("encoder", OneHotEncoder(handle_unknown="ignore"))
            ]
        ).columns

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", num_pipeline, num_columns),
                ("cat", cat_pipeline, cat_columns)
            ],
            remainder='passthrough'
        )

        return preprocessor


    def initiate_data_transformation(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        train_df, test_df = self.clean_data(
        train_df,test_df)

        X_train = train_df.drop(columns=["Churn"])
        y_train = train_df["Churn"]

        X_test = test_df.drop(columns=["Churn"])
        y_test = test_df["Churn"]

        label_encoder = LabelEncoder()
        y_train = label_encoder.fit_transform(y_train)
        y_test = label_encoder.transform(y_test)

        preprocessor = self.get_preprocessor(X_train)

        X_train = preprocessor.fit_transform(X_train)

        X_test = preprocessor.transform(X_test)

        save_object(file_path=self.config.preprocessor_obj_file_path, obj=preprocessor)

        return X_train, X_test, y_train, y_test

                 
