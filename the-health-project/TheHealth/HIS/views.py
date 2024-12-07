from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'patient-dashborad.html')

def adminLogin(request):
    return render(request, 'admin-login.html')

def createID(request):
    return render(request, 'create-id.html')