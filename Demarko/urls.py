from tokenize import Name
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Rejestracja.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', formularz),
    path('Rejestracja/<id>', Polaczenie, name='Rejestracja'),
    path('Kody/<id>', Polaczenie2, name='Kody'),
]
