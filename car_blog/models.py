from django.db import models


# Create your models here.
class Color(models.Model):
    name = models.CharField("Color", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
