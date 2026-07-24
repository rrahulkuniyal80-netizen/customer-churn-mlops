from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.logger import logger
from src.utils.common import save_object

class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        logger.info("Model training started.")

        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        logger.info(f"Accuracy Score: {accuracy}")
        logger.info(f"Precision Score: {precision}")
        logger.info(f"Recall Score: {recall}")
        logger.info(f"F1 Score: {f1}")

        save_object(
            file_path=self.config.model_path,
            obj=model
        )

        logger.info("Trained model saved successfully.")