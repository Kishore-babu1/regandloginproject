from django import forms
from .models import RegModel
class RegModelForm(forms.ModelForm):
    class Meta:
        model = RegModel
        widgets = {'password': forms.PasswordInput(), 'cpassword': forms.PasswordInput()}
        fields = ['firstname','lastname','username','password','cpassword','emailid','mobileno']
class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
