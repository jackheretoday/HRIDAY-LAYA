from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def patient(request):
    return render(request, 'patient.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def doctor(request):
    return render(request, 'doctor.html')