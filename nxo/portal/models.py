from django.db import models

# Create your models here.


class File(models.Model):
    """Object for file group"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    path = models.FileField(upload_to='uploads/')
    # userid = models.IntegerField()
    computed_ram = models.IntegerField(default=0)
    computed_vcpu = models.IntegerField(default=0)
    computed_capacity = models.IntegerField(default=0)
    user_ram = models.IntegerField(default=0)
    user_vcpu = models.IntegerField(default=0)
    user_capacity = models.IntegerField(default=0)
    ssd_ratio = models.FloatField(default=0.2)

    def update_resources(self):
        vms = Vm.objects.all().filter(file=self)
        self.computed_vcpu = 0
        self.computed_ram = 0
        self.computed_capacity = 0

        for vm in vms:
            self.computed_vcpu += vm.vcpu
            self.computed_ram += vm.ram
            self.computed_capacity += vm.capacity

        if self.user_ram == 0:
            self.user_ram = self.computed_ram

        if self.user_vcpu == 0:
            self.user_vcpu = self.computed_vcpu

        if self.user_capacity == 0:
            self.user_capacity = self.computed_capacity

        self.save()


class Vm(models.Model):
    """VM object"""

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    vcpu = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
    powerstate = models.CharField(max_length=20, default='')
    capacity = models.IntegerField(default=0)
    no_disks = models.IntegerField(default=0)

