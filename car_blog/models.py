from django.db import models


# Create your models here.
class Transmission(models.Model):
    name = models.CharField("Коробка передач", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Коробка передач"
        verbose_name_plural = "Коробки передачи"


class Body_type(models.Model):
    name = models.CharField("Типы кузова", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузовов"


class Brend(models.Model):
    counter = models.CharField("Страна", max_length=200, null=True)
    name = models.CharField("Название компании", max_length=200)
    logo = models.ImageField("Логотип компании", upload_to='logo/', max_length=255)
    tel = models.CharField("Телефон", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Название компании"
        verbose_name_plural = "Название компаний"


class Engine(models.Model):
    name = models.CharField("Тип двигателя", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип двигателя"
        verbose_name_plural = "Типы длигателей"


class Model(models.Model):
    brend = models.ForeignKey(Brend, verbose_name="Фирма", on_delete=models.CASCADE, null=True)
    name = models.CharField("Марка", max_length=255)

    def __str__(self):
        return f"{self.brend} - {self.name}"

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"


class Characteristics(models.Model):
    model = models.ForeignKey(Model, verbose_name='Модели', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField("Фото", upload_to="image/", max_length=255, null=True)
    color = models.CharField("Цвет авто", max_length=200, null=True)
    transmission = models.ForeignKey(Transmission, verbose_name="Тип коробки передач", on_delete=models.CASCADE, null=True)
    body_type = models.ForeignKey(Body_type, verbose_name="Тип кузова", on_delete=models.CASCADE, null=True)
    engine = models.ForeignKey(Engine, verbose_name="Тип двигателя", on_delete=models.CASCADE, null=True)
    power = models.CharField('Мощьность', max_length=100, null=True)
    old = models.DateField("Год выпуска", null=True)
    milli = models.CharField("Пробег", max_length=100, null=True)
    price = models.CharField("Стоимость", max_length=100, null=True)

    def __str__(self):
        # return self.model
        return f"{self.model} - {self.price}"

    class Meta:
        verbose_name = "Основные характеристики машины"
        verbose_name_plural = "Основные характеристики машин"
