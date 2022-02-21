from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def AboutPage(request):
    return render(request, 'About.html')

def ServicesPage(request):
    return render(request, 'services.html')
