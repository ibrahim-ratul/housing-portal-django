from django.db import models
from django.db.models.signals import post_save

from house.models import House
from accounts.models import Accounts


class Rents(models.Model):
    owner = models.CharField(max_length=50)
    tenant = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    date_rented = models.DateField(default=None)
    last_payment_date = models.DateField(default=None)
    price = models.FloatField(default=None)
    title = models.CharField(max_length=120, default=None)

    def __repr___(self):
        return f"Owner: {self.owner} Tenant: {self.tenant} Title: {self.title}"


def rent_post_save(sender, instance, created, **kwargs):
    if created:
        print(instance.title)
        House.objects.get(title=instance.title).delete()


post_save.connect(rent_post_save, sender=Rents)
