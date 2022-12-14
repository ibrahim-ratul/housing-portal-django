from django.db import models

# Create your models here.
OPTIONS = (("SELL", "SELL"), ("BUY", "BUY"),
           ("TAKE RENT", "TAKE RENT"), ("GIVE RENT", "GIVE RENT"))


class House(models.Model):
    title = models.CharField(max_length=120)
    # image = models.ImageField()
    address = models.TextField(max_length=250)
    option = models.TextField(
        max_length=9, choices=OPTIONS, default="TAKE RENT")
    price = models.DecimalField(decimal_places=3, max_digits=8)
    rooms = models.IntegerField(default=1)
    kitchen = models.IntegerField(default=1)
    balcony = models.IntegerField(default=1)
    washroom = models.IntegerField(default=1)
    description = models.TextField(null=True, blank=True)
