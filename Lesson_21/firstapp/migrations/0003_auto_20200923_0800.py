# Generated by Django 3.1.1 on 2020-09-23 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizza',
            options={'verbose_name': 'Пицца', 'verbose_name_plural': 'Пиццы'},
        ),
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
    ]
