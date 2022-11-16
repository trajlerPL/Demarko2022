from dataclasses import field
from importlib import resources
from django.contrib import admin
from .models import Kod_Zlecenia_Lakiernia, Lista_Email,  Nazwa_Wydzialu,  Pracownik_Lakiernia, Rejestracja_Lakiernia,  Zlecenie_Lakiernia
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field


# Register your models here.


admin.site.register(Zlecenie_Lakiernia)
admin.site.register(Pracownik_Lakiernia)
admin.site.register(Kod_Zlecenia_Lakiernia)
admin.site.register(Nazwa_Wydzialu)
admin.site.register(Lista_Email)


class PostResource(resources.ModelResource):

    Pracownik = Field()
    Nr_Zlecenia = Field()
    Kod_Zlecenia = Field()
    Czas = Field()
    Data = Field()

    class Meta:
        model=Rejestracja_Lakiernia
        fields= ('Pracownik','Nr_Zlecenia','Kod_Zlecenia','Czas','Data')
        export_order = fields

    def dehydrate_Pracownik(self, obj):
        return str(obj.Pracownik)

    def dehydrate_Nr_Zlecenia(self, obj):
        return str(obj.Nr_Zlecenia)

    def dehydrate_Kod_Zlecenia(self, obj):
        return str(obj.Kod_Zlecenia)

    def dehydrate_Czas(self, obj):
        return str(obj.Czas)

    def dehydrate_Data(self, obj):
        return str(obj.Data)


class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class=PostResource


admin.site.register(Rejestracja_Lakiernia, PostAdmin)
 