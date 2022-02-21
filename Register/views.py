import json
from wsgiref import validate
from django.forms import ValidationError
from django.shortcuts import redirect, render
from matplotlib.style import use
from Register.models import User
# Create your views here.
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
import random

from .forms import registerForm

def renderReg(request):
    if(request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cfmPassword = request.POST['cfmPassword']
        errors = {'usernameEr': '', 'emailEr': '', 'phoneEr': '', 'passwordEr': '', 'cfmEr': ''}
        form = registerForm(request.POST)
        # Validation
        if(len(username)<3):
            errors['usernameEr'] = 'Invalid first name.'
            return render(request, 'register.html', errors)
        else:
            if(User.objects.filter(username = username)):
                errors['usernameEr'] = 'Username already taken.'
                return render(request, 'register.html', errors)
        try:
            validate_email(email)
        except ValidationError as e:
            errors['emailEr'] = validate_email.message
            return render(request, 'register.html', errors)
            
        # if(User.objects.filter(email = email)):
        #     errors['emailEr'] = "Email already exists."
        #     return render(request, 'register.html', errors)
        
        if(len(phone)!=10):
            errors['phoneEr'] = 'Invalid phone number.'
            return render(request, 'register.html', errors)

        if(len(phone)==10):
            try:
                int(phone)
            except Exception as e:
                errors['phoneEr'] = 'Invalid phone number.'
                valid=False
                return render(request, 'register.html', errors)

        if(len(password)>=0):
            try:
                validate_password(password)
            except Exception as e:
                errors['passwordEr'] = e.messages[0]
                return render(request, 'register.html', errors)

        if(password != cfmPassword):
            errors['cfmEr'] = 'Passwords did not match.'
            return render(request, 'register.html', errors)

        if(form.is_valid() == False):
            return render(request, 'register.html', errors)

        else:
            user = User.objects.create_user(username = username, phone = phone, email = email, password = cfmPassword)
            user.save()
            return redirect('/login')

    else:
        return render(request, 'register.html')
