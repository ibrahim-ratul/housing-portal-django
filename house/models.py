from django.db import models
from accounts.models import Accounts

# Create your models here.


class House(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(default='default.jpg', upload_to='inventory')
    address = models.TextField(max_length=250)
    price = models.DecimalField(decimal_places=3, max_digits=8)
    rooms = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=1)
    balcony = models.IntegerField(default=1)
    washroom = models.IntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, default=None)
