from dataclasses import fields
import django_filters
from .models import Rejestracja_Lakiernia


class Filtr_LAK(django_filters.FilterSet):

    class Meta:
        
        model = Rejestracja_Lakiernia
        fields = ('Pracownik', 'Data')