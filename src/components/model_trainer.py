from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from pathlib import Path
from src.logger import logger
from src.utils.common import save_object
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os
from sklearn.metrics import classification_report
import mlflow 
import mlflow.sklearn
db_path = Path.cwd() / "mlflow.db"
mlflow.set_tracking_uri(f"sqlite:///{db_path.as_posix()}")

class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        logger.info("Model training started.")

        mlflow.set_experiment(self.config.experiment_name)
        with mlflow.start_run():

            model = LogisticRegression(C = self.config.C,
                                       max_iter=self.config.max_iter,
                                       random_state=self.config.random_state
                                       )
            mlflow.log_params({"model_name": "LogisticRegression",
                               "C": self.config.C,
                               "max_iter": self.config.max_iter,
                               "random_state": self.config.random_state
                               }
                               )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)

            disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
            plt.savefig("confusion_matrix.png")
            plt.close()
            with open("classification_report.txt", "w") as f:
                                     
                                     f.write(report)

            logger.info(f"Accuracy Score: {accuracy}")
            logger.info(f"Precision Score: {precision}")
            logger.info(f"Recall Score: {recall}")
            logger.info(f"F1 Score: {f1}")

            mlflow.log_metrics(
                {
                    "accuracy": accuracy,
                    "precision": precision,
                    "recall": recall,
                    "f1_score": f1,
                }
            )
            mlflow.log_artifact("classification_report.txt")
            os.remove("confusion_matrix.png")
            os.remove("classification_report.txt")

            mlflow.set_tags({
                "project": "Customer Churn Prediction",
                "developer": "Nand Kishor",
                "framework": "Scikit-Learn",
                "algorithm": "Logistic Regression"
            })
            
            save_object(
                file_path=self.config.model_path,
                obj=model
            )

            mlflow.sklearn.log_model(
                            sk_model= model, 
                            name="model"
                        )
            

            logger.info("Trained model saved successfully.")