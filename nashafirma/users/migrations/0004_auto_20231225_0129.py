# Generated by Django 3.2 on 2023-12-24 23:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='ваш email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адреса відправника'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='first_name',
            field=models.CharField(default='', max_length=25, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='імя'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='username',
            field=models.CharField(default='', max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='логін'),
        ),
    ]