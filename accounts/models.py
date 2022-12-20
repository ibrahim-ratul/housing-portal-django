from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    is_owner = models.BooleanField("Owner", default=False)
    is_tenant = models.BooleanField("Tenant", default=False)
    image = models.ImageField(default='account.png',
                              upload_to='profile_pics')
    full_name = models.CharField(max_length=70, default=None)
    phone = models.CharField(max_length=14, default=None)

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
