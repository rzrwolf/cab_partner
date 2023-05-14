from datetime import date, datetime, timedelta

from django.db import models
from django.utils.timezone import make_aware
from phonenumber_field.modelfields import PhoneNumberField


class PatientManager(models.Manager):
    def returnByDateVisited(self, verboseDate):
        today = make_aware(datetime.now())
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)
        match verboseDate:

            case 'today':
                return self.filter(visit__created__gt=today).distinct()
            case 'yesterday':
                yesterday = (today - timedelta(days=1))
                return self.filter(visit__created__gt=yesterday, visit__created__lt=today).distinct()
            case 'week':
                week = (today - timedelta(days=7))
                return self.filter(visit__created__gt=week).distinct()
            case 'month':
                month = (today - timedelta(days=30))
                return self.filter(visit__created__gt=month).distinct()
            case 'all':
                return self.all()
            case _:
                return self.filter(visit__created__gt=today).distinct()

# Create your models here.
class Gender(models.TextChoices):
    male = "Муж", "Муж."
    female = "Жен", "Жен."

class Patient(models.Model):
    surname = models.CharField("Фамилия", max_length=200)
    name = models.CharField("Имя", max_length=200)
    fathname = models.CharField("Отчество", max_length=200)
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    id = models.AutoField("Идентификатор", primary_key=True)
    dateofbirth = models.DateField("Дата рождения")
    gender = models.CharField("Пол", max_length=50, choices=Gender.choices, default=Gender.male)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)



objects = PatientManager()


class Meta:
    ordering = ['-created']


def returnFIO(self):
    return self.surname + " " + self.name + " " + self.fathname


def returnShortFIO(self):
    return self.surname + self.name[0] + self.fathname[0]


def returnAge(self):
    today = date.today()
    age = today.year - self.dateofbirth.year - (
            (today.month, today.day) < (self.dateofbirth.month, self.dateofbirth.day))
    return age


def returnAgeMonths(self):
    today = date.today()
    months = (today.year - self.dateofbirth.year) * 12 + (today.month - self.dateofbirth.month)
    return months


def __str__(self):
    return self.surname + " " + self.name + " " + self.fathname