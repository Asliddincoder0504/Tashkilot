from django.shortcuts import render
from .models import Tashkilot

def home(request):
    return render(request, 'home.html')


def tashkilotlar(request):
    # Tashkilotlar ma'lumotlarini bazadan olish
    tashkilotlar = Tashkilot.objects.all()

    # 'tashkilot/tashkilot.html' shablonini chaqirish va 'tashkilotlar' o'zgaruvchisini uzatish
    return render(request, 'tashkilot_list.html', {'tashkilotlar': tashkilotlar})