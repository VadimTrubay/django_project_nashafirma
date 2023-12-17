# Generated by Django 4.2.7 on 2023-12-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product', 'price'], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукт'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=100, verbose_name='продукт'),
        ),
    ]