# Generated by Django 5.0.6 on 2024-07-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='miniAmountToUseCoupon',
            field=models.PositiveBigIntegerField(default='100'),
        ),
    ]
