# Generated by Django 3.2 on 2022-04-23 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='employee_number',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='社員番号'),
        ),
    ]
