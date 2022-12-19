# Generated by Django 3.2.16 on 2022-12-19 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(default='default.jpg', upload_to='inventory')),
                ('address', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('rooms', models.IntegerField(default=1)),
                ('kitchen', models.IntegerField(default=1)),
                ('balcony', models.IntegerField(default=1)),
                ('washroom', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
