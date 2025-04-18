from django.db import models


class Tashkilot(models.Model):
    nomi = models.CharField(max_length=100)
    manzili = models.CharField(max_length=255)  # manzili maydoni
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    tashkilot_rahbari = models.CharField(max_length=100)
    tashkilot_turi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class Xodim(models.Model):
    tashkilot = models.ForeignKey(Tashkilot, related_name='xodimlar', on_delete=models.CASCADE)
    ismi = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.ismi} - {self.lavozimi}"
