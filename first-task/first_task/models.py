from django.db import models
import csv


class DRBDAllocation(models.Model):

    name = models.CharField(max_length=30)
    device = models.PositiveIntegerField()
    port = models.PositiveIntegerField()

    @classmethod
    def create(cls, o, device=None, port=None, name=None):
        port_list = []
        device_list = []
        name_list = []
        objects = o.objects.all()
        for object in objects:
            port_list.append(object.port)
            device_list.append(object.device)
            if len(object.name.split('-')) == 3:
                name_list.append(int(object.name.split('-')[2]))
        port_list = sorted(port_list)
        device_list = sorted(device_list)
        name_list = sorted(name_list)
        looping = True
        min_port = 7791
        min_device = 3
        min_name = 1
        while looping:
            if min_port in port_list:
                min_port += 1
            if min_device in device_list:
                min_device += 1
            if min_name in name_list:
                min_name += 1
            else:
                looping = False
        allocation = cls(name=f'mws-priv-{min_name}', device=min_device, port=min_port)
        return allocation

    def __str__(self):
        return str(self.name)

