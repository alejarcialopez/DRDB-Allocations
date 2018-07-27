from django.db import models


class DRBDAllocation(models.Model):

    name = models.CharField(max_length=30)
    device = models.PositiveIntegerField()
    port = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        port_list = []
        device_list = []
        name_list = []
        objs = DRBDAllocation.objects.all()
        for obj in objs:
            port_list.append(obj.port)
            device_list.append(obj.device)
            name_list.append(int(obj.name.split('-')[2]))
        port_list = sorted(port_list)
        device_list = sorted(device_list)
        name_list = sorted(name_list)
        min_name = 1
        min_device = 3
        min_port = 7791
        while min_device in device_list:
            min_device += 1
        while min_name in name_list:
            min_name += 1
        while min_port in port_list:
            min_port += 1
        min_name = "mws-priv-{0}".format(min_name)
        self.name = min_name
        self.port = min_port
        self.device = min_device
        super(DRBDAllocation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
