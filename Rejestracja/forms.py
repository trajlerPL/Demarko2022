from dataclasses import fields
import email
from logging import PlaceHolder
from pyexpat import model
from tkinter import Widget
from tkinter.tix import Form
from django import forms
from django.forms import ModelForm
from .models import *


#Formularz kontaktowy

class Form_paintshop(ModelForm):
    class Meta:
        model = Rejestracja_Lakiernia
        fields = '__all__'


        labels = {
            'Pracownik' : 'Pracownik',
            'Nr_Zlecenia' : ' Nr Zlecenia SAP/ Nr Naczepy ',
            'Kod_Zlecenia' : ' Kod rejestracji pracy ',
            'Czas' : 'Czas pracy',
            'Data': 'Data aktywności',
        }



        widgets = {
            'Pracownik' : forms.Select(attrs={'class':'form-control'}),
            'Nr_Zlecenia' : forms.Select(attrs={'class':'form-control'}),
            'Kod_Zlecenia' : forms.Select(attrs={'class':'form-control'}),
            'Czas' : forms.TextInput(attrs={'class':'form-control'}),
            'Data': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RRRR-MM-DD'}),

        }

       