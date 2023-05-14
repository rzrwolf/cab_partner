import uuid

from django.db import models

# Create your models here.
from orders.models import Order


class ProbeGroup(models.Model):
    name = models.CharField("Название Группы", max_length=200, blank=True, null=True)
    description = models.CharField("Описание", max_length=200, blank=True, null=True)
    id = models.UUIDField("Идентификатор", default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    order = models.IntegerField("Порядок", default=1)

    def __str__(self):
        return str(self.name)


class Probe(models.Model):
    name = models.CharField("Название теста", max_length=200, blank=True, null=True)
    description = models.CharField("Описание", max_length=200, blank=True, null=True)
    id = models.AutoField("Идентификатор", primary_key=True)
    order = models.IntegerField("Порядок", default=1)
    enabled = models.BooleanField("Включен для клиента", default=True)
    related_to_probegroup = models.ForeignKey(ProbeGroup, on_delete=models.CASCADE, null=True, blank=True,
                                              verbose_name="Привязка к группе")
    probeSpecial = models.CharField("Спец.маркер", max_length=250, blank=True, null=True)

    code = models.CharField("Код", max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return str(self.name)


class ProbeInst(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE, null=True, verbose_name="Тест")
    id = models.AutoField("Идентификатор", primary_key=True)
    related_to_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,
                                         verbose_name="Привязка к анализу")
    created = models.DateTimeField("Создан", null=True, blank=True, )
    status = models.BooleanField("В работе", default=True)
    flag = models.BooleanField("Флаг", null=True, blank=True)
    comment = models.CharField("Название теста", max_length=200, blank=True, null=True)
