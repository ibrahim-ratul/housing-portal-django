from django.db import models
from accounts.models import Accounts
from django.db.models.signals import pre_save, post_save
from house.models import House


class Rents(models.Model):
    owner = models.CharField(max_length=50)
    tenant = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    date_rented = models.DateField(default=None)
    last_payment_date = models.DateField(default=None)
    price = models.FloatField(default=None)
    title = models.CharField(max_length=120, default=None)


def rent_post_save(sender, instance, created, **kwargs):
    if created:
        House.objects.get(title=instance.title).delete()


post_save.connect(rent_post_save, sender=Rents)
