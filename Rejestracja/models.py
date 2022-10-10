from asyncio.windows_events import NULL
from datetime import datetime
from msilib.schema import Class
from pickle import TRUE
from tabnanny import verbose
from django.db import models


class Zlecenie(models.Model):
    Nr_Zlecenia = models.CharField(max_length=15)
    Nazwa_Projektu = models.CharField(max_length=15, null=TRUE)
    def __str__(self):
        return self.Nr_Zlecenia

    class Meta:
        verbose_name = "Zlecenie"
        verbose_name_plural = "Zlecenia"


class Pracownik(models.Model):
    Nr_Pracownika = models.DecimalField(max_digits=5,decimal_places=0)
    Imie = models.CharField(max_length=50)
    Nazwisko = models.CharField(max_length=50)
    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko

    class Meta:
        verbose_name = "Pracownik"
        verbose_name_plural = "Pracownicy"


class Kod_Zlecenia(models.Model):
    Nazwa_kodu = models.CharField(max_length=30, null=TRUE)
    Numer_kodu = models.DecimalField(max_digits=5, decimal_places=0)
    def __str__(self):
        return self.Nazwa_kodu

    class Meta:
        verbose_name = "Operacja"
        verbose_name_plural = "Operacje"




class Nazwa_Wydzialu(models.Model):
    Nazwa_W = models.CharField(max_length=50)
    def __str__(self):
        return self.Nazwa_W

    class Meta:
        verbose_name = "Wydział"
        verbose_name_plural = "Wydziały"


class Formularz(models.Model):

    Wydział = models.ForeignKey(Nazwa_Wydzialu,on_delete=models.CASCADE,null=TRUE)
    Pracownik = models.ForeignKey(Pracownik,on_delete=models.CASCADE,null=TRUE)
    Nr_Zlecenia = models.ForeignKey(Zlecenie,on_delete=models.CASCADE,null=TRUE)
    Kod_Zlecenia = models.ForeignKey(Kod_Zlecenia,on_delete=models.CASCADE,null=TRUE)
    Czas = models.DecimalField(max_digits=10, decimal_places=2,null=TRUE)
    Data = models.DateField(datetime(2022, 10, 10),null=TRUE)


    class Meta:
        verbose_name = "Formulerz"
        verbose_name_plural = "Formularze"



