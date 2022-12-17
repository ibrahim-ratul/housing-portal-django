from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    is_owner = models.BooleanField("Owner", default=False)
    is_tenant = models.BooleanField("Tenant", default=False)
