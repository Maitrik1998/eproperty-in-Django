from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from property.models import Property

class PropertyForm(forms.ModelForm):  
    class Meta:  
        model = Property  
        fields = "__all__" 


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2') 