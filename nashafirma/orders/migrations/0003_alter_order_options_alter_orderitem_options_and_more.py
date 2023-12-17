# Generated by Django 4.2.7 on 2023-12-17 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_alter_product_options_alter_product_price_and_more'),
        ('orders', '0002_alter_order_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['created_at', 'user'], 'verbose_name': 'замовлення', 'verbose_name_plural': 'замовлення'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['order', 'product', 'weight'], 'verbose_name': 'продукти', 'verbose_name_plural': 'продукти'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='створено'),
        ),
        migrations.AlterField(
            model_name='order',
            name='done',
            field=models.BooleanField(default=False, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='orders.OrderItem', to='products.product', verbose_name='продукти'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='користувач'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='note',
            field=models.CharField(blank=True, max_length=100, verbose_name='нотатка'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='замовлення'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='продукт'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='weight',
            field=models.FloatField(default=0, verbose_name='вага'),
        ),
    ]
