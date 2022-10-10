from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import render
from .models import  Formularz, Kod_Zlecenia




def formularz(request):
    polaczenie = Formularz.objects.all()
    dane = {'polaczenie_z_html' : polaczenie}
    return render(request, 'form.html', dane)





def Polaczenie (request, id):
    typ1_user = Formularz.objects.get(pk=id)
    typ3    =   "<h1>"  +   str(typ1_user)          +   "</h1>" +   \
                "<p>"   +   str(typ1_user.Wydział)  +   "</p>"  +   \
                "<p>"   +   str(typ1_user.Pracownik)+   "</p>"  
    return HttpResponse(typ3)





def Polaczenie2 (request, id):
    typ2_user = Kod_Zlecenia.objects.get(pk=id)
    return HttpResponse(typ2_user.Numer_kodu)