Here's the complete and improved README structure that you can use for your project:

---

# ME/CFS and Depression Diagnosis Prediction

This project involves the development of a machine learning model to predict the diagnosis of patients based on various features related to health, such as sleep quality, physical pain, stress level, depression score, and other relevant metrics. The model is trained to classify diagnoses into three categories: **ME/CFS**, **Depression**, and **Both**.

## Table of Contents

1. [Introduction](#introduction)
2. [Data Description](#data-description)
3. [Installation](#installation)
4. [Model Training](#model-training)
5. [Model Evaluation](#model-evaluation)
6. [Results](#results)
7. [Saved Models](#saved-models)
8. [License](#license)

## Introduction

The objective of this project is to classify individuals into three diagnosis categories:

* **ME/CFS** (Myalgic Encephalomyelitis/Chronic Fatigue Syndrome)
* **Depression**
* **Both**

The model uses various health-related features to predict the diagnosis, utilizing machine learning techniques such as Random Forest, Logistic Regression, Decision Trees, and K-Nearest Neighbors (KNN).

## Data Description

The dataset contains 1620 entries and 16 columns. The columns are as follows:

* **age**: Age of the individual
* **gender**: Gender of the individual
* **sleep_quality_index**: Sleep quality score
* **brain_fog_level**: Level of brain fog
* **physical_pain_score**: Score of physical pain
* **stress_level**: Stress level
* **depression_phq9_score**: Depression score
* **fatigue_severity_scale_score**: Fatigue severity score
* **pem_duration_hours**: Duration of PEM (Post-exertional malaise)
* **hours_of_sleep_per_night**: Number of hours of sleep per night
* **pem_present**: Whether PEM is present (binary)
* **work_status**: Work status (Not working, Working, Partially working)
* **social_activity_level**: Level of social activity
* **exercise_frequency**: Frequency of exercise
* **meditation_or_mindfulness**: Whether the individual practices meditation or mindfulness
* **diagnosis**: Diagnosis label (ME/CFS, Depression, Both)

### Missing Values

The dataset contains some missing values, which are handled during preprocessing using methods like imputation.

## Installation

To get started, clone this repository:

```bash
git clone https://github.com/yourusername/ME-CFS-Diagnosis-Prediction.git
cd ME-CFS-Diagnosis-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Model Training

The project trains several machine learning models to predict the diagnosis of patients:

1. **Logistic Regression** (multi-class classification)
2. **Decision Tree Classifier**
3. **Random Forest Classifier**
4. **K-Nearest Neighbors (KNN)**
5. **Support Vector Machine (SVM)**
6. **Baseline Model** (Majority Class)

### Preprocessing

Each model is trained using a pipeline that includes the following preprocessing steps:

* **Imputation** (for handling missing values)
* **Scaling** (using `StandardScaler`)
* **One-Hot Encoding** (for categorical features)

## Model Evaluation

The models were evaluated on a test set using **5-fold cross-validation**. The evaluation metrics include:

* **Accuracy**: Proportion of correctly predicted instances.
* **Precision**: Proportion of true positive predictions over all positive predictions.
* **Recall**: Proportion of true positive predictions over all actual positives.
* **F1-Score**: Harmonic mean of precision and recall.

### Performance Results on the Test Set

| Model                   | Accuracy | Macro F1 |
| ----------------------- | -------- | -------- |
| **Baseline**            | 0.401    | 0.191    |
| **Logistic Regression** | 0.768    | 0.762    |
| **Decision Tree**       | 0.701    | 0.691    |
| **Random Forest**       | 0.806    | 0.787    |
| **SVM**                 | 0.767    | 0.753    |
| **KNN**                 | 0.711    | 0.699    |

From the above results, **Random Forest** and **Logistic Regression** were found to be the top-performing models, with high **F1-scores** on both the training and test sets.

## Saved Models

The following models have been trained and saved for future use:

* **Random Forest Model**: saved as `random_forest_model.joblib`
* **Logistic Regression Model**: saved as `logistic_regression_model.joblib`
* **KNN Model**: saved as `knn_model.joblib`
* **SVM Model**: saved as `svm_model.joblib`

These models can be loaded using the following code:

```python
from joblib import load

rf_model = load('random_forest_model.joblib')
log_reg_model = load('logistic_regression_model.joblib')
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This updated structure is comprehensive, well-organized, and ready for use in your GitHub repository!
