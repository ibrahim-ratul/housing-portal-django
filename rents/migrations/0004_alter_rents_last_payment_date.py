# Generated by Django 3.2.16 on 2022-12-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0003_alter_rents_last_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rents',
            name='last_payment_date',
            field=models.DateField(default=None),
        ),
    ]
