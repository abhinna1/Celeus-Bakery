from django.shortcuts import render
# Create your views here.


def renderLogin(request):
    return render(request, 'login.html')