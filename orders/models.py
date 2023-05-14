from django.db import models

# Create your models here.
from patients.models import Patient


class Order(models.Model):
    patients = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    id = models.AutoField("Идентификатор", primary_key=True)
    created = models.DateTimeField("Добавлен", auto_now_add=False, blank=False, )
    barcode = models.IntegerField("Заявка", blank=True, null=True)
    cito = models.BooleanField("CITO", default=False)
    notes = models.CharField("Комментарий", max_length=254, null=True, blank=True)
