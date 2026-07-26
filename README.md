# Customer Churn Prediction MLOps Pipeline

An end-to-end MLOps project for predicting customer churn using Scikit-Learn. This project demonstrates a complete machine learning workflow, including data ingestion, validation, transformation, model training, experiment tracking with MLflow, data versioning with DVC, and remote storage using AWS S3.

---

## Project Overview

Customer churn prediction helps businesses identify customers who are likely to leave their services. This project builds a Logistic Regression model and packages the entire workflow into a reproducible MLOps pipeline.

The project focuses on:

- Modular pipeline architecture
- Configuration-driven development
- Experiment tracking using MLflow
- Data and artifact versioning using DVC
- Remote storage with AWS S3
- Reproducible machine learning workflows

---

## Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python |
| ML Library | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Remote Storage | AWS S3 |
| Configuration | YAML |
| Version Control | Git & GitHub |

---

## Project Structure

```text
customer-churn-mlops/
│
├── config/
│   ├── config.yaml
│   └── schema.yaml
│
├── params/
│   └── params.yaml
│
├── data/
│
├── artifacts/
│
├── notebook/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── config/
│   │   └── configuration.py
│   │
│   ├── entity/
│   │   └── config_entity.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── utils/
│   │   └── common.py
│   │
│   └── logger.py
│
├── main.py
├── dvc.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Pipeline Workflow

```
Raw Dataset
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
MLflow Tracking
      │
      ▼
Artifacts & Model Saving
```

---

## Features

- Modular MLOps architecture
- Configuration-driven pipeline
- Data preprocessing using Scikit-Learn Pipelines
- Logistic Regression model training
- MLflow experiment tracking
- Automatic metric logging
- Confusion Matrix generation
- Classification Report generation
- Model serialization
- DVC pipeline for reproducibility
- AWS S3 remote storage for DVC

---

## MLflow Tracking

The project tracks:

### Parameters

- C
- max_iter
- random_state

### Metrics

- Accuracy
- Precision
- Recall
- F1 Score

### Artifacts

- Confusion Matrix
- Classification Report
- Trained Model

---

## DVC Pipeline

Run the complete pipeline:

```bash
dvc repro
```

Push tracked artifacts to AWS S3:

```bash
dvc push
```

Pull artifacts:

```bash
dvc pull
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/customer-churn-mlops.git
```

Move into the project

```bash
cd customer-churn-mlops
```

Create a virtual environment

```bash
conda create -n mlops python=3.13
```

Activate the environment

```bash
conda activate mlops
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the training pipeline

```bash
python main.py
```

or using DVC

```bash
dvc repro
```

---

## Dataset

**Dataset:** Telco Customer Churn Dataset

Target Variable:

```
Churn
```

---

## Results

Current model:

- Logistic Regression

Tracked using MLflow:

- Accuracy
- Precision
- Recall
- F1 Score

Generated artifacts:

- Confusion Matrix
- Classification Report
- Trained Model

---

## Future Improvements

- Docker
- FastAPI Deployment
- GitHub Actions CI/CD
- Kubernetes
- Model Monitoring
- Automated Retraining Pipeline

---

## Screenshots

### MLflow Dashboard

_Add screenshot here_

### DVC Pipeline

_Add screenshot here_

### AWS S3 Remote Storage

_Add screenshot here_

---

## Author

**Nand Kishor**

GitHub:https://github.com/rrahulkuniyal80-netizen/customer-churn-mlops/new/main?filename=README.md

LinkedIn:https://www.linkedin.com/in/nand-kishor-11077924b/

---
