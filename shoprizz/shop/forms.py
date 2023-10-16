from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import  MaxValueValidator
from django import forms


class RegisterForm(UserCreationForm):
    customer_first_name = forms.CharField(max_length=155, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    customer_last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    customer_phone_number = forms.IntegerField(validators=[MaxValueValidator(99999999999)], required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No.'}))
    customer_email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    customer_registered_date = forms.DateField(required=False, widget=forms.HiddenInput())

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
    
    class Meta:
        model = User
        fields = ('username', 'customer_first_name', 'customer_last_name', 'customer_phone_number', 'customer_email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. Maximum 10 characters only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Your password cannot be too similar to your other personal information. </small></span>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
