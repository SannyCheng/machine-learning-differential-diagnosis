# predict.py
import pandas as pd
import joblib
import pickle
import os

# Set project path （This is the absolute path of our group 18, you need to modify the path according to your computer settings, just modify this one place）
PROJECT_PATH = r"D:\Users\group18 coding"

# 1. Load the model
model_path = os.path.join(PROJECT_PATH, "random_forest_final.pkl")
model = joblib.load(model_path)

# 2. Load encoder
encoder_path = os.path.join(PROJECT_PATH, "label_encoders.pkl")
with open(encoder_path, "rb") as f:
    label_encoders = pickle.load(f)

# 3. Create prediction samples
example_input = pd.DataFrame([{
    "age": 45,
    "gender": "Female",
    "sleep_quality_index": 3.0,
    "brain_fog_level": 6.0,
    "physical_pain_score": 4.0,
    "stress_level": 5.0,
    "depression_phq9_score": 12.0,
    "fatigue_severity_scale_score": 7.0,
    "pem_duration_hours": 24.0,
    "hours_of_sleep_per_night": 6.0,
    "pem_present": 1.0,
    "work_status": "Not working",
    "social_activity_level": "Very low",
    "exercise_frequency": "Sometimes",
    "meditation_or_mindfulness": "no"
}])

# 4. data pre-processing
for col in example_input.columns:
    if col in label_encoders:
        example_input[col] = example_input[col].astype(str)
        for val in example_input[col].unique():
            if val not in label_encoders[col].classes_:
                example_input[col] = example_input[col].replace(val, label_encoders[col].classes_[0])
        example_input[col] = label_encoders[col].transform(example_input[col])
    else:
        example_input[col] = pd.to_numeric(example_input[col], errors='coerce')

example_input = example_input.fillna(0)

# 5. Prediction
prediction = model.predict(example_input)
prediction_code = prediction[0]

# 6. Output result
prediction_map = {0: "Depression", 1: "ME/CFS", 2: "Both"}
prediction_label = prediction_map[prediction_code]

print(f"Prediction category code: {prediction_code}")
print(f"Prediction category: {prediction_label}")