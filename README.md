# Student Exam Performance Predictor

An end-to-end Machine Learning web application that predicts a student's math score based on demographic and academic background features — built with a modular ML pipeline and deployed via Flask with CI/CD.

---

## Problem Statement

Educational institutions often struggle to identify students at risk of underperforming before results are declared. This project builds a regression model that predicts a student's math score using features like gender, parental education level, lunch type, test preparation course, and scores in reading and writing.

The goal is to surface predicted performance so that timely support can be provided.

---

## Project Structure

```
student_analysis_mlproject/
├── artifacts/                  # Auto-generated: stores train/test splits, model & preprocessor
│   ├── data.csv
│   ├── train.csv
│   ├── test.csv
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── notebook/
│   ├── data/
│   │   └── stud.csv            # Raw dataset
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       # Reads data, creates train/test split
│   │   ├── data_transformation.py  # Feature engineering & preprocessing pipeline
│   │   └── model_trainer.py        # Trains & evaluates multiple ML models
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py     # Handles inference for new inputs
│   │
│   ├── exception.py            # Custom exception handler with file/line tracing
│   ├── logger.py               # Timestamped logging across all modules
│   └── utils.py                # Shared utilities: model evaluation, pickle I/O
│
├── templates/
│   ├── index.html              # Landing page
│   └── home.html               # Prediction form UI
│
├── app.py                      # Flask application entry point
├── requirements.txt
├── setup.py
└── .github/workflows/          # CI/CD pipeline via GitHub Actions
```

---

## ML Pipeline

### 1. Data Ingestion
- Reads raw `stud.csv` from the `notebook/data/` directory
- Performs an 80/20 train-test split using `sklearn.model_selection.train_test_split`
- Saves all splits to the `artifacts/` folder for reproducibility

### 2. Data Transformation
- Numerical features: `SimpleImputer(median)` + `StandardScaler`
- Categorical features: `SimpleImputer(most_frequent)` + `OneHotEncoder` + `StandardScaler`
- Built using `sklearn.Pipeline` and `ColumnTransformer`
- Preprocessor serialized as `preprocessor.pkl` via `dill`

### 3. Model Training
- Trains and evaluates 10 regression models in a single run:

| Model | Type |
|---|---|
| Linear Regression | Baseline |
| Lasso / Ridge | Regularized Linear |
| K-Neighbors Regressor | Instance-based |
| Decision Tree | Tree-based |
| Random Forest | Ensemble (Bagging) |
| Gradient Boosting | Ensemble (Boosting) |
| XGBoost | Optimized Boosting |
| CatBoost | Gradient Boosting |
| AdaBoost | Adaptive Boosting |

- Best model selected automatically based on R2 score
- Final model serialized as `model.pkl`

---

## Dataset

Source: [Students Performance in Exams — Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

| Feature | Type | Description |
|---|---|---|
| gender | Categorical | Male / Female |
| race/ethnicity | Categorical | Group A-E |
| parental level of education | Categorical | Highest education level of parent |
| lunch | Categorical | Standard / Free-reduced |
| test preparation course | Categorical | Completed / None |
| reading score | Numerical | Score out of 100 |
| writing score | Numerical | Score out of 100 |
| math score | Target | Score out of 100 |

Total records: 1,000 students

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.8+ |
| ML Libraries | Scikit-learn, XGBoost, CatBoost |
| Web Framework | Flask |
| Data Processing | Pandas, NumPy |
| Serialization | Dill |
| Visualization | Matplotlib, Seaborn |
| Logging | Python logging module |
| CI/CD | GitHub Actions |
| Version Control | Git / GitHub |

---

## How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/student_analysis_mlproject.git
cd student_analysis_mlproject
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python src/components/data_ingestion.py
```
This will automatically trigger data transformation and model training. All outputs are saved to `artifacts/`.

### 5. Run the Flask app
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

---

## Web Application

The Flask app exposes the following routes:

- `GET /` — Renders the home page
- `POST /predict` — Accepts form input and returns the predicted math score

---

## Deployment

The application is deployed via a GitHub Actions CI/CD pipeline defined in `.github/workflows/`.

On every push to `main`:
1. GitHub Actions triggers the workflow
2. Dependencies are installed and the app is built
3. App is deployed to the cloud automatically

---

## Key Design Decisions

- Modular architecture — Each ML step (ingestion, transformation, training) is an independent, reusable class
- Custom exception handling — All errors surface with exact file name and line number for fast debugging
- Centralized logging — Timestamped logs generated per run for full traceability
- Config-driven paths — All artifact paths defined via `@dataclass` configs, making the pipeline portable

---

## Author

Atharva
B.Tech Student | RAIT, DY Patil University
GATE DA AIR 7007
[GitHub](https://github.com/<your-username>) | [LinkedIn](https://linkedin.com/in/<your-profile>)
