from django.shortcuts import render
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

def health_data(request):
    return render(request, 'health_data.html')

def recommendation_dashboard(request):
    return render(request, 'recommendation_dashboard.html')

def food_recommendation(request):
    return render(request, 'recomendation.html')

def location_recommendation(request):
    return render(request, 'location_recomendation.html')

def patient_signup(request):
    return render(request, 'patient_signup.html')

def doctor_signup(request):
    return render(request, 'doctor_signup.html')

# Prediction Page (Form-based submission)
def predict(request):
    if request.method == 'POST':
        try:
            if model is None:
                return render(request, 'prediction.html', {'result': 'Error: Model file not found'})

            # Extract user input from form
            features = [float(request.POST[key]) for key in request.POST.keys()]
            input_data = np.array([features])

            # Make prediction
            prediction = model.predict(input_data)
            result = "Heart Disease Detected" if prediction[0] else "No Heart Disease"

            return render(request, 'prediction.html', {'result': result})

        except Exception as e:
            return render(request, 'prediction.html', {'result': f"Error: {str(e)}"})

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
            features = np.array(data['features']).reshape(1, -1)

            # Predict using the model
            prediction = model.predict(features)
            result = int(prediction[0])  # Convert NumPy value to int

            return JsonResponse({'prediction': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'message': 'Send a POST request with JSON data.'})
