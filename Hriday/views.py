from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib
import numpy as np
import json
import os
from django.conf import settings

# Dynamically find the model path
model_path = os.path.join(settings.BASE_DIR, 'Hriday', 'ml_models', 'heart_disease_model.pkl')

# Load model with error handling
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None  # Handle missing model file

# Home Page
def home(request):
    return render(request, 'home.html')

# Patient Page
def patient(request):
    return render(request, 'patient.html')

# Admin Login Page
def adminlogin(request):
    return render(request, 'adminlogin.html')

# Doctor Page
def doctor(request):
    return render(request, 'doctor.html')

# Video Call Page
def video_call(request):
    return render(request, 'video_call.html')

# Health Data Page
def health_data(request):
    return render(request, 'health_data.html')

# Recommendation Dashboard
def recommendation_dashboard(request):
    return render(request, 'recommendation_dashboard.html')

# Food Recommendation
def food_recommendation(request):
    return render(request, 'recomendation.html')

# Location Recommendation
def location_recommendation(request):
    return render(request, 'location_recomendation.html')

# Patient Signup
def patient_signup(request):
    return render(request, 'patient_signup.html')

# Doctor Signup
def doctor_signup(request):
    return render(request, 'doctor_signup.html')

#ECG Data
def ecg_data(request):
    return render(request,'embed_ECG.html')

# Prediction Page (Form-based submission)
def predict(request):
    if request.method == 'POST':
        try:
            if model is None:
                return render(request, 'result.html', {'result': 'Error: Model file not found'})

            # Extract numerical input values
            features = []
            for key, value in request.POST.items():
                if key == 'csrfmiddlewaretoken':
                    continue  # Skip CSRF token
                try:
                    features.append(float(value))  # Convert to float
                except ValueError:
                    return render(request, 'result.html', {'result': f"Error: Invalid input '{value}' for {key}"})

            # Ensure correct feature count (model expects exactly 13 inputs)
            if len(features) != 13:
                return render(request, 'result.html', {'result': "Error: Incorrect number of input features."})

            # Convert to NumPy array and reshape
            input_data = np.array([features])

            # Make prediction
            prediction = model.predict(input_data)
            result = "Heart Disease Detected" if prediction[0] else "No Heart Disease"

            return render(request, 'result.html', {'result': result})

        except Exception as e:
            return render(request, 'result.html', {'result': f"Error: {str(e)}"})

    return render(request, 'prediction.html')

# API Endpoint for Prediction (JSON-based)
@csrf_exempt
def predict_heart_disease(request):
    if request.method == 'POST':
        try:
            if model is None:
                return JsonResponse({'error': 'Model file not found'}, status=500)

            # Parse JSON data
            data = json.loads(request.body)
            
            # Validate input data
            if 'features' not in data or not isinstance(data['features'], list):
                return JsonResponse({'error': 'Invalid JSON format. Expected {"features": [values]}'}, status=400)

            # Convert input to NumPy array
            features = np.array(data['features']).reshape(1, -1)

            # Ensure correct number of features
            if features.shape[1] != 13:
                return JsonResponse({'error': 'Incorrect number of input features.'}, status=400)

            # Predict using the model
            prediction = model.predict(features)
            result = int(prediction[0])  # Convert NumPy value to int

            return JsonResponse({'prediction': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'message': 'Send a POST request with JSON data.'})
