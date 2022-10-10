from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Formularz



#Formularz rejestracji czasu pracy


class Formularzform(ModelForm):
    class Meta:
        model = Formularz
        fields = ("__all__")