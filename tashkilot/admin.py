from django.contrib import admin
from .models import Tashkilot, Xodim

# Tashkilot modeli uchun admin sozlamalari
@admin.register(Tashkilot)
class TashkilotAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'manzili', 'telefon', 'email', 'tashkilot_rahbari', 'tashkilot_turi')
    search_fields = ('nomi', 'manzili')

# Xodim modeli uchun admin sozlamalari
@admin.register(Xodim)
class XodimAdmin(admin.ModelAdmin):
    list_display = ('ismi', 'lavozimi', 'tashkilot', 'telefon', 'email')
    list_filter = ('tashkilot', 'lavozimi')
    search_fields = ('ismi', 'lavozimi')