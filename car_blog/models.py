from django.db import models


# Список моделей

# Бренд
class Brand(models.Model):
    name = models.CharField("Название компании", max_length=200)
    tel = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название компании"
        verbose_name_plural = "Название компаний"


# Коробка передач
class Transmission(models.Model):
    name = models.CharField("Трансмиссия", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Трасмиссия"
        verbose_name_plural = "Трансмисии"


# Тип кузова
class Body_type(models.Model):
    name = models.CharField("Типы кузова", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузовов"


# Привод
class Gearing(models.Model):
    name = models.CharField("Привод", max_length=200)

    def __str__(self):
        return self.name


# Основные характеристики машины
class Characteristics(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    body_type = models.ForeignKey(Body_type, on_delete=models.CASCADE)
    gearing = models.ForeignKey(Gearing, on_delete=models.CASCADE)
    images = models.CharField("Картинка", max_length=200)
    color = models.CharField("Цвет", max_length=200)
    millage = models.CharField("Пробег", max_length=200)
    price = models.CharField("Цена", max_length=200)
