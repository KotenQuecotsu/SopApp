from django.db import models
from django.db.models import CharField


class Person(models.Model):
    name = models.CharField(max_length=100)
    subname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/')
    birth_date = models.DateField("Дата рождения")
    personal_chars = models.CharField(max_length=400, default=' ')
    breaks = models.CharField(max_length=400,default=' ')
    

