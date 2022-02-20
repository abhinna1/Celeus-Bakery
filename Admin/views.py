from django.shortcuts import render

# Create your views here.

def AdminPanel(request):
    return render(request, 'adminproducts.html')