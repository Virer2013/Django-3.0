# Generated by Django 3.1.1 on 2020-10-08 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20201005_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.pizza', verbose_name='Пицца')),
            ],
        ),
    ]
