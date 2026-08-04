import pandas as pd
import joblib

class PredictionPipeline:

    def __init__(self):

        self.model = joblib.load(
            "artifacts/model_trainer/model.pkl"
        )

        self.preprocessor = joblib.load(
            "artifacts/data_transformation/preprocessor.pkl"
        )

    def predict(self, customer_data):
        df = pd.DataFrame([customer_data])

        transformed_data = self.preprocessor.transform(df)

        prediction = self.model.predict(transformed_data)

        return prediction[0]