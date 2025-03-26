from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Webpages
    path('', views.home, name='home'),  # Default home page
    path('admin/', admin.site.urls),
    path('patient.html', views.patient, name='patient'),
    path('adminlogin.html', views.adminlogin, name='adminlogin'),
    path('doctor.html', views.doctor, name='doctor'),
    path('video_call.html', views.video_call, name='video_call'),
    path('home.html', views.home, name='home'),
    path('health_data.html', views.health_data, name='health_data'),  # Add this
    path('recommendation_dashboard.html', views.recommendation_dashboard, name='recommendation_dashboard'), 
    path('recomendation.html', views.food_recommendation, name='food_recommendation'),  # Add this
    path('location_recomendation.html', views.location_recommendation, name='location_recommendation'),  # Add this
    path('patient_signup.html', views.patient_signup, name='patient_signup'),  # Add this
    path('doctor_signup.html', views.doctor_signup, name='doctor_signup'),  # Add this
    path('embed_ECG.html', views.ecg_data, name='ecg_data'),  # Add this
    # Prediction Routes
    path('prediction.html', views.predict, name='predict'),  # Form-based prediction
    path('api/predict/', views.predict_heart_disease, name='predict_heart_disease'),  # API endpoint
]
