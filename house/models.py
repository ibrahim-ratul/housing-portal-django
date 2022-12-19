from django.db import models
from accounts.models import Accounts
import random
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save


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
    slug = models.SlugField(unique=True, null=True, blank=True)


def slugify_instance_title(instance, save=False, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(1000_000, 25_500_000)
        slug = f"{slug}-{rand_int}"
        slugify_instance_title(instance, save=save, new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
    return instance


def house_pre_save(sender, instance, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance)


pre_save.connect(house_pre_save, sender=House)


def house_post_save(sender, instance, created, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(house_post_save, sender=House)
