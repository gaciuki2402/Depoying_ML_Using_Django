from django.shortcuts import render
from django.http import JsonResponse

from joblib import load
import pandas as pd
import os
model = load('./savedModels/PID_Model.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    age = request.GET['age']
    stds_uti_history = request.GET['stds_uti']
    iud_use = request.GET['iud_use']
    past_pelvic_pain = request.GET['past_pelvic_pain']
    imaging_results = request.GET['imaging_results']
    abnormal_discharge = request.GET['abnormal_discharge']
    irregular_periods = request.GET['irregular_periods']
    dyspareunia = request.GET['dyspareunia']
    dysuria = request.GET['dysuria']
    wbc_count = request.GET['wbc_count']
    esr = request.GET['esr']
    crp_level = request.GET['crp_level']
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
    return JsonResponse({'prediction': 'Positive' if y_pred == 1 else 'Negative'})
    return render(request, 'result.html')