from django import forms
from .models import Payment
from django.contrib.auth.models import User

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('when','how_much')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
