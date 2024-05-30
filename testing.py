import joblib

model_path = r'C:\Users\user\djangoMLDeployment\savedModels\PID_Model.joblib'

try:
    model = joblib.load(model_path)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
