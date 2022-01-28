from django.shortcuts import render
# Create your views here.


def renderReg(request):
    return render(request, 'register.html')