from django.shortcuts import render
from django.http import JsonResponse
from joblib import load
import pandas as pd
import os

# Define the model path
model_path = r'C:\Users\user\djangoMLDeployment\savedModels\PID_Model.joblib'

# Load the model with error handling
try:
    model = load(model_path)
    print("Model loaded successfully")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    if request.method == 'POST':
        try:
            age = int(request.POST.get('age'))
            stds_uti_history = request.POST.get('stds_uti_history')
            iud_use = request.POST.get('iud_use')
            past_pelvic_pain = request.POST.get('past_pelvic_pain')
            imaging_results = request.POST.get('imaging_results')
            abnormal_discharge = request.POST.get('abnormal_discharge')
            irregular_periods = request.POST.get('irregular_periods')
            dyspareunia = request.POST.get('dyspareunia')
            dysuria = request.POST.get('dysuria')
            wbc_count = request.POST.get('wbc_count')
            esr = request.POST.get('esr')
            crp_level = request.POST.get('crp_level')

            # Create dataframe for input data
            input_data = pd.DataFrame({
                'Age': [age],
                'STDs/UTI History': [stds_uti_history],
                'IUD Use': [iud_use],
                'Past Pelvic Pain': [past_pelvic_pain],
                'Imaging Results': [imaging_results],
                'Abnormal Discharge': [abnormal_discharge],
                'Irregular Periods': [irregular_periods],
                'Dyspareunia': [dyspareunia],
                'Dysuria': [dysuria],
                'WBC Count': [wbc_count],
                'ESR': [esr],
                'CRP Level': [crp_level]
            })

            # Make prediction
            if model is not None:
                y_pred = model.predict(input_data)[0]
                prediction = 'Positive' if y_pred == 1 else 'Negative'
            else:
                return JsonResponse({'error': 'Model not loaded properly'}, status=500)

            return JsonResponse({'prediction': prediction})

        except Exception as e:
            return JsonResponse({'error': f"Prediction error: {e}"}, status=400)

    return render(request, 'result.html')
