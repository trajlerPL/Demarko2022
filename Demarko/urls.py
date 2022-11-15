from tokenize import Name
from unicodedata import name
from django.contrib import admin
from django.urls import path
from pip import main
from Rejestracja.views import *
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('Strona_glowna', base),
    path('Rejestracja',registrationoftime),
    path('Kontakt',contact),
    path('Wydajnosc',wydajnosc),
    path('Zgloszenia',alerts),
    path('Inne',inne),
    path('Reg_paintshop',registartion_paintshop),
    path('Reg_assembly',registartion_assembly),
    path('Reg_welding',registartion_assembly),
    path('Reg_prepare',registartion_assembly),
    path('Efi_paintshop',efficiency_paintshop),
    path('Efi_assembly',efficiency_paintshop),
    path('Efi_welding',efficiency_paintshop),
    path('Efi_prepare',efficiency_paintshop),
    
]


urlpatterns += staticfiles_urlpatterns()