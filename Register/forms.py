from django import forms

input_class = "form-control my-4 py-2"

class registerForm(forms.Form):
    username = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    cfmPassword = forms.CharField(max_length=100, widget=forms.PasswordInput)
