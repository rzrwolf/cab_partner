from django.shortcuts import render

# Create your views here.


def loginView(request):
    return render(request, 'login.html')


def logoutView(request):
    return None


def dashboard(request):

    return render(request, 'main.html')