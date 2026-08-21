# 🎓 Student Exam Performance Predictor

An end-to-end Machine Learning project that predicts a student's **math score** based on demographic and academic factors, deployed as a Flask web application. This project demonstrates a complete ML lifecycle — from data ingestion and preprocessing, through model training and evaluation, to deployment on the cloud.

## 📖 Overview

Given inputs such as gender, ethnicity, parental education level, lunch type, test preparation course status, and reading/writing scores, the model predicts a student's expected math score. The project is structured as a modular, production-style ML pipeline rather than a single notebook — making it easy to maintain, extend, and deploy.

## 🚀 Features

- **End-to-end ML pipeline**: data ingestion → data transformation → model training → prediction
- **Multiple models evaluated**: Linear Regression, Random Forest, Decision Tree, Gradient Boosting, XGBoost, CatBoost, AdaBoost — with the best-performing model selected automatically
- **Custom exception handling & logging** for easier debugging in production
- **Flask web app** with a simple HTML form for entering student details and viewing predictions
- **Modular, package-based codebase** (`src/`) installable via `setup.py`
- **Cloud deployment ready** via AWS Elastic Beanstalk (`.ebextensions`)

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| ML/Data | pandas, numpy, scikit-learn, XGBoost, CatBoost |
| Web Framework | Flask |
| Serialization | dill |
| Deployment | AWS Elastic Beanstalk |

## 📂 Project Structure

```
mlproject/
├── .ebextensions/            # AWS Elastic Beanstalk deployment configuration
├── artifacts/                # Saved model, preprocessor, and train/test data
├── catboost_info/            # Auto-generated CatBoost training logs
├── notebook/                 # EDA and model experimentation notebooks
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging configuration
│   └── utils.py                # Shared utility functions
├── templates/                 # HTML templates (index.html, home.html)
├── app.py                     # Flask application entry point
├── application.py             # AWS Elastic Beanstalk entry point
├── requirements.txt
├── setup.py
└── README.md
```

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/KshitijO-O/mlproject.git
   cd mlproject
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

### Train the model
```bash
python src/pipeline/train_pipeline.py
```
This runs the full pipeline — data ingestion, transformation, and model training — and saves the trained model and preprocessor to the `artifacts/` folder.

### Run the web app
```bash
python app.py
```
Then open your browser and go to:
```
http://127.0.0.1:5000
```
Fill in the student details on the form to get a predicted math score.

## ☁️ Deployment

This project is configured for deployment on **AWS Elastic Beanstalk** using the `.ebextensions` folder and `application.py` as the WSGI entry point.

## 📊 Model Performance

Multiple regression models were trained and evaluated using R² score, and the best-performing model was selected for the final prediction pipeline. Detailed experimentation and comparison can be found in the `notebook/` directory.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open a pull request or issue.

## 📄 License

This project is open-source and available for educational purposes.

## 👤 Author

**Kshitij Milind Padwal**
GitHub: [@KshitijO-O](https://github.com/KshitijO-O)
