# Generated by Django 4.2.3 on 2023-09-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startupapp', '0007_alter_payments_amountpaid_alter_payments_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='amountPaid',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
