from urllib import request
from webbrowser import get
from django import views
from django.forms import formset_factory
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.forms import formset_factory

from .filters import Filtr_LAK

from .models import Rejestracja_Lakiernia
from .forms import Form_paintshop 



#Strona główna

def main(request):     
    return render(request, 'Strona_glowna.html',   {})

def base(request):     
    return render(request, 'Strona_glowna.html',   {})   

def wydajnosc(request):     
    return render(request, 'Wydajnosc.html',   {})

def alerts(request):     
    return render(request, 'Zgloszenia.html',   {})

def inne(request):     
    return render(request, 'Inne.html',   {})

#Panel rejestracji czasu pracy 

def registrationoftime(request):     
    return render(request, 'Rejestracja.html',   {})

def registartion_paintshop(request):
    form = Form_paintshop()

    if request.method == "POST":
        print(request.POST)
        form = Form_paintshop(request.POST)
        if form.is_valid():
            form.save()
 
    ShowLakiernia = Rejestracja_Lakiernia.objects.all()
    MojFiltr = Filtr_LAK(request.GET, queryset=ShowLakiernia)
    ShowLakiernia =  MojFiltr.qs  


    dane = {'form':form,'Tabelka': ShowLakiernia, 'filtrhtml': MojFiltr}
    return render (request, 'Reg_paintshop.html', dane)



#Panel wykazu pracy

   


def registartion_assembly(request):
    return render(request, 'Reg_assembly.html', {})   

def registartion_welding(request):
    return render(request, 'Reg_welding.html', {})   

def registartion_prepare(request):
    return render(request, 'Reg_prepare.html', {})   


#Panel kontaktowy

def contact(request):     
    return render(request, 'Kontakt.html',   {})


#Panel wydajność

def efficiency_prepare(request):
    return render(request, 'Efi_prepare.html', {})   

def efficiency_welding(request):
    return render(request, 'Efi_welding.html', {})   

def efficiency_paintshop(request):
    return render(request, 'Efi_paintshop.html', {})   

def efficiency_assembly(request):
    return render(request, 'Efi_assemlby.html', {})   