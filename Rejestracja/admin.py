from django.contrib import admin
from .models import Formularz, Kod_Zlecenia, Nazwa_Wydzialu, Pracownik, Zlecenie


# Register your models here.

admin.site.register(Formularz)
admin.site.register(Zlecenie)
admin.site.register(Pracownik)
admin.site.register(Kod_Zlecenia)
admin.site.register(Nazwa_Wydzialu)