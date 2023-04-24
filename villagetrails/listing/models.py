from django.db import models
from signin.models import VTUser
from django.utils.timezone import now


# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    startDate = models.DateTimeField(default=now)
    endDate = models.DateTimeField(default=now)
    hostId = models.ForeignKey(VTUser,on_delete=models.CASCADE, unique=False, to_field='id', related_name='host_id')
    guestId = models.ForeignKey(VTUser,default=1,on_delete=models.CASCADE, unique=False, to_field='id', related_name='guest_id')
    cost = models.FloatField(null=True)
    state = models.CharField(max_length=255)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)