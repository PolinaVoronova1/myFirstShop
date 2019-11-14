# Generated by Django 2.2.4 on 2019-11-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_delete_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CA', 'Cash'), ('CR', 'Credit'), ('PP', 'PrivatPay'), ('POP', 'Pay of parts'), ('POC', 'Pay of card')], default='CR', max_length=100, null=True),
        ),
    ]
