from django.db import models

# Create your models here.


class File(models.Model):
    """Object for file group"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField()
    name = models.CharField(max_length=250)
    path = models.CharField(max_length=250)
    # userid = models.IntegerField()
    computed_ram = models.IntegerField()
    computed_vcpu = models.IntegerField()
    computed_capacity = models.IntegerField()
    user_ram = models.IntegerField()
    user_vcpu = models.IntegerField()
    ssd_ratio = models.FloatField(default=0.2)


class Vm(models.Model):
    """VM object"""

    name = models.CharField(max_length=200)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    capacity = models.IntegerField()
    no_disks = models.IntegerField()

