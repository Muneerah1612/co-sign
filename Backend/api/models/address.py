from django.db import models
from django.contrib.auth.models import User


class Addresses(models.Model):
    address_generated=models.CharField(max_length=80)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    redeem_script=models.CharField(max_length=400)
    service_key = models.CharField(max_length=80)

    def __str__(self):
        return self.address_generated
    