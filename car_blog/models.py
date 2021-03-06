from django.db import models


# Create your models here.
class Transmission(models.Model):
    name = models.CharField("Трансмиссия", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трасмиссия"
        verbose_name_plural = "Трансмисии"


class Body_type(models.Model):
    name = models.CharField("Типы кузова", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузовов"


class Brend(models.Model):
    name = models.CharField("Название компании", max_length=200)
    tel = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название компании"
        verbose_name_plural = "Название компаний"

# class Model(models.Model):

