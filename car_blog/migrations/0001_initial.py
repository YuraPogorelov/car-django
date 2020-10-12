# Generated by Django 3.1.1 on 2020-10-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Body_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Типы кузова')),
            ],
            options={
                'verbose_name': 'Тип кузова',
                'verbose_name_plural': 'Типы кузовов',
            },
        ),
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('logo', models.ImageField(max_length=255, upload_to='image/')),
                ('tel', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Название компании',
                'verbose_name_plural': 'Название компаний',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тип двигателя')),
            ],
            options={
                'verbose_name': 'Тип двигателя',
                'verbose_name_plural': 'Типы длигателей',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Трансмиссия')),
            ],
            options={
                'verbose_name': 'Трасмиссия',
                'verbose_name_plural': 'Трансмисии',
            },
        ),
    ]
