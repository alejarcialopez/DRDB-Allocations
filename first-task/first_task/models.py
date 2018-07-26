from django.db import models
import csv


class DRBDAllocation(models.Model):

    name = models.CharField(max_length=30)
    device = models.PositiveIntegerField()
    port = models.PositiveIntegerField()

    @classmethod
    def create(cls, name=None, device=None, port=None):
        port_list = []
        device_list = []
        name_list = []

        with open("/Users/aa2012/Documents/DRDB-Allocations/first-task/first_task/mws_allocations.txt",
                  'r') as file_allocation:
            content = csv.DictReader(file_allocation, delimiter=' ')
            for element in content:
                if '-' in element['shortname']:
                    device_list.append(int(element['device_number']))
                    port_list.append(int(element['port']))
                    name_list.append(int(element['shortname'].split('-')[2]))

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


