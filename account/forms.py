from django import forms
from django.contrib.auth.models import User

from django.forms import ModelForm
from employee_data.models import Data

# Create the form class.
class DataForm(ModelForm):

    # Form to get employee data for the data model
    class Meta:
         model = Data
         fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
    
    # Form to get registration info
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']