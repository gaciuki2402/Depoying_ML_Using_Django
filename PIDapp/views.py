from django.shortcuts import render
import joblib
from django.http import JsonResponse
from joblib import load
import pandas as pd

model_path = r'C:\Users\user\djangoMLDeployment\savedModels\PID_Model.joblib'
model = load(model_path)

def predictor(request):
    return render(request, 'main.html')

# Define your view function
def formInfo(request):
    if request.method == 'POST':
        age = request.POST.get('age')
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
# create dataframe for input data
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
        y_pred = model.predict(input_data)[0]
        prediction = 'Positive' if y_pred == 1 else 'Negative'
        return JsonResponse({'prediction': prediction})
    return render(request, 'result.html')