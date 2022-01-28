from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


__all__ = ['UserForm', 'StatusForm']

class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=(forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'})))
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'profile_pic', 'birth_date','email','password1')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # del self.fields['password1']
        del self.fields['password2']
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        